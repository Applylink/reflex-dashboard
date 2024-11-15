"""The settings page."""

import reflex as rx

from reflex_dashboard.backend.supervisor_state import MySupervisorState
from reflex_dashboard.templates import template
from reflex_dashboard.views.table import display_table


@template(route="/my_supervisor", title="My Supervisor", on_load=MySupervisorState.load_entries)
def my_supervisor() -> rx.Component:
    return rx.vstack(
        rx.heading("My Supervisors", size="5"),
        display_table(MySupervisorState),
        spacing="8",
        width="100%",
    )
