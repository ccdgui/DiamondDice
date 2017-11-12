#import models
from diamonddice.models import Dice, Die

def roll_dice():

    hands = Dice.objects.all()
    existing_dice = []

    if hands.exists():
        new_hand = hands.latest('created_at')
        existing_dice = list(new_hand.dice.all())
        new_hand.pk = None
    else:
        new_hand = Dice()

    new_hand.save()
    new_hand.roll_score(existing_dice)
    new_hand.save()

    return new_hand

