from rest_framework import serializers
from diamonddice.models import Dicehand, Dice


class DiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dice
        fields = '__all__'

class DicehandSerializer(serializers.ModelSerializer):
    dice = DiceSerializer(many=True, read_only=True)

    class Meta:
        model = Dicehand
        fields = ('dice_score', 'display_message', 'dice')

