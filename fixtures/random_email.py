#!/usr/bin/env python3
"""
TODO: docstring
"""

import pytest
from utils.data_generator import email_generator


@pytest.fixture()
def random_email():
    """TODO: docstring
    :return: random email
    :rtype: string
    """

    return email_generator()
