"""The table page."""

import reflex as rx

from reflex_dashboard.backend.table_state import TableState
from reflex_dashboard.templates import template
from reflex_dashboard.views.table import main_table


@template(route="/table", title="Table", on_load=TableState.load_entries)
def table() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        rx.heading("Table", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
