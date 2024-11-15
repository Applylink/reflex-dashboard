import reflex as rx

from reflex_dashboard.backend.table_state import GeneralTableState


def _header_cell(header: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.text(header),
            align="center",
            spacing="2",
        ),
    )

def _show_item(item: dict, index: int, headers: list[str]) -> rx.Component:
    bg_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 1),
        rx.color("accent", 2),
    )
    hover_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 3),
        rx.color("accent", 3),
    )
    return rx.table.row(
        rx.foreach(
            headers,
            lambda header: rx.table.cell(item[header]),
        ),
        style={"_hover": {"bg": hover_color}, "bg": bg_color},
        align="center",
    )

def _pagination_view(table_state) -> rx.Component:
    return (
        rx.hstack(
            rx.text(
                "Page ",
                rx.code(table_state.page_number),
                f" of {table_state.total_pages}",
                justify="end",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=table_state.first_page,
                    opacity=rx.cond(table_state.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(table_state.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=table_state.prev_page,
                    opacity=rx.cond(table_state.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(table_state.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=table_state.next_page,
                    opacity=rx.cond(
                        table_state.page_number == table_state.total_pages, 0.6, 1,
                    ),
                    color_scheme=rx.cond(
                        table_state.page_number == table_state.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=table_state.last_page,
                    opacity=rx.cond(
                        table_state.page_number == table_state.total_pages, 0.6, 1,
                    ),
                    color_scheme=rx.cond(
                        table_state.page_number == table_state.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                align="center",
                spacing="2",
                justify="end",
            ),
            spacing="5",
            margin_top="1em",
            align="center",
            width="100%",
            justify="end",
        ),
    )


def display_table(table_state: GeneralTableState) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.cond(
                    table_state.sort_reverse,
                    rx.icon(
                        "arrow-down-z-a",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=table_state.toggle_sort,
                    ),
                    rx.icon(
                        "arrow-down-a-z",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=table_state.toggle_sort,
                    ),
                ),
                rx.select(
                    table_state.headers,
                    placeholder=f"Sort By: {table_state.headers[0]}",
                    size="3",
                    on_change=table_state.set_sort_value,
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    rx.input.slot(
                        rx.icon("x"),
                        justify="end",
                        cursor="pointer",
                        on_click=table_state.setvar("search_value", ""),
                        display=rx.cond(table_state.search_value, "flex", "none"),
                    ),
                    value=table_state.search_value,
                    placeholder="Search here...",
                    size="3",
                    max_width=["150px", "150px", "200px", "250px"],
                    width="100%",
                    variant="surface",
                    color_scheme="gray",
                    on_change=table_state.set_search_value,
                ),
                align="center",
                justify="end",
                spacing="3",
            ),
            rx.button(
                rx.icon("arrow-down-to-line", size=20),
                "Export",
                size="3",
                variant="surface",
                display=["none", "none", "none", "flex"],
                on_click=rx.download(url="/items.csv"),
            ),
            spacing="3",
            justify="between",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.foreach(
                        table_state.headers,
                        _header_cell,
                    ),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    table_state.get_current_page,
                    lambda item, index: _show_item(item, index, table_state.headers),
                ),
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        _pagination_view(table_state),
        width="100%",
    )
