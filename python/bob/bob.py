def response(hey_bob):
    """
    Responds to textual input in the style of Bob.

    :param hey_bob: str - text for Bob to respond too. 
    :return: str - one of ("Sure.", 
    "Whoa, chill out!", 
    "Calm down, I know what I'm doing!", 
    "Fine. Be that way!",
    "Whatever.")
    """
    
    # Establish response constants
    QUESTION_RESPONSE = "Sure."
    YELL_RESPONSE = "Whoa, chill out!"
    YELL_QUESTION_RESPONSE = "Calm down, I know what I'm doing!"
    SILENCE_RESPONSE = "Fine. Be that way!"
    DEFAULT_RESPONSE = "Whatever."

    # Check if valid str, return default otherwise
    if type(hey_bob) != type('str'):
        return DEFAULT_RESPONSE
    
    # Yelling question response
    if (bool(hey_bob.strip().endswith('?'))
        and bool(hey_bob.isupper())):
        return YELL_QUESTION_RESPONSE
    
    # Question response
    if bool(hey_bob.strip().endswith('?')):
        return QUESTION_RESPONSE
    
    # Yelling response
    if bool(hey_bob.isupper()):
        return YELL_RESPONSE
    
    # Silence response
    if (bool(hey_bob.isspace())
        or bool(hey_bob == "")):
        return SILENCE_RESPONSE
    
    # Default response
    return DEFAULT_RESPONSE
