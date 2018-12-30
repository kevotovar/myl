from django.urls import path
from . import views

urlpatterns = [
    path('report', views.tournaments_report, name='report'),
    path('report/send', views.tournament_report_post, name='report-send'),
]
