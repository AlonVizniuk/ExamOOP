from datetime import datetime
from typing import override
from customer import Customer
from order import Order
from payment_type import PaymentType


class OrderVIP(Order):

    def __init__(self, name: str, delivery_address: str, order_items: list, customer: Customer, payment_type: PaymentType, order_date: datetime):
        super().__init__(name, delivery_address, order_items, customer, payment_type, order_date)



    @override
    def calculate_total_price(self):
        if self.customer.customer_type.value == 'VIP':
            before_discount = super().calculate_total_price()
            pay_percentage = 1 - self.customer.customer_discount
            return before_discount * pay_percentage
        else:
            raise Exception("VIP order with customer type 'Regular' is not supported")

        