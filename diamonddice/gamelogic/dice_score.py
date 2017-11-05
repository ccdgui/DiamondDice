    dice_counter = []
    score = 0

    for Dice in all_dice:
      if Dice.status == 'unlocked':
        dice_counter.append(Dice)


    dice_hand = Counter([Dice.value for Dice in dice_counter])
    dice_scored = []

 #Looks at the value frequency in the dice hand.
    for value, freq in dice_hand.items():

        if freq == 2:             #Checks for Full House
          for value, freq in dice_hand.items():
            if freq == 3:
              score += 700
              [dice_scored.append(Dice) for Dice in dice_counter]
              hand_type = "Full House"
              #Player1.dice_hand.hand_name = 'Full House'

        if Dice.status == 'unlocked':

          if freq == 3: #Checks for '111'special case of 3 of a kind
            if value == 1:
              score += 300
              [dice_scored.append(Dice) for Dice in dice_counter if Dice.value == [value for value, freq in dice_hand.items() if freq == 3][0]]
              hand_type = "Three of a kind"
              #Player1.dice_hand.hand_name = 'Three of a kind'

            else:
              score += (value * 100)       #Checks for 3 of a kind
              [dice_scored.append(Dice) for Dice in dice_counter if Dice.value == [value for value, freq in dice_hand.items() if freq == 3][0]]
              hand_type = "Three of a kind"
              #Player1.dice_hand.hand_name = 'Three of a kind'

          if freq == 4:               #Checks for 4 of a kind
            score += (value * 1000)
            [dice_scored.append(Dice) for Dice in dice_counter if Dice.value == [value for value, freq in dice_hand.items() if freq == 4][0]]
            hand_type = "Four of a kind"
            #Player1.dice_hand.hand_name = 'Four of a kind'

          if freq == 5:               #Checks for 5 of a kind
            score += (10000)
            [dice_scored.append(Dice) for Dice in dice_counter if Dice.value == [value for value, freq in dice_hand.items() if freq == 5][0]]

            hand_type = "Five of a kind"
            #Player1.dice_hand.hand_name = 'Five of a kind'


      #Checks for straight (sum of unique values in the Dice hand)
    straight_check = sum(set([Dice.value for Dice in dice_counter]))
    if len(set([Dice.value for Dice in dice_counter])) == 5:
        if straight_check == 20 or straight_check == 15:
          score += (2000)
          [dice_scored.append(Dice) for Dice in dice_counter]
          hand_type = "Straight"


      #Changes status to 'scored'
    for Dice in dice_scored:
        Dice.status = 'scored'

    for Dice in dice_counter:

        if Dice.status == 'unlocked':

          if Dice.value == 1:
            score += 100
            Dice.status = 'scored'
            #Player1.dice_hand.hand_name = "Single Dice scored"

          if Dice.value == 5:
            score += 50
            Dice.status = 'scored'
            #Player1.dice_hand.hand_name = "Single Dice scored"

