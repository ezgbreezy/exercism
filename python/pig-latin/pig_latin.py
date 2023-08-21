"""
My first solution to the Pig Latin Exercism problem in Python
"""

def translate(text):
    """
    Translates english to pig latin.

    :param text: str - english to be translated
    :return: str - translated pig-latin
    """

    # Define sounds
    vowels = ['a', 'e', 'i', 'o', 'u']  

    # Define pig-latin suffix
    suffix = "ay"

    # Convert text str to list and set index
    text = text.split()
    index = -1

    # Loop through words in text
    for word in text:
        
        # Increment index
        index += 1

        # Reset cluster and 'y' vowel status
        cluster = ""
        if vowels.count('y') > 0:
                vowels.remove('y')

        # Loop through letters in word
        for letter in word:
            if len(cluster) == 1:
                vowels.append('y')
            if letter in vowels:
                # 'qu' edge case handling
                if letter == 'u' and cluster.endswith('q'):
                    cluster += letter
                    text[index] = word.removeprefix(cluster) + cluster + suffix
                    break
                # 'yt' edge case handling
                elif letter == 't' and cluster.endswith('y'):
                    cluster = ""
                    text[index] = word + suffix
                    break
                else:
                    text[index] = word.removeprefix(cluster) + cluster + suffix
                    break
            else:
                # 'xr' edge case handling
                if (letter == 'r' and cluster.endswith('x')):
                    cluster = ""
                    text[index] = word + suffix
                    break
                # 'yt' edge case handling
                elif letter == 't' and cluster.endswith('y'):
                    cluster = ""
                    text[index] = word + suffix
                    break
                cluster += letter
    
    return ' '.join(text)
