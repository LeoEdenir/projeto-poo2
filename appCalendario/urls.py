from django.urls import path

from . import views

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamento/<int:agendamento_id>/', views.pegar_agendamento, name='agendamento'),
]
