from django.urls import path

from . import views
from .views import logar_usuario, cadastrar_usuario, deslogar_usuario, prontuario

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', logar_usuario, name="logar_usuario"),
    path('cadastro/', cadastrar_usuario, name="cadastrar_usuario"),
    path('logout/', deslogar_usuario, name="deslogar_usuario"),

    path('prontuario/<int:id_paciente>/', prontuario, name="prontuario"),
]
