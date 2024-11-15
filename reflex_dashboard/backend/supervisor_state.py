from reflex_dashboard.backend.data_source import CSVDataSource
from reflex_dashboard.backend.table_state import GeneralTableState


class MySupervisorState(GeneralTableState):

    def load_entries(self):
        self.headers = ["name", "payment", "date", "status"]
        data_source = CSVDataSource("items.csv")
        self.items = data_source.get_data()
        self.total_items = len(self.items)
