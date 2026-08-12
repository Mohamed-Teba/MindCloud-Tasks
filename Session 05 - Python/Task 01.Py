from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()
c.stop()


class FullAbstract(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class Duck:
    def quack(self):
        print("Quack!")


class Person:
    def quack(self):
        print("I'm quacking like a duck!")


class Dog:
    def bark(self):
        print("Woof!")


def make_it_quack(thing):
    # No type checking – just calls the method if it exists
    thing.quack()

make_it_quack(Duck())
make_it_quack(Person())