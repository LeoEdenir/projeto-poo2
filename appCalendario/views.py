from django.shortcuts import render, redirect

from appCalendario.forms import AgendamentoForm
from appCalendario.models import Agendamento
from appGH.utils import redirect_if_not_logged_in


def agenda(request):
    redirect_if_not_logged_in(request)

    if request.user.tipo_usuario == "patient":
        meetings = Agendamento.objects.filter(paciente_id__usuario_id=request.user)
    else:
        meetings = Agendamento.objects.all()

    context = {
        "meetings": meetings,
        "form_agendamento": AgendamentoForm()
    }
    return render(request, 'agenda.html', context)


def criar_agendamento(request):
    redirect_if_not_logged_in(request)
    context = {"created": False}
    if request.method == 'POST' and request.user.tipo_usuario in ("admin", "secretary"):

        initial = {}
        if request.user.tipo_usuario == "secretary":
            initial['secretario_id'] = request.user.secretary

        form = AgendamentoForm(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            context["created"] = True
            context["form_agendamento"] = AgendamentoForm()
        else:
            context["form_agendamento"] = form

    meetings = Agendamento.objects.all()
    context["meetings"] = meetings

    return render(request, 'agenda.html', context)


def pegar_agendamento(request, agendamento_id):
    redirect_if_not_logged_in(request)

    agendamento = Agendamento.objects.get(id=agendamento_id)
    context = {"updated": False, "agendamento": agendamento}

    if request.method == 'POST' and request.user.tipo_usuario in ("admin", "secretary"):
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            context["updated"] = True
            context["form_agendamento"] = form
        else:
            context["form_agendamento"] = form

    elif request.method == 'GET':
        form = AgendamentoForm(instance=agendamento)
        context["form_agendamento"] = form

    return render(request, 'agendamento.html', context)
