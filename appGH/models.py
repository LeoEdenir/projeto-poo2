import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    TIPOS_USUARIOS = [
        ('patient', 'Paciente'),
        ('doctor', 'Médico'),
        ('secretary', 'Secretário'),
        ('admin', 'Administrador'),
    ]
    SEXOS = [
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    ]

    tipo_usuario = models.CharField(verbose_name="Tipo de usuário", choices=TIPOS_USUARIOS, max_length=10)
    sexo = models.CharField(verbose_name="Sexo", choices=SEXOS, max_length=10)
    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ("first_name",)

    def __str__(self):
        return self.get_full_name()

    @property
    def age(self):
        return int((datetime.date.today() - self.data_nascimento).days / 365) if self.data_nascimento else 0

    @property
    def is_paciente(self):
        return self.tipo_usuario == "patient"

    @property
    def is_medico(self):
        return self.tipo_usuario == "doctor"

    @property
    def is_secretario(self):
        return self.tipo_usuario == "secretary"

    @property
    def is_admin(self):
        return self.tipo_usuario == "admin"


class Medico(models.Model):
    usuario_id = models.OneToOneField(verbose_name="Usuário", to=Usuario, related_name="doctor",
                                      on_delete=models.CASCADE)
    registro_profissional = models.CharField(verbose_name="Registro profissional", max_length=255)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return f"Médico - {self.usuario_id.get_full_name()}"


class Secretario(models.Model):
    usuario_id = models.OneToOneField(verbose_name="Usuário", to=Usuario, related_name="secretary",
                                      on_delete=models.CASCADE)
    data_admissao = models.DateField(verbose_name="Data de admissão")

    class Meta:
        verbose_name = "Secretário"
        verbose_name_plural = "Secretários"

    def __str__(self):
        return f"Secretário - {self.usuario_id.get_full_name()}"


class Paciente(models.Model):
    usuario_id = models.OneToOneField(verbose_name="Usuário", to=Usuario, related_name="patient",
                                      on_delete=models.CASCADE)
    hipertensao = models.BooleanField(verbose_name="Hipertensão", default=False)
    depressao = models.BooleanField(verbose_name="Depressão", default=False)
    ansiedade = models.BooleanField(verbose_name="Ansiedade", default=False)
    diabetes_tipo_1 = models.BooleanField(verbose_name="Diabetes tipo 1", default=False)
    diabetes_tipo_2 = models.BooleanField(verbose_name="Diabetes tipo 2", default=False)
    hipotireoidismo = models.BooleanField(verbose_name="Hipotireoidismo", default=False)
    hepatite_b = models.BooleanField(verbose_name="Hepatite B", default=False)
    hepatite_c = models.BooleanField(verbose_name="Hepatite C", default=False)
    asma = models.BooleanField(verbose_name="Asma", default=False)
    epilepsia = models.BooleanField(verbose_name="Epilepsia", default=False)
    aids = models.BooleanField(verbose_name="aids", default=False)
    avc = models.BooleanField(verbose_name="AVC", default=False)
    demencia = models.BooleanField(verbose_name="Demência", default=False)

    altura = models.PositiveSmallIntegerField(verbose_name="Altura (cm)", blank=True, null=True)
    peso = models.FloatField(verbose_name="Peso (kg)", blank=True, null=True)

    informacoes_adicionais = models.TextField(verbose_name="Informações adicionais", blank=True, null=True)

    @property
    def imc(self):
        return self.peso / ((self.altura / 100)**2)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"Paciente - {self.usuario_id.get_full_name()}"
