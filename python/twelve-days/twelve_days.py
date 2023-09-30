def recite(start_verse, end_verse):

    day = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh", 
        "twelfth"
    ]

    verses = (
        f"On the {day[end_verse - 1]} day of Christmas my true love gave to me: ",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
        "a Partridge in a Pear Tree."
    )

    recital = []

    for line in range(end_verse, start_verse - 1, - 1):
        recital.append(verses[:line])
    
    return recital