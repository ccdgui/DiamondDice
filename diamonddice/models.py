from django.db import models
from random import randint



class Dicehand(models.Model):
    dice_score = models.IntegerField(default = 0)
    dice_value1 = models.IntegerField(default = 0)
    dice_status1 = models.CharField(max_length=30, default="unlocked")
    dice_value2 = models.IntegerField(default = 0)
    dice_status2 = models.CharField(max_length=30, default="unlocked")
    dice_value3 = models.IntegerField(default = 0)
    dice_status3 = models.CharField(max_length=30, default="unlocked")
    dice_value4 = models.IntegerField(default = 0)
    dice_status4 = models.CharField(max_length=30, default="unlocked")
    dice_value5 = models.IntegerField(default = 0)
    dice_status5 = models.CharField(max_length=30, default="unlocked")
    display_message = models.CharField(max_length=140, default="It worked!")
    created_at = models.DateTimeField(auto_now_add=True)

    def roll(self):
        if self.dice_status1 == 'unlocked':
            self.dice_value1 = randint(1,6)
        if self.dice_status2 == 'unlocked':
            self.dice_value2 = randint(1,6)
        if self.dice_status3 == 'unlocked':
            self.dice_value3 = randint(1,6)
        if self.dice_status4 == 'unlocked':
            self.dice_value4 = randint(1,6)
        if self.dice_status5 == 'unlocked':
            self.dice_value5 = randint(1,6)

    def _score_die(self, value):
        score = 0
        if value == 1:
            score = 100
        elif value == 5:
            score = 50
        return score

    def score(self):
        score = 0
        score += self._score_die(self.dice_value1)
        score += self._score_die(self.dice_value2)
        score += self._score_die(self.dice_value3)
        score += self._score_die(self.dice_value4)
        score += self._score_die(self.dice_value5)
        self.dice_score = score

    def save(self, *args, **kwargs):
        self.score()
        super(Dicehand, self).save(*args, **kwargs)
