import pytest
from fixture.application import Application
from fixture.session import SessionHelper

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture