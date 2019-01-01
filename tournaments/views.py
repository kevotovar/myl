from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.utils import count_duplicates, get_current_time_with_tz, get_start_date_and_end_date_from_datetime
from tournaments.models import Tournament, Participant
from user.models import User
from shops.models import Shop


def tournaments_report(request):
    shop_id = request.user.shop.id
    shop = Shop.objects.get(id=shop_id)
    current_time = get_current_time_with_tz()
    (start_time, end_time) = get_start_date_and_end_date_from_datetime(datetime_obj=current_time)
    tournaments_count = shop.tournaments.filter(created__gte=start_time, created__lte=end_time).count()
    context = dict(
        tournaments_count=tournaments_count,
        shop=shop,
    )
    return render(request, 'tournaments/report.html', context=context)


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
