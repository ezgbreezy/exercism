def is_isogram(string):
    """
    Determines whether or not a word is an isogram.

    An isogram is a word that does not contain repeating letters.

    :param string: str - word to be checked if isogram
    :return: bool - is the word an isogram?
    """

    for letter in string.lower():
        if letter.isalpha() and string.lower().count(letter) > 1:
            return False
    return True