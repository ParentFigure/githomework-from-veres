""" 
Var 17
"""
from enum import Enum
import math

class Color(Enum):
    """ 
    Define a color
    """
    RED = 1
    GREEN = 2
    BLUE = 3


class Point:
    """ 
    Define a point
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    """
    Get x or y
    """
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    """
    Print out point data
    """
    def print_point(self):
        print(f"Point x = {self.x}, y = {self.y}")

    """
    Destructor
    """
    def __del__(self):
        print("Point has been deleted")

class Polynom:
    """ 
    Define a polynom with color and points
    """
    def __init__(self, color, *points):
        self.color = color
        self.points = list(points)

    """
    __repr__ method
    """
    def __repr__(self):
        return f"Polynom({self.color.name}, {', '.join(map(str, self.points))})"
    """
    Get values
    """
    def get_points(self):
        return self.points
    
    def get_color(self):
        return self.color
    """
    Print our polynom data
    """
    def print_polynom(self):
        print(f"Polynom color {self.color} with points {self.points}")
    """ 
    Perimeter
    """
    def perimeter(self):
        if len(self.points) < 2:
            return 0

        p = 0
        for i in range(len(self.points) - 1):
            p += math.dist((self.points[i].x, self.points[i].y), (self.points[i+1].x, self.points[i+1].y))
        p += math.dist((self.points[-1].x, self.points[-1].y), (self.points[0].x, self.points[0].y))
        return p
    """ 
    Longest diagonal
    """
    def longest_diagonal(self):
        if len(self.points) < 4:
            return 0

        max_distance = 0
        for i in range(len(self.points) - 1):
            for j in range(i+1, len(self.points)):
                distance = math.dist((self.points[i].x, self.points[i].y), (self.points[j].x, self.points[j].y))
                if distance > max_distance:
                    max_distance = distance
        return max_distance
    """ 
    Sort by x
    """
    def sort_by_x(self):
        def get_x(point):
            return point.x
        self.points.sort(key=get_x)
    """ 
    Sort by y
    """
    def sort_by_y(self):
        def get_y(point):
            return point.y
        self.points.sort(key=get_y)
    """
    Destructor
    """
    def __del__(self):
       print("Polynom has been deleted")

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(1, 2)
    point4 = Point(2, 1)

    polynom = Polynom(Color.RED, point1, point2, point3, point4)

    print("Original Polynom:")
    print(polynom)

    print(f"Perimeter: {polynom.perimeter()}")
    print(f"Longest Diagonal: {polynom.longest_diagonal()}")

    polynom.sort_by_x()
    print("\nSorted by X:")
    print(polynom)

    polynom.sort_by_y()
    print("\nSorted by Y:")
    print(polynom)  

    polynom1 = Polynom(Color.GREEN, point1, point2, point3)
    print(f"Perimeter: {polynom1.perimeter()}")
    print(f"Longest Diagonal: {polynom1.longest_diagonal()}")
    print(f"{polynom1}")

#MADE SOME COOL CHANGES!