"""House exercise based on @enahelds solution using 
the .join string method and list comprehension. """

from typing import List
TEXT = """the horse and the hound and the horn that belonged to 
the farmer sowing his corn that kept 
the rooster that crowed in the morn that woke 
the priest all shaven and shorn that married 
the man all tattered and torn that kissed 
the maiden all forlorn that milked 
the cow with the crumpled horn that tossed 
the dog that worried 
the cat that killed 
the rat that ate 
the malt that lay in 

""".splitlines()

def recite(start_verse: int, end_verse: int) -> List[str]:
    return [f"This is {''.join(TEXT[-n:])}the house that Jack built."
            for n in range(start_verse, end_verse + 1)]