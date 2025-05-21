from customer import Customer
from coffee import Coffee
from order import Order


byron = Customer("Byron")
tiffany = Customer("Tiffany")


latte = Coffee("Latte")
mocha = Coffee("Mocha")


byron.create_order(latte, 5.0)
byron.create_order(mocha, 6.0)
tiffany.create_order(latte, 7.5)


print(f"Byron's coffees: {[c.name for c in byron.coffees()]}")
print(f"Tiffany's coffees: {[c.name for c in tiffany.coffees()]}")
print(f"Latte customers: {[c.name for c in latte.customers()]}")
print(f"Latte orders: {latte.num_orders()}")
print(f"Latte average price: {latte.average_price():.2f}")


top = Customer.most_aficionado(latte)
print(f"Most aficionado for latte: {top.name if top else 'None'}")
