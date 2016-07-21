from pytest_bdd import scenario
from bdd.order_steps import *
from tests.conftest import *
from fixture.session import *

@scenario('all.feature','Registration New User')
def test_registration():
    pass

@scenario('all.feature', 'Order')
def test_order():
    pass