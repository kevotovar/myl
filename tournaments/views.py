from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.utils import count_duplicates
from tournaments.models import Tournament, Participant
from user.models import User


def tournaments_report(request):
    store = request.user.shop
    return render(request, 'tournaments/report.html')


@api_view(['POST'])
def tournament_report_post(request):
    data = dict(request.data)
    if data:
        data.pop('csrfmiddlewaretoken')
        data_items = data.items()
        if len(data_items) < 4:
            return Response(
                {'error': 'No se pueden reportar torneos con menos de 4 jugadores'},
                status=status.HTTP_400_BAD_REQUEST
            )
        places = [None] * len(data_items)
        for key, value in data_items:
            places[int(key)-1] = value[0]
        duplicates = count_duplicates(places)
        if duplicates:
            return Response(
                {'error': "Existen ID's duplicados"},
                status=status.HTTP_400_BAD_REQUEST
            )
        shop = request.user.shop
        users = User.objects.filter(ranking_id__in=places).all()
        if users.count() != len(places):
            not_found_ids = len(places) - users.count()
            return Response(
                {'error': "Verifica los ID's no se encontraron {}".format(not_found_ids)},
                status=status.HTTP_400_BAD_REQUEST
            )
        tournament = Tournament.objects.create(shop=shop)
        participants = []
        for user in users:
            place = places.index(user.ranking_id) + 1
            participants.append(Participant(
                tournament=tournament,
                place=place,
                user=user,
            ))
            if place in [1, 2, 3]:
                user.points = user.points + abs(place - 4)
                user.save()
        Participant.objects.bulk_create(participants)
        return Response(
            {'success': 'Torneo reportado'},
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {'error': 'Recarga la pagina o intenta de nuevo'},
            status=status.HTTP_400_BAD_REQUEST
        )
