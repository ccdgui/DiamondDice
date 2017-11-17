from rest_framework import serializers
from diamonddice.models import Dice, Die


class DieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Die
        fields = '__all__'

class DiceSerializer(serializers.ModelSerializer):
    dice = DieSerializer(many=True, read_only=True)

    class Meta:
        model = Dice
        fields = ('dice_score', 'round_score', 'player_score', 'token', 'hand_name', 'display_message', 'dice')

class SaveSerializer(serializers.ModelSerializer):
    dice = DieSerializer(many=True, read_only=True)

    class Meta:
        model = Dice
        fields = ('dice_score', 'round_score', 'player_score', 'token', 'hand_name', 'display_message', 'dice')