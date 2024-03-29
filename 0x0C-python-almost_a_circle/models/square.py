#!/usr/bin/python3
""" module that contains the class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for Square class
        Args:
            size (int): size of square
            x (int): x-coordinate
            y (int): y-coordinate
            id (int): id of square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ prints the unoffical string representation of rectangle """
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ finds Square height """
        return self.width

    @size.setter
    def size(self, size):
        """ sets Square size
        Args:
            size (int): size of square
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates the Square
        Args:
            args: arguments
            kwargs: key-word arguments
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """ returns dictionary representation of rectangle
        Returns:
            dictionary of attributes
        """
        obj_dict = {}
        for attr in ['id', 'size', 'x', 'y']:
            obj_dict[attr] = getattr(self, attr)
        return obj_dict
