from typing import override
from animal import Animal
from pet import Pet


class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self.name = None

    @override
    def get_name(self) -> str:
        if self.name is None:
            return 'None'
        else:
            return self.name


    @override
    def set_name(self, name: str):
        self.name = name


    @override
    def play(self):
        pass

    @override
    def walk(self):
        pass

    @override
    def eat(self):
        pass



