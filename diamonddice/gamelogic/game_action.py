#import models
from diamonddice.models import Dice

def roll_dice():

    existing_dice = []
    hands = Dice.objects.all()

    def reset_dice():

        reset_dice = new_hand.dice.all()

        for die in reset_dice:
            die.die_status = "unlocked"
            die.save()

    if hands.exists():

        new_hand = hands.latest('created_at')
        unlocked_dice = new_hand.dice.filter(die_status="unlocked")

        if new_hand.dice_score == 0:
                new_hand.round_score = 0
                reset_dice()
                new_hand.save()

        if not unlocked_dice.exists():
                reset_dice()
                new_hand.save()

        existing_dice = list(new_hand.dice.all())
        new_hand.pk = None

    else:
        new_hand = Dice()

    new_hand.save()
    new_hand.roll(existing_dice)
    new_hand.score()
    new_hand.save()

    return new_hand






