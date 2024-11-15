"""The settings page."""

import reflex as rx

from reflex_dashboard.components.navbar import navbar
from reflex_dashboard.templates import template


@template(route="/resume_ai", title="Resume AI")
def resume_ai() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading("Resume AI", size="2xl"),
    )
