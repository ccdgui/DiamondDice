#import models
from diamonddice.models import Dice
from diamonddice.gamelogic.display_message import display_message
from diamonddice.gamelogic.play_token import play_token

def reset_dice():
    hands = Dice.objects.all()
    new_hand = hands.latest('created_at')
    reset_dice = new_hand.dice.all()

    for die in reset_dice:
        die.die_status = "unlocked"
        die.die_value = 0
        die.save()

def roll_dice():

    existing_dice = []
    hands = Dice.objects.all()

    if hands.exists():

        new_hand = hands.latest('created_at')
        unlocked_dice = new_hand.dice.filter(die_status="unlocked")

        if new_hand.dice_score == 0:
                new_hand.token -= 1
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

    unlocked_dice = new_hand.dice.filter(die_status="unlocked")
    if not unlocked_dice.exists():
        new_hand.alldice_locked = "Yes"

    display_message(new_hand)
    new_hand.save()

    return new_hand

def save_dice():

    hands = Dice.objects.all()
    current_hand = hands.latest('created_at')
    this_round_score = current_hand.round_score
    play_token(current_hand)
    reset_dice()
    current_hand.player_score += this_round_score
    current_hand.round_score = 0
    current_hand.dice_score = 0
    current_hand.save()

    return current_hand

