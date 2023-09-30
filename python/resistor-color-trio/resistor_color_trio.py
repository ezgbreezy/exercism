def label(colors: list) -> str:
    """Calculates resistance value in ohms of list of resistor color codes.

    :param colors: list - list of color codes
    :return: str - resistance value in ohms
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

    # Get first two color indices and concatenate 
    ohms = str(RESISTOR_COLORS.index(colors[0])) + str(RESISTOR_COLORS.index(colors[1]))
    
    # Concatenate zeros if they exist
    if RESISTOR_COLORS.index(colors[2]) != "black":
        ohms += '0' * RESISTOR_COLORS.index(colors[2])
    
    # Make int copy
    ohms_int = int(ohms)
    
    # Check results and return case
    match ohms:
        case ohms if ohms_int == 0:
            return "0 ohms"
        case ohms if ohms_int < 1000:
            return f"{ohms.lstrip('0')} ohms"
        case ohms if ohms_int < 1000000:
            return f"{ohms.lstrip('0')[:-3]} kiloohms"
        case ohms if ohms_int < 1000000000:
            return f"{ohms.lstrip('0')[:-6]} megaohms"
        case ohms if ohms_int < 1000000000000:
            return f"{ohms.lstrip('0')[:-9]} gigaohms"
