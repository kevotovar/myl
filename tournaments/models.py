from django.db import models

from core.models import TimeStampedModel
from shops.models import Shop
from user.models import User

# Create your models here.
class Tournament(TimeStampedModel):
    BASIC = 1
    ADVANCED = 2
    PREMIERE = 3
    TOURNAMENT_LEVELS = (
        (BASIC, 'Basic'),
        (ADVANCED, 'Advanced'),
        (PREMIERE, 'Premiere')
    )
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='tournaments')
    level = models.IntegerField(choices=TOURNAMENT_LEVELS, default=BASIC)
    participants = models.ManyToManyField(User, through='Participant')

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_tournaments')
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT, related_name='tournament_participants')
    place = models.PositiveIntegerField()
