"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""
import copy

class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

# Ex 1. Write a function called distance_between_points that takes two Points as arguments
# and returns the distance between them.


def distance_between_points(p1, p2):
    d =((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)  ** .5
    return d

# Ex 2. Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy.
# It should change the location of the rectangle by adding dx to the x coordinate of corner
# and adding dy to the y coordinate of corner.


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return f"({rect.corner.x},{rect.corner.y})"

# Ex 3.
# Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.


def move_rectangle_new(rect, dx, dy):
    rect_new = copy.deepcopy(rect)
    rect_new = move_rectangle(rect, dx, dy)
    return rect_new

# Ex 4.
# Write

# def main():
#     blank = Point()
#     blank.x = 3
#     blank.y = 4
#     print('blank',)
#     print_point(blank)
#
#     box = Rectangle()
#     box.width = 100.0
#     box.height = 200.0
#     box.corner = Point()
#     box.corner.x = 0.0
#     box.corner.y = 0.0
#
#     center = find_center(box)
#     print('center',)
#     print_point(center)
#
#     print(box.width)
#     print(box.height)
#     print('grow')
#     grow_rectangle(box, 50, 100)
#     print(box.width)
#     print(box.height)



if __name__ == '__main__':
    # main()
    p1 = Point()
    p1.x = 3
    p1.y = 4
    p2 = Point()
    p2.x = 0
    p2.y = 0
    print(distance_between_points(p1, p2))

    rect = Rectangle()
    rect.width = 1
    rect.length = 2
    rect.corner = p1
    print(move_rectangle(rect, 10, 10))

    print(move_rectangle_new(rect, 4, 5))
