from abc import abstractmethod

import reflex as rx


class GeneralTableState(rx.State):
    items: list[dict] = []
    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False
    total_items: int = 0
    offset: int = 0
    limit: int = 12
    excluded_fields: list[str] = []
    headers: list[str] = []

    @abstractmethod
    def load_entries(self):
        raise NotImplementedError

    @rx.var
    def filtered_sorted_items(self) -> list[dict]:
        items = self.items

        if self.sort_value:
            items = sorted(
                items,
                key=lambda item: str(item.get(self.sort_value, "")).lower(),
                reverse=self.sort_reverse,
            )

        if self.search_value:
            search_value = self.search_value.lower()
            items = [
                item
                for item in items
                if any(
                    search_value in str(value).lower() for key, value in item.items() if key not in self.excluded_fields
                )
            ]

        return items

    @rx.var
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var
    def total_pages(self) -> int:
        return (self.total_items // self.limit) + (1 if self.total_items % self.limit else 0)

    @rx.var
    def get_current_page(self) -> list[dict]:
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_items[start_index:end_index]

    def prev_page(self):
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self):
        if self.page_number < self.total_pages:
            self.offset += self.limit

    def first_page(self):
        self.offset = 0

    def last_page(self):
        self.offset = (self.total_pages - 1) * self.limit

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse

    def set_sort_value(self, value: str):
        self.sort_value = value

    def set_search_value(self, value: str):
        self.search_value = value
