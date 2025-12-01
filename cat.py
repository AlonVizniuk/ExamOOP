from typing import override
from animal import Animal
from pet import Pet


class Cat(Animal, Pet):
    def __init__(self,name= ""):
        super().__init__(4)
        self.name = name

    @override
    def set_name(self, name):
        self.name = name

    @override
    def get_name(self) -> str:
        return self.name

    @override
    def play(self):
        pass

    @override
    def eat(self):
        pass



