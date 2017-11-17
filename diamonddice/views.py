#diamonddice game logic
from diamonddice.gamelogic.game_action import roll_dice, save_dice

#django import statements
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

    def get(self, request, format=None):

        current_hand = save_dice()

        serializer = DiceSerializer(current_hand)

        return Response(serializer.data)
