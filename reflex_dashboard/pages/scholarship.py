"""The settings page."""

import reflex as rx

from reflex_dashboard.components.navbar import navbar
from reflex_dashboard.templates import template


@template(route="/scholarship", title="Scholarship")
def scholarship() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("Scholarship", size="2xl"),
    )
