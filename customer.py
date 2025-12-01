from customer_type import CustomerType
from gift import Gift
from item import Item


class Customer:
    _next_id = 1

    def __init__(self, first_name, last_name, email, delivery_address, customer_type: CustomerType, customer_discount, favorite_items, gift):
        self.id = Customer._next_id
        Customer._next_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = favorite_items
        self.gift = gift

    def get_items_names(self):
        return {item.name for item in self.favorite_items}

    def add_items_to_favorite(self, items: list):
        list_of_names = self.get_items_names()
        for item in items:
            if item.name not in list_of_names:
                self.favorite_items.append(item)
                list_of_names.add(item.name)

    def add_item_to_favorite(self, item: Item):
        list_of_names = self.get_items_names()
        if item.name not in list_of_names:
            self.favorite_items.append(item)

    def remove_item_from_favorite(self, item: Item):
        list_of_names = self.get_items_names()
        if item.name in list_of_names:
            self.favorite_items.remove(item)

    def take_gift(self, gift: Gift):
        self.gift = gift

    def open_gift(self):
        if self.gift is not None:
            self.gift.open_gift()
        else:
            print("No gift to open for this customer")
