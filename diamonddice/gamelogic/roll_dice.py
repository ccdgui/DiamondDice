#import models
from diamonddice.models import Dicehand

#import statements
from random import randint
from collections import Counter


#Defining Dice with 4 attributes rank (1 to 5), status (locked, unlocked and scored) and value (1 to 6 after Dice are rolled)

class Dice:

  def __init__(self,status,value):

    self.status = status
    self.value = value

d1 = Dice('unlocked',1)
d2 = Dice('unlocked',1)
d3 = Dice('unlocked',1)
d4 = Dice('unlocked',1)
d5 = Dice('unlocked',1)


def roll_dice():

    #first_roll = Dicehand.objects.get(pk=1)
    hands = Dicehand.objects.all()

    if hands.exists():
        new_hand = hands.latest('created_at')
        new_hand.pk = None  # When we save, save a new copy
    else:
        new_hand = Dicehand()

    new_hand.roll()
    new_hand.dice_score = new_hand.score()
    new_hand.save()

    return new_hand
