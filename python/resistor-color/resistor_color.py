"""Functions for looking up resistance values.
"""

RESISTOR_COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> int:
    """Returns resistance value of a provided resistor color code.

    :param color: str - a resistor color code
    :return: int - the resistance value of the inputted color code
    """

    return RESISTOR_COLORS[color]

def colors() -> list:
    """Returns a list of resistor colors.

    :return: list - all the resistor colors
    """

    return list(RESISTOR_COLORS.keys())