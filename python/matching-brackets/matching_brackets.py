def is_paired(input_string):
    """Checks if bracket sequences are properly paired.

    :param input_string: str - sequence of brackets
    :return: bool - is the sequence properly paired?
    """
    brackets = {
        "open_brace": '{',
        "closed_brace": '}',
        "open_parenthesis": '(',
        "closed_parenthesis": ')',
        "open_square": '[',
        "closed_square": ']'
    }
    expected = []
    
    for character in input_string:
        for bracket_name, bracket in brackets.items():

            # If new opening bracket add respective closing bracket to expected list
            if character == bracket and bracket_name.startswith('open'):
                expected.append(brackets[f'closed{bracket_name.removeprefix("open")}'])

            # If closing bracket unexpected, return false
            if character == bracket and bracket_name.startswith('closed'):
                if expected and expected[-1] == bracket:
                    expected.pop()
                else:
                    return False

    # Check for any expected characters
    return len(expected) == 0
   
        
    
   



