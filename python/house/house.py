def recite(start_verse: str, end_verse: str) -> list:
    """Recites specified verses nursery rhyme "The House That Jack Built".

    :param start_verse: int - first verse number to recite
    :param end_verse: int - last verse number to recite
    :return: list - recited verses
    """
    # Structure verses into list of associated verbs and nouns
    verses = [
        ["", "the horse and the hound and the horn"],
        ["belonged to", "the farmer sowing his corn"],
        ["kept", "the rooster that crowed in the morn"],
        ["woke", "the priest all shaven and shorn"],
        ["married", "the man all tattered and torn"],
        ["kissed", "the maiden all forlorn"],
        ["milked", "the cow with the crumpled horn"],
        ["tossed", "the dog"],
        ["worried", "the cat"],
        ["killed", "the rat"],
        ["ate", "the malt"],
        ["lay in", "the house that Jack built."]
    ]
    verses.reverse()
    
    line = ''
    recital = []

    # Iterate through number of verses to recite
    for repeat in range(end_verse - 1, start_verse - 2, -1):
        # Iterate through lines in verse
        for count, [verb, subject] in zip(range(repeat + 1), verses):
                if count == repeat:
                    line = f'This is {subject}{line}'
                    recital.append(line)
                elif line:
                    line = f' that {verb} {subject}{line}'
                else:
                    line = f' that {verb} {subject}'
        # Reset line each verse
        line = ''
    # Loop appends the order backwards, reverse before returning
    recital.reverse()

    return recital
