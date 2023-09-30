from math import hypot

def score(x: int | float, y: int | float) -> int:
    """
    Calculates score of dart coordinates.

    :param x: int or float - x axis coordinate
    :param y: int or float - y axis coordinate
    :return: int - the score value of the coordinate position on the board
    """

    # Declare point zone constants
    INNER_ZONE = 1
    MIDDLE_ZONE = 5
    OUTER_ZONE = 10

    # Store point in tuple
    point = (x, y)

    # Get hypotenuese, check value against point zone
    match point:
        case point if hypot(x, y) <= INNER_ZONE:
            return 10
        case point if hypot(x, y) <= MIDDLE_ZONE:
            return 5
        case point if hypot(x, y) <= OUTER_ZONE:
            return 1
        case point if hypot(x, y) > OUTER_ZONE:
            return 0
        case _:
            raise ValueError
    
