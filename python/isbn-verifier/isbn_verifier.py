def is_valid(isbn: str) -> bool:
    """
    Checks if ISBN-10 number is valid.

    :param isbn: str - ISBN number to check
    :return: bool - is the number valid?
    """

    # Convert to list and remove hyphens
    isbn = list(isbn.replace("-", ""))
    
    # Verify valid length
    if len(isbn) != 10:
        return False
    
    # Replace 'X'
    if isbn[9] == 'X':
        isbn[isbn.index('X')] = '10'
    elif isbn[9].isnumeric() == False:
        return False 
    
    # Perform formula verification
    multiplier = 10
    result = 0
    for digit in isbn:
        if digit.isnumeric() == False:
            return False
        result += int(digit) * multiplier
        multiplier -= 1
    result %= 11

    # Return result
    return result == 0
