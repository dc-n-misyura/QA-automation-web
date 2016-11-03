#!/usr/bin/env python3
"""
TODO: docstring
"""

import pytest
from core import get_application


@pytest.fixture()
def web_application():
    """Selenium web driver fixture. Used for initialize webdriver and
    maximize browser window.

    Since pytest 3.0 @yield_fixture decorator was deprecated, I could use
    # @fixture decorator to run tests without adding finalizer as other
    function.
    """

    app = get_application()

    yield app

    app.quit()
