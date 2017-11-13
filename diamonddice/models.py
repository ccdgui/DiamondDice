from django.db import models
from random import randint
from django.db.models import Count

class Dice(models.Model):
    dice_score = models.IntegerField(default = 0)
    round_score = models.IntegerField(default = 0)
    hand_name = models.CharField(max_length=140, default="No Hand")
    display_message = models.CharField(max_length=140, default="Let's roll!")
    token = models.IntegerField(default = 3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.dice_score, self.hand_name, self.display_message)


    class Meta:
        ordering = ('created_at',)

    def roll(self, existing_dice):

        if len(existing_dice) > 0:
            for die in existing_dice:
                new_die = Die(hand=self, die_value=die.die_value, die_status=die.die_status)
                if new_die.die_status == "unlocked":
                    new_die.die_value = randint(1,6)
                new_die.save()
        else:
            for i in range(5):
                Die.objects.create(hand=self, die_value=randint(1,6))


    def score(self):

        this_dice_score = 0
        this_round_score = self.round_score
        self.hand_name = ''

        unlocked_dice = self.dice.filter(die_status="unlocked")
        dice_count = unlocked_dice.values('die_value').order_by('die_value').annotate(Count('die_value')).order_by('die_value__count')

        #check for full house
        if len(dice_count) == 2 and dice_count[0]['die_value__count'] == 2 and dice_count[1]['die_value__count'] == 3:
            this_dice_score += 2000
            scored_values = [dice_scored['die_value'] for dice_scored in dice_count]
            self.hand_name = 'Full House'

        #check for straight
        elif len(dice_count) == 5 and sum([dice_scored['die_value'] for dice_scored in dice_count]) == 20 or sum([dice_scored['die_value'] for dice_scored in dice_count]) == 15:
            scored_values = [dice_scored['die_value'] for dice_scored in dice_count]
            self.hand_name = 'Straight'
            this_dice_score += 2000

        else:

            scored_values = []
            for dice_scored in dice_count:

                    #check for three of a kind
                    if dice_scored['die_value__count'] == 3:
                        scored_values.append(dice_scored['die_value'])
                        this_dice_score += dice_scored['die_value'] * 100
                        self.hand_name = 'Three of a kind'

                    #check for four of a kind
                    if dice_scored['die_value__count'] == 4:
                        scored_values.append(dice_scored['die_value'])
                        this_dice_score += dice_scored['die_value'] * 1000
                        self.hand_name = 'Four of a kind'

                    #check for five of a kind
                    if dice_scored['die_value__count'] == 5:
                        scored_values.append(dice_scored['die_value'])
                        this_dice_score += dice_scored['die_value'] * 10000
                        self.hand_name = 'Five of a kind'

                    #check single dice with value 1 or 5
                    if dice_scored['die_value__count'] == 1:
                        if dice_scored['die_value'] == 1:
                            scored_values.append(dice_scored['die_value'])
                            this_dice_score += 100

                        elif dice_scored['die_value'] == 5:
                            this_dice_score += 150
                            scored_values.append(dice_scored['die_value'])

        unlocked_dice.filter(die_value__in=scored_values).update(die_status='scored')

        this_round_score += this_dice_score
        self.dice_score = this_dice_score
        self.round_score = this_round_score



class Die(models.Model):
    die_value = models.IntegerField(default = 0)
    die_status = models.CharField(max_length=30, default="unlocked")
    created_at = models.DateTimeField(auto_now_add=True)
    hand = models.ForeignKey(Dice, related_name='dice')


    def __str__(self):
        return '%s %s' % (self.die_value, self.die_status)

    class Meta:
        ordering = ('created_at',)

