from rest_framework import serializers
from diamonddice.models import Dice, Die, Coin

class DieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Die
        fields = '__all__'

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'


class DiceSerializer(serializers.ModelSerializer):
    dice = DieSerializer(many=True, read_only=True)
    coin = CoinSerializer(many=True, read_only=True)

    class Meta:
        model = Dice
        fields = ('dice_score', 'round_score', 'player_score', 'token', 'roll_token', 'hand_name', 'display_message', 'dice', 'coin')


