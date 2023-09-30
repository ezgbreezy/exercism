def rebase(input_base: int, input_digits: list, output_base: int) -> int:
    """Converts a number from one base to another base.

    :param input_base: int - base of number to be converted
    :param digits: list - digits of number to be converted
    :param output_base: int - base to convert number too
    :return: int - converted number
    """

    # Check for valid input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    # Check for valid output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # Check for valid input digits
    for digit in input_digits:
        if input_base <= digit or 0 > digit:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    
    # Convert input to base 10 number
    base10 = get_base10(input_base, input_digits)

    # Get positions from base 10 number
    positions = root(base10, output_base)

    # Convert to output base
    output_number = []

    # Create list of possible output base digits
    output_base_digits = range(output_base)
    output_base_digits = list(reversed(output_base_digits))

    # Create list of position of output digit
    positions = list(range(positions))
    positions.reverse()

    # Calculate output number
    for position in positions:
        print(f"Position: {position}")
        current_factor = output_base ** position
        for digit in output_base_digits:
            if digit * current_factor <= base10 :
                print(f"Digit: {digit}")
                output_number.append(digit)
                if digit * current_factor != 0:
                    base10 %= digit * current_factor
                print(f"Base10: {base10}")
                break

    return output_number
        

def get_base10(input_base: int, digits: list) -> int:
    """Convert input digits to base 10 number

    :param input_base: int - base of number to be converted
    :param digits: list - digits of number to be converted
    :return: int - converted base 10 tnumber
    """

    base10 = int()
    digits.reverse()
    for iteration, digit in enumerate(digits):
        base10 += digit * (input_base ** iteration)
    return base10


def root(degree: int, radicand: int) -> int:
    """Calculate given root of radicand 

    :param degree: int - degree of root
    :param radicand: int - integer to find root of
    """
    root = 1
    while degree > radicand:
        degree /= radicand
        root += 1
    return root
