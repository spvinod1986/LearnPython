from abc import ABC, abstractmethod  # For abstract class
from collections import namedtuple  # For data classes


class Point:
    # These are class attributes
    default_color = "red"
    default_location = 10

    # Constructor
    def __init__(self, x, y):
        # These are instance attributes
        self.x = x
        self.y = y

    # This is instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # This is Class Method
    @classmethod  # decorator
    def zero(cls):
        cls(0, 0)

    # overriding magic method which is called when converting object to string
    def __str__(self):
        return f"({self.x}, {self.y})"

    # overriding equality magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # overriding greater than magic method
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # overriding add magic method
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
print(type(point))
print(isinstance(point, int))
point.draw()
print(point.default_color)
print(Point.default_color)
print(point)

# creating custom container class which works similar to dict, list etc


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("pYthon")
cloud.add("python")
print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])

# properties


class Product:
    def __init__(self, price):
        self.price = price

    # This is getter
    @property
    def price(self):
        return self.__price

    # This is setter. Commenting out the setter will result in readonly property
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than zero")
        self.__price = value


product = Product(50)
print(product.price)

# Inheritance


class Animal:  # object is the base class for all classes
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):  # Animal is base class
    def __init__(self):
        super().__init__()  # This calls the constructor in the base class
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):  # Animal is base class
    def swim(self):
        print("swim")


mammal = Mammal()
mammal.eat()
print(mammal.age)
print(mammal.weight)
print(isinstance(mammal, Mammal))
print(isinstance(mammal, Animal))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))

# multiple inheritance


class Flyer:
    def fly(self):
        print("fly")


class Swimmer:
    def swim(self):
        print("swim")


class FlyingFish(Flyer, Swimmer):
    pass

# Abstract Base Class


class Stream(ABC):
    def open(self):
        print("connection open")

    def close(self):
        print("connection close")

    @abstractmethod
    def read(self):
        pass


class MemoryStream(Stream):
    def read(self):
        print("reading data from memory")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network")


# This file will also be considered abstract if it does not implement abstract method
class FileStream(Stream):
    pass


stream = MemoryStream()

# duck typing


class TextBox():
    def draw(self):
        print("TextBox")


class DropdownList():
    def draw(self):
        print("DropdownList")


def draw(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
dropdownlist = DropdownList()
draw([textbox, dropdownlist])

# Extend built in types


class Text(str):
    def duplicate(self):
        return self + self


text = Text("python")
print(text.duplicate())

# data classes

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)
print(p1 == p2)
