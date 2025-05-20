import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_property():
    c = Coffee("Mocha")
    assert c.name == "Mocha"
    with pytest.raises(ValueError):
        Coffee("ab")  # too short
    with pytest.raises(ValueError):
        Coffee(123)  # not a string

def test_orders_and_customers_relationship():
    customer = Customer("Anna")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 6.0)
    assert order in coffee.orders()
    assert customer in coffee.customers()

def test_num_orders_and_average_price():
    customer = Customer("Bob")
    coffee = Coffee("Americano")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    Order(customer, coffee, 4.0)
    Order(customer, coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
