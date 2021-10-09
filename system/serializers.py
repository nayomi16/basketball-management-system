# serializers.py
from rest_framework import serializers

from .models import CoachModel, GameModel, PlayerModel, PlayerStatModel, RoleModel, TeamModel, TeamStatModel, UserRoleModel, UserStatModel


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleModel
        fields = ('type')

class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRoleModel
        fields = ('user', 'role', 'is_logged_in')

class UserStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserStatModel
        fields = ('user','login_time', 'logout_time')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = ('name', 'abbr')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameModel
        fields = ('host', 'guest', 'compet1_score', 'compet2_score', 'winner', 'date', 'round_number')

class TeamStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamStatModel
        fields = ('team', 'game', 'score')

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoachModel
        fields = ('user', 'team')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerModel
        fields = ('user', 'team', 'height')

class PlayerStaterializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerStatModel
        fields = ('player', 'game', 'score')



