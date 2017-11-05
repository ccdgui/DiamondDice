#diamonddice game logic
from diamonddice.gamelogic.roll_dice import roll_dice

from random import randint

#django import statements
from .models import Dicehand
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import DicehandSerializer, SavehandSerializer

#defining class object Dice



#Django class based Views
class DiamondView(TemplateView):
    template_name='index.html'

class RollView(APIView):

    def get(self, request, format=None):

        new_hand = roll_dice()

        serializer = DicehandSerializer(new_hand)

        return Response(serializer.data)

class SaveView(APIView):

    def delete(self, request, format=None):

        Dicehand.objects.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
