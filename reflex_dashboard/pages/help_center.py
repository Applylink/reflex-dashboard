"""The help center page."""

from pathlib import Path

import reflex as rx

from reflex_dashboard import styles
from reflex_dashboard.templates import template


@template(route="/help_center", title="Help Center")
def help_center() -> rx.Component:
    """The about page.

    Returns:
        The UI for the about page.
    """
    with Path("README.md").open(encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
