#diamonddice game logic
from diamonddice.gamelogic.game_action import roll_dice

#django import statements
from .models import Dice
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import DiceSerializer


class DiamondView(TemplateView):
    template_name='index.html'

class RollView(APIView):

    def get(self, request, format=None):

        new_hand = roll_dice()

        serializer = DiceSerializer(new_hand)

        return Response(serializer.data)

class SaveView(APIView):

    def delete(self, request, format=None):

        Dice.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
