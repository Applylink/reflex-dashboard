"""The settings page."""

import reflex as rx

from reflex_dashboard.components.navbar import navbar
from reflex_dashboard.templates import template


@template(route="/university", title="University")
def university() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("University", size="2xl"),
    )
