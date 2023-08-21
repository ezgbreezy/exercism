"""
Calculates quantities of grains of wheat on a chessboard.
"""

def square(number):
    """
    Determines how many grains of wheat are on a given square.

    :param number: int - the square, between 1 and 64
    :return: int - the number of grains on the given square
    """

    # Check that number is valid chess square
    MAX = 64
    MIN = 1

    if number < MIN or number > MAX:
        raise ValueError("square must be between 1 and 64")

    # Calculate number of grains
    number_of_grains = 1

    for square in range(number - 1):
        number_of_grains *= 2
    return number_of_grains


def total():
    """
    The total number of grains on a chessboard.

    :return: int - the total number of grains
    """
    
    return (square(64) * 2) - 1
