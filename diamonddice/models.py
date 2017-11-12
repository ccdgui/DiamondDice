from django.db import models
from random import randint
from django.db.models import Count

class Dice(models.Model):
    dice_score = models.IntegerField(default = 0)
    hand_name = models.CharField(max_length=140, default="No Hand")
    display_message = models.CharField(max_length=140, default="Let's roll!")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.dice_score, self.hand_name, self.display_message)


    class Meta:
        ordering = ('created_at',)

    def roll_score(self, existing_dice):

        if len(existing_dice) > 0:  # Assuming that if any dice exist, there are 5

            for die in existing_dice:

                new_die = Die(hand=self, die_value=die.die_value, die_status=die.die_status)

                if new_die.die_status == "unlocked":
                    new_die.die_value = randint(1,6)

                new_die.save()

        else:

            for i in range(5):
                Die.objects.create(hand=self, die_value=randint(1,6))



        score = self.dice_score

        unlocked_dice = self.dice.filter(die_status="unlocked")

        dice_count = unlocked_dice.values('die_value').order_by('die_value').annotate(Count('die_value')).order_by('die_value__count')

        scored_values = []
        for dice_scored in dice_count:
            if dice_scored['die_value__count'] == 2:
                scored_values.append(dice_scored['die_value'])
                score += dice_scored['die_value'] * 10000

            if dice_scored['die_value__count'] == 3:
                scored_values.append(dice_scored['die_value'])
                score += dice_scored['die_value'] * 10000

        unlocked_dice.filter(die_value__in=scored_values).update(die_status='scored')

        self.dice_score = score


class Die(models.Model):
    die_value = models.IntegerField(default = 0)
    die_status = models.CharField(max_length=30, default="unlocked")
    created_at = models.DateTimeField(auto_now_add=True)
    hand = models.ForeignKey(Dice, related_name='dice')


    def __str__(self):
        return '%s %s' % (self.die_value, self.die_status)

    class Meta:
        ordering = ('created_at',)



#if 0 die is unlocked, player has to roll again
#if die has scored its status becomes 'scored', if player decides to roll again die status changed from 'score' to 'locked'

