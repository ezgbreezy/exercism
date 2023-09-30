"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    
    # Check for equality
    if list_one == list_two:
        return EQUAL

    # Check if list_one sublist of list_two 
    if is_sublist(list_one, list_two) is True:
        return SUBLIST
        
    # Check if list_two sublist of list_one
    if is_sublist(list_two, list_one) is True:
        return SUPERLIST
    
    return UNEQUAL

def is_sublist(sublist: list, superlist: list) -> int:
    """ Checks if one list is a sublist of another.

    :param sublist: list - the expected sublist
    :param superlist: list - the expected superlist
    :return: bool - is 'sublist' a sublist of 'superlist'?
    """
    sublist_hash = hash(tuple(sublist))
    for index, item in enumerate(superlist):
        superlist_hash = hash(tuple(superlist[index:index + len(sublist)]))
        if sublist_hash == superlist_hash:
            return True
    return False