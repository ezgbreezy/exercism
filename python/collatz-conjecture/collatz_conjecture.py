def steps(number):
    """
    Performs Collatz-Conjecture using a given positive whole integer.

    :param number: int - a positive whole integer.
    :return: int - number of steps to reach 1
    """

    # Test for valid input (positive number)
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # Perform Collatz-Conjecture
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            steps += 1
        else:
            number = 3 * number + 1
            steps += 1
    return steps
