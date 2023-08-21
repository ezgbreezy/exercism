def is_armstrong_number(number):
    """
    Determines if a number is an Armstrong number. 

    An Armstrong number is a number that is the sum 
    of its own digits each raised to the power of the 
    number of digits.

    :param number: int or float - number on which to perform check
    :return: bool - is the number an armstrong number?
    """

    # Convert number to string
    number = str(number)

    # Get number of digits
    digits = len(number)
    sum = 0

    # Add each digit raised to number of digits to sum
    for digit in number:
        sum += int(digit) ** digits

    # Check if number is equal to sum
    return int(number) == sum
     
    