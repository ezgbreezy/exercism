def leap_year(year):
    """
    Checks whether or not a given year is a leap year in the Gregorian calendar.

    :param year: 'int' - Year
    """

    # Check if year is leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False
    