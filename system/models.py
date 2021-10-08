from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class RoleModel(models.Model):
    COACH = 'C'
    PLAYER = 'P'
    ADMIN = 'A'

    ROLE_TYPES = [
        (COACH, 'Coach'),
        (PLAYER, 'Player'),
        (ADMIN, 'Admin'),
    ]
    type = models.CharField(
        max_length=2,
        choices=ROLE_TYPES,
        default=PLAYER,
        verbose_name='type of role'
    )

    def __str__(self):
        return str(self.type)
        # return 'Type : %s, Id : %s' % (self.type, self.id)

    def get_id(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('role_detail', args=[str(self.id)])


class UserRoleModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
       

    def get_absolute_url(self):
        return reverse('user_role', args=[str(self.id)])


class UserStatModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_time = models.DateTimeField(verbose_name='login date time', default=timezone.now)
    logout_time = models.DateTimeField(verbose_name='logout date time')

    def __str__(self):
        return str(self.login_time)

    def get_absolute_url(self):
        return reverse('user_stat_detail', args=[str(self.id)])


class TeamModel(models.Model):
    name = models.TextField(max_length=100)
    abbr = models.TextField(max_length=3)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('team', args=[str(self.id)])


class GameModel(models.Model):
    QF = 'QF'
    SF = 'SF'
    FI = 'FI'
    WI = 'WI'

    ROUNDS = [
        (QF, 'Quarter Final'),
        (SF, 'Semi Final'),
        (FI, 'Final'),
        (WI, 'Winner')
    ]

    compet_team01 = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='host')
    compet_team02 = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='guest')
    compet1_score = models.IntegerField()
    compet2_score = models.IntegerField()
    winner = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='winner')
    date = models.DateField(verbose_name='game date')
    round_number = models.CharField(
        max_length=2,
        choices=ROUNDS,
        default=QF,
        verbose_name='round type'
    )

    def __str__(self):
        return 'Game # %s' % (self.id)

    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])


class TeamStatModel(models.Model):
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='team')
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE, related_name='game')
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('team_stat', args=[str(self.id)])


class CoachModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)

    def __str__(self):
        return 'Name : %s %s' % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('coach', args=[str(self.id)])


class PlayerModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    height = models.IntegerField()

    def __str__(self):
        return 'Name : %s , Height : %s' % (self.user.first_name, self.height)

    def get_absolute_url(self):
        return reverse('player', args=[str(self.id)])


class PlayerStatModel(models.Model):
    player = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('player_stat', args=[str(self.id)])



