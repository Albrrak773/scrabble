from ps3 import calculate_handlen
from ps3 import is_valid_word
from ps3 import get_word_score
from ps3 import update_hand
from ps3 import deal_hand
from ps3 import load_words
from ps3 import display_hand
handListed = [] # make the hand look in prestable way
handString = ""
hand = deal_hand(7)

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    hand_listed = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand_listed.append(letter)       # print all on the same line
    hand_string = " ".join(hand_listed)
    return   hand_string                        # print an empty line

print(display_hand(hand))