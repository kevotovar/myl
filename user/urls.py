from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking', views.ranking_view, name='ranking'),
    path('ranking/data', views.RankingListJson.as_view(), name='ranking-data'),
]
