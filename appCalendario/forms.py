from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from appCalendario.models import Agendamento


class AgendamentoForm(forms.ModelForm):
    especialidade = forms.ChoiceField(choices=Agendamento.ESPECIALIDADES, required=True)

    class Meta:
        model = Agendamento
        fields = "__all__"

        widgets = {
            "data_hora": DateTimePickerInput(options={"format": "HH:mm:ss DD/MM/YYYY"}),
        }
