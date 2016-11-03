#!/usr/bin/env python3
import pytest

pytest_plugins = ['fixtures.web_application', 'fixtures.random_email']


@pytest.fixture(autouse=True)
def g():
    global_dict = {}
    return global_dict
