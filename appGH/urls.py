from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logar_usuario, name="logar_usuario"),
    path('cadastro/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('logout/', views.deslogar_usuario, name="deslogar_usuario"),

    path('pacientes/', views.pacientes, name="pacientes"),
    path('pacientes/<int:paciente_id>/', views.prontuario, name="prontuario"),

    path('medicos/', views.medicos, name="medicos"),
    path('medicos/<int:medico_id>/', views.medico, name="medico"),

    path('secretarios/', views.secretarios, name="secretarios"),
    path('secretarios/<int:secretario_id>/', views.secretario, name="secretario"),
]
