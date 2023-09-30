def value(colors: list) -> int:
    """Returns resistance value of a provided resistor color code.

    :param color: list - resistor color codes
    :return: int - the resistance value of the inputted color code
    """

    RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]
    return int(str(RESISTOR_COLORS.index(colors[0])) + str(RESISTOR_COLORS.index(colors[1])))

   