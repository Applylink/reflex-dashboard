"""The settings page."""

import reflex as rx

from reflex_dashboard.components.navbar import navbar
from reflex_dashboard.templates import template


@template(route="/location", title="Location")
def location() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("Location", size="2xl"),
    )
