from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
c1 = Customer("Byron")
c2 = Customer("Tiffany")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create orders
c1.create_order(latte, 5.0)
c1.create_order(latte, 6.0)
c1.create_order(mocha, 4.5)
c2.create_order(latte, 10.0)

# Test outputs
print(f"{c1.name} ordered: {[coffee.name for coffee in c1.coffees()]}")
print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Average price of {latte.name}: {latte.average_price():.2f}")
print(f"Most aficionado of {latte.name}: {Customer.most_aficionado(latte).name}")
