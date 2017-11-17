def play_token(current_hand):

    score = current_hand.round_score
    token = -1

    step_one = 200
    step_two = 500
    step_three = 1000
    step_four = 1500
    step_five = 2000
    step_six = 2500

    range1 = range(step_one,step_two)
    range2 = range(step_two,step_three)
    range3 = range(step_three,step_four)
    range4 = range(step_four,step_five)
    range5 = range(step_five,step_six)

    if score in range1:
      token += 1

    elif score in range2:
      token += 2

    elif score in range3:
      token += 3

    elif score in range4:
      token += 4

    elif score in range5:
      token += 5

    current_hand.token += token