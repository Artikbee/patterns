"""
Adapter - это структурный паттерн проектирования, который
позволяет объекты с несовместимым интерфейсами работать вместе.

Паттерн Adapter особенно полезен, когда нужно обеспечить совместимость между
различными компонентами системы, не изменяя существующий код.
"""


class Dog:
    def bark(self):
        return "Гав!"


class Cat:
    def meow(self):
        return "Мяу!"


class CatAdapter:
    def __init__(self, cat: Cat):
        self.cat = cat

    def bark(self):
        return self.cat.meow()


def make_noise(animal: Dog | CatAdapter):
    print(animal.bark())


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    adapted_cat = CatAdapter(cat)

    print("Собака издает звук:")
    make_noise(dog)

    print("Кошка издает звук через адаптер:")
    make_noise(adapted_cat)
