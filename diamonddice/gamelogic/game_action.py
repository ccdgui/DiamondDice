#import models
from diamonddice.models import Dice, Coin
from diamonddice.gamelogic.display_message import display_message
from diamonddice.gamelogic.play_token import play_token, roll_token

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
    existing_coins = []
    hands = Dice.objects.all()

    if hands.exists():
        new_hand = hands.latest('created_at')
        unlocked_dice = new_hand.dice.filter(die_status="unlocked")

        if new_hand.dice_score == 0 and new_hand.previous_roll_saved != "yes":
            new_hand.token -= 1
            reset_dice()
            new_hand.save()

        if new_hand.previous_roll_saved == "yes":
            new_hand.token -= 1

        if not unlocked_dice.exists():
            reset_dice()
            new_hand.save()

        existing_dice = list(new_hand.dice.all())
        existing_coins = list(new_hand.coin.all())
        new_hand.pk = None

    else:
        new_hand = Dice()

    new_hand.save()
    new_hand.roll(existing_dice, existing_coins)
    new_hand.score()
    new_hand.previous_roll_saved = "no"
    new_hand.save()

    unlocked_dice = new_hand.dice.filter(die_status="unlocked")
    if not unlocked_dice.exists():
        new_hand.alldice_locked = "Yes"

    display_message(new_hand)
    roll_token(new_hand)
    new_hand.save()

    return new_hand

def save_dice():

    hands = Dice.objects.all()

    current_hand = hands.latest('created_at')
    this_round_score = current_hand.round_score

    Coin.objects.create(wallet=current_hand, coin_value=this_round_score)

    all_coins = current_hand.coin.all()

    if all_coins.count() == 5:
        # Take value of coins and do something
        all_coins.delete()


    play_token(current_hand)
    reset_dice()
    current_hand.player_score += this_round_score
    current_hand.round_score = 0
    current_hand.dice_score = 0
    current_hand.previous_roll_saved = "yes"
    current_hand.save()

    return current_hand

