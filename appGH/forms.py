from django import forms
from django.contrib.auth.forms import UserCreationForm

from appGH.models import Usuario


class SignUpForm(UserCreationForm):
    TIPOS_USUARIOS = [
        ('patient', 'Paciente'),
        ('doctor', 'Médico'),
        ('secretary', 'Secretário'),
    ]

    data_nascimento = forms.DateField(required=False, widget=forms.SelectDateWidget(
        years=[str(i) for i in range(1900, 2022)]
    ))
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS, required=False)
    sexo = forms.ChoiceField(choices=Usuario.SEXOS, required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'data_nascimento', 'tipo_usuario', 'sexo')
