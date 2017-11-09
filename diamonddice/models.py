from django.db import models
from random import randint

class Dicehand(models.Model):
    dice_score = models.IntegerField(default = 0)
    display_message = models.CharField(max_length=140, default="It worked!")
    created_at = models.DateTimeField(auto_now_add=True)

    def roll(self):

        dice = self.dice.all()
        if dice.exists():  # Assuming that if any dice exist, there are 5
            for die in dice:
                if die.dice_status == "unlocked":
                    die.dice_value = randint(1,6)
                    die.save()
        else:
            for i in range(5):
                Dice.objects.create(dicehand=self, dice_value=randint(1,6))

    def score(self):
        score = 100
        self.dice_score = score

    def save(self, *args, **kwargs):
        self.score()
        super(Dicehand, self).save(*args, **kwargs)


class Dice(models.Model):
    dice_value = models.IntegerField(default = 0)
    dice_status = models.CharField(max_length=30, default="unlocked")
    created_at = models.DateTimeField(auto_now_add=True)
    dicehand = models.ForeignKey(Dicehand, related_name='dice', on_delete=models.CASCADE)














