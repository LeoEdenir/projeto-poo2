from django.db import models

from appGH.models import Paciente, Medico, Secretario


class Agendamento(models.Model):
    paciente_id = models.ForeignKey(verbose_name="Paciente", to=Paciente, related_name="agendamentos",
                                    on_delete=models.CASCADE)
    medico_id = models.ForeignKey(verbose_name="Médico", to=Medico, related_name="agendamentos",
                                  on_delete=models.SET_NULL, null=True)
    secretario_id = models.ForeignKey(verbose_name="Secretário", to=Secretario, related_name="agendamentos",
                                      on_delete=models.SET_NULL, null=True)

    criado_em = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    data_hora = models.DateTimeField(verbose_name="Data e hora")

    ESPECIALIDADES = [
        ("CM", "Clínica Médica"),
        ("CC", "Clínica Cirúrgica"),
        ("CG", "Clínica Gineco-obstétrica"),
        ("CP", "Clínica Pediátrica"),
    ]

    especialidade = models.CharField(verbose_name="Especialidade", max_length=3)
    teleconsulta = models.BooleanField(verbose_name="É teleconsulta?", default=False)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ("-data_hora", "paciente_id__usuario_id__first_name")
