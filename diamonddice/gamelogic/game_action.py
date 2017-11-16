#import models
from diamonddice.models import Dice
from diamonddice.gamelogic.display_message import display_message

def roll_dice():

    existing_dice = []
    hands = Dice.objects.all()
    new_hand = hands.latest('created_at')
    unlocked_dice = new_hand.dice.filter(die_status="unlocked")

    def reset_dice():

        reset_dice = new_hand.dice.all()

        for die in reset_dice:
            die.die_status = "unlocked"
            die.save()

    if hands.exists():

        if new_hand.dice_score == 0:
                reset_dice()
                new_hand.save()

        else:
                new_hand.alldice_locked = "No"

        existing_dice = list(new_hand.dice.all())
        new_hand.pk = None

    else:
        new_hand = Dice()

    new_hand.save()
    new_hand.roll(existing_dice)
    new_hand.score()

    if not unlocked_dice.exists():
        new_hand.alldice_locked = "Yes"
        reset_dice()
        new_hand.save()

    display_message(new_hand)
    new_hand.save()

    return new_hand






