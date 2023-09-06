#!/usr/bin/python3

"""
This module contains Simple rectangle class with property and some methods
"""


class Rectangle:
    """This class is an empty class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Initializes a new rectangle instance
        and decremented the public class attribute
        number_of_instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allow width to be set"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allow height to be set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the rectangle area"""
        res = self.height * self.width
        return res

    def perimeter(self):
        """Return the perimeter of the retangle"""
        res = (self.height + self.width) * 2
        return res

    def __str__(self) -> str:
        """
        Returns a string representation of the
        rectangle using the '#' character.
        """
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return ""
        if hasattr(self, "print_symbol"):
            symbol_to_print = self.print_symbol
        else:
            Rectangle.print_symbol

        return "\n".join([f"{symbol_to_print}" * width for _ in range(height)])

    def __repr__(self):
        """Returns a string that can
        be used to recreate the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted
        and decremented the public class attribute
        number_of_instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This function returns the biggest
        rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        if rect_1_area > rect_2_area:
            return rect_1
        else:
            return rect_2
