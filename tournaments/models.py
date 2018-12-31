from django.db import models

from core.models import TimeStampedModel
from shops.models import Shop
from user.models import User


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

    def __str__(self):
        return '{} - {}'.format(self.id, self.shop.name)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tournaments')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_participants')
    place = models.PositiveIntegerField()
