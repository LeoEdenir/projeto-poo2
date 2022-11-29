from django import forms
from django.contrib.auth.forms import UserCreationForm

from appGH.models import Usuario, Paciente, Medico, Secretario


class SignUpForm(UserCreationForm):
    TIPOS_USUARIOS = [
        ('patient', 'Paciente'),
        ('doctor', 'Médico'),
        ('secretary', 'Secretário'),
    ]

    data_nascimento = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        },
        format='%d/%m/%Y'
    ))
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIOS, required=False)
    sexo = forms.ChoiceField(choices=Usuario.SEXOS, required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'data_nascimento', 'tipo_usuario', 'sexo')

    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=commit)

        if instance.tipo_usuario == "patient":
            Paciente.objects.create(usuario_id=instance)
        elif instance.tipo_usuario == "doctor":
            Medico.objects.create(usuario_id=instance)
        elif instance.tipo_usuario == "secretary":
            Secretario.objects.create(usuario_id=instance)

        return instance


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'sexo', 'data_nascimento')


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ('usuario_id', )


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('registro_profissional', )


class SecretarioForm(forms.ModelForm):
    class Meta:
        model = Secretario
        fields = ('data_admissao', )
