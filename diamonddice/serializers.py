from rest_framework import serializers
from diamonddice.models import Dicehand

class DicehandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicehand
        fields = '__all__'

class SavehandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicehand
        fields = 'display_message'