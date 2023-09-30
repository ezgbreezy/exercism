def rotate(text: str, key: str) -> str:
    """
    Implements a Caesar Cipher on given text, 
    thereby rotating the letter *key* times.

    :param text: str - text to be ciphered
    :param key: int - rotation factor
    :return: str - rotated text
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    key_map = letters[key:] + letters[:key]
    
    return text.translate(text.maketrans(letters + letters.upper(), key_map + key_map.upper()))
