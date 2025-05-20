class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customer_totals = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer = order.customer
                customer_totals[customer] = customer_totals.get(customer, 0) + order.price
        if not customer_totals:
            return None
        
        return max(customer_totals, key=customer_totals.get)
