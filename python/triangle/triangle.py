"""
Functions for evaluating types of triangles.
"""

def equilateral(sides):
    """
    Checks if a triangle is of type equilateral.

    :param sides: 'list' or 'tuple' - Sides of a triangle expressed as an 'int' or 'float'.
    """

    # Check for triangle inequality violation
    if not bool(valid_triangle(sides)):
        return False
    
    # Check if equilateral triangle
    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False


def isosceles(sides):
    """
    Checks if a triangle is of type isosceles.

    :param sides: 'list' or 'tuple' - Sides of a triangle expressed as an 'int' or 'float'.
    """

    # Check for triangle inequality violation
    if not bool(valid_triangle(sides)):
        return False
    
    # Check if isosceles triangle
    if (sides[0] == sides[1]
        or sides[0] == sides[2]
        or sides[1] == sides[2]):
        return True
    else:
        return False


def scalene(sides):
    """
    Checks if a triangle is of type scalene.

    :param sides: 'list' or 'tuple' - Sides of a triangle expressed as an 'int' or 'float'.
    """
    
    # Check for triangle inequality violation
    if not bool(valid_triangle(sides)):
        return False

    # Check if scalene triangle
    if sides[0] != sides[1] != sides[2] != sides[0]:
        return True
    else:
        return False


def valid_triangle(sides):
    """
    Checks if provided lengths of sides produce a valid triangle.

    :param sides: 'list' or 'tuple' - Sides of a triangle expressed as an 'int' or 'float'.
    """

    # Check if lengths are greater than 0
    for side in sides:
        if side <= 0:
            return False
    
    # Check if sum of two lengths greater than third length
    sum_of_sides = 0
    if (sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[0] + sides[2] >= sides[1]):
        return True
    else:
        return False
        


        
    
