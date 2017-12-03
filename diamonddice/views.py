#diamonddice game logic
from diamonddice.gamelogic.game_action import roll_dice, save_dice

#django import statements
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import DiceSerializer
from django.http import JsonResponse

def scores(request):
#    if "scores" not in request.session:
 #       request.session.scores = []
    return JsonResponse(dict(scores=request.session["scores"]))

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

        if 'scores' not in request.session:
            request.session["scores"] = []

        request.session["scores"].append(current_hand.player_score)
        request.session.modified = True

        serializer = DiceSerializer(current_hand)

        return Response(serializer.data)
