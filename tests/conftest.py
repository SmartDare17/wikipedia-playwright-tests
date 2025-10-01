# tests/conftest.py
import pytest

@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1600, "height": 1000},  # desktop layout
        device_scale_factor=1.0,
    )
    p = context.new_page()
    yield p
    context.close()
