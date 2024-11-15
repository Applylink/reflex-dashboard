"""Welcome to Reflex!."""

# Import all the pages.
import reflex as rx

from . import styles
from .pages import *  # noqa: F403

# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    # title="Dashboard Template",
    # description="A dashboard template for Reflex.",
)
