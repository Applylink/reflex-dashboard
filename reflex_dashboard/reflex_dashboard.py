"""Welcome to Reflex!."""
import reflex as rx

# Import all the pages.
from reflex_dashboard.pages import *  # noqa: F403

from . import styles

# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    # title="Dashboard Template",
    # description="A dashboard template for Reflex.",
)
