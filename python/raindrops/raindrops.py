def convert(number):
    """
    Converts number to raindrop sound based on its factors.

    If it has 
        3 as a factor the sound is 'Pling'.
        5 as a factor the sound is 'Plang'.
        7 as a factor the sound is 'Plong'.

    :param number: int or float - the number to be converted
    :return: str - the sound the number converted too
    """

    sound = ""

    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    if sound == "":
        sound = str(number)

    return sound