def display_message(new_hand):

    if new_hand.dice_score == 0:
        new_hand.display_message = "Sorry, you scored 0. Press Roll to continue."
        new_hand.save()

    if new_hand.alldice_locked == "Yes":
        new_hand.display_message = "Five dice score, you must roll again!"
        new_hand.save()

    if new_hand.dice_score>0:
        new_hand.display_message = "Press Roll to continue."
        new_hand.save()