import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_setter_getter():
    c = Customer("Julius")
    assert c.name == "Julius"
    with pytest.raises(ValueError):
        c.name = ""  # too short
    with pytest.raises(ValueError):
        c.name = "a" * 16  # too long
    with pytest.raises(ValueError):
        c.name = 123  # not a string

def test_orders_and_coffees_relationship():
    c = Customer("Anna")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    order1 = Order(c, coffee1, 5.0)
    order2 = Order(c, coffee2, 6.0)
    assert order1 in c.orders()
    assert order2 in c.orders()
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_create_order_method():
    c = Customer("Ben")
    coffee = Coffee("Espresso")
    order = c.create_order(coffee, 7.0)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 7.0
    assert order in c.orders()

def test_most_aficionado():
    c1 = Customer("C1")
    c2 = Customer("C2")
    coffee = Coffee("Black")
    o1 = Order(c1, coffee, 5.0)
    o2 = Order(c1, coffee, 3.0)
    o3 = Order(c2, coffee, 10.0)
    # c2 spent 10, c1 spent 8 total
    assert Customer.most_aficionado(coffee) == c2
    # Test with no orders returns None
    coffee2 = Coffee("Decaf")
    assert Customer.most_aficionado(coffee2) is None
