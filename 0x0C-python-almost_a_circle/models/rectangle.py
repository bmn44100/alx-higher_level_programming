#!/usr/bin/python3
""" module that contains the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for class Rectangle """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    """ width of rectangle """
    return self.__width


@width.setter
def width(self, value):
    """ sets width as an integer """
    if type(value) is not int:
        raise TypeError('width must be an integer')
    if value <= 0:
        raise ValueError('width must be > 0')
    self.__width = value


@property
def height(self):
    """ height of rectangle """
    return self.__height


@height.setter
def height(self, value):
    """ sets height as an integer """
    if type(value) is not int:
        raise TypeError('height must be an integer')
    if value <= 0:
        raise ValueError('height must be > 0')
    self.__height = value


@property
def x(self):
    """ value x """
    return self.__x


@x.setter
def x(self, value):
    """ sets x as an integer """
    if type(value) is not int:
        raise TypeError('x must be an integer')
    if value < 0:
        raise ValueError('x must be >= 0')
    self.__x = value


@property
def y(self):
    """ value y """
    return self.__y


@y.setter
def y(self, value):
    """ sets y as an integer """
    if type(value) is not int:
        raise TypeError('y must be an integer')
    if value < 0:
        raise ValueError('y must be >= 0')
    self.__y = value


def area(self):
    """ claculates are of rectangle """
    return self.__width * self.__height


def display(self):
    """ print the rectangle with # """
    for i in range(self.__height):
        for j in range(self.__width):
            print("#", end="")
        print()


def __str__(self):
    """ Update the class Rectangle by overriding the __str__ method """
    return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
        .format(self.id, self.x, self.y, self.width, self.height)


def display(self):
    """ prints rectangle with character # """
    for i in range(self.__y):
        print()
    for k in range(self.__height):
        print(" " * self.__x, end="")
        for j in range(self.__width):
            print("#", end="")
        print()


def update(self, *args, **kwargs):
    """ updates the rectangle """
    if len(args) != 0:
        i = 0
        rect_attrs = ["id", "width", "height", "x", "y"]
        for arg in args:
            setattr(self, rect_attrs[i], args[i])
            i += 1
    else:
        for k, v in kwargs.items():
            setattr(self, k, v)


def to_dictionary(self):
    """ returns a dictionary representation of rectangle """
    rect_dict = {}
    rect_attrs = ["id", "width", "height", "x", "y"]
    for attr in rect_attrs:
        rect_dict[attr] = getattr(self, attr)
    return rect_dict
