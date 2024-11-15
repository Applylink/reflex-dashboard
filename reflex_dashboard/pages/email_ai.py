"""The settings page."""

import reflex as rx

from reflex_dashboard.backend.email_state import State
from reflex_dashboard.components.navbar import navbar
from reflex_dashboard.templates import template
from reflex_dashboard.views.email import email_gen_ui
from reflex_dashboard.views.email_table import main_table


@template(route="/email_ai", title="Email AI", on_load=State.load_entries)
def email_ai() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.flex(
            rx.box(main_table(), width=["100%", "100%", "100%", "60%"]),
            email_gen_ui(),
            spacing="6",
            width="100%",
            flex_direction=["column", "column", "column", "row"],
        ),
        height="100vh",
        bg=rx.color("accent", 1),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
        padding_y=["1em", "1em", "2em"],
    )
