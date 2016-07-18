from pytest_bdd import scenario
from bdd.order_steps import *
from tests.conftest import *
from fixture.session import *

@scenario('order.feature', 'Order')
def test_order():
    pass