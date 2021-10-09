from rest_framework.response import Response
from rest_framework.serializers import Serializer
from system.models import GameModel, PlayerModel, PlayerStatModel, TeamModel, TeamStatModel, UserRoleModel
from system.serializers import GameSerializer, TeamSerializer
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .serializers import GameSerializer, UserRoleSerializer
from django.db.models import Avg, Sum, Count




class HomeView(APIView):   
    def get(self, request):
        games = GameModel.objects.all()
        Serializer = GameSerializer(games)
        return Response(games['host'])  

# class LoginView(APIView):
    
#     def put(self,request):
#         user_role = UserRoleModel.objects.get(user_id=request.user.id)
#         user_role.is_logged_in = True

#         Serializer = UserRoleSerializer(user_role)
#         Serializer.save()

class PlayerView(APIView):
    def get(self, request, player_id=None):
        player = PlayerModel.objects.filter(id=player_id).first()
        stat = PlayerStatModel.objects.filter(player_id=player_id)

        context = {
        'player': player,
        'player_id': player.id,
        'team': player.team.name,
        'games': len(stat),
        'average_score': PlayerStatModel.objects.filter(player_id=player_id).aggregate(Avg('score'))
            }
        return Response(context)

class TeamView(APIView):
    def get(request, team_id=None):
        user_role = UserRoleModel.objects.get(user_id=request.user.id)
    if UserRoleModel.role.type != 'P':

        players = PlayerModel.objects.filter(team_id=team_id)
        context = {
            'players': players,
            'average_score': TeamStatModel.objects.filter(team_id=team_id).aggregate(Avg('score')),
        }

