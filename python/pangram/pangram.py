def is_pangram(sentence):
    """
    Tests whether a sentence is a pangram. 

    A pangram is a phrase containing all 26 letters of the alphabet.

    :param sentence: str - the sentence to be tested
    :return: bool - is the sentence a pangram? 
    """

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alpha:
        if (letter not in sentence
            and letter.upper() not in sentence):
            print(letter)
            return False
    
    return True    
