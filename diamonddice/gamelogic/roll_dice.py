#import models
from diamonddice.models import Dicehand

def roll_dice():

    hands = Dicehand.objects.all()

    if hands.exists():
        new_hand = hands.latest('created_at')
        new_hand.pk = None  # When we save, save a new copy
    else:
        new_hand = Dicehand()

    new_hand.save()
    new_hand.roll()


    return new_hand
