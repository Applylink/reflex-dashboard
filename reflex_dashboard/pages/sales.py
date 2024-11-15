"""The settings page."""

import reflex as rx

from ..components.navbar import navbar
from ..templates import template
from ..views.email import email_gen_ui
from ..views.email_table import main_table


@template(route="/sales", title="Sales")
def sales() -> rx.Component:
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
