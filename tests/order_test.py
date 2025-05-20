import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_init_validations():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

    with pytest.raises(TypeError):
        Order("not customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(customer, "not coffee", 5.0)
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    with pytest.raises(ValueError):
        Order(customer, coffee, "free")
