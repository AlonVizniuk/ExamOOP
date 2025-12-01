class Item:
    _next_id = 1

    def __init__(self, name, price):
        self.id = Item._next_id
        Item._next_id += 1
        self.name = name
        self.price = price