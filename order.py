from datetime import datetime
from customer import Customer
from payment_type import PaymentType


class Order:
    _next_id = 1

    def __init__(self, name: str, delivery_address: str, order_items: list, customer: Customer, payment_type: PaymentType, order_date: datetime):
        self.order_id = Order._next_id
        Order._next_id += 1
        self.name = name
        self.delivery_address = delivery_address
        self.order_items = order_items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.customer.add_items_to_favorite(self.order_items)
        self.total_price = self.calculate_total_price()


    def calculate_total_price(self):
        total_price = 0
        for order_item in self.order_items:
            total_price += order_item.price
        return total_price