from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from appGH.forms import SignUpForm, UserForm, PacienteForm
from appGH.models import Paciente


def cadastrar_usuario(request, *args, **kwargs):
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('logar_usuario')

    if user.tipo_usuario not in ('admin', 'secretary'):
        return redirect('index')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form_usuario'] = form

    else:
        form = SignUpForm()
        context['form_usuario'] = form
    return render(request, 'cadastro.html', context)


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')


def index(request):
    if not request.user.is_authenticated:
        return redirect('logar_usuario')

    return render(request, 'index.html', {})


def prontuario(request, id_paciente):
    if not id_paciente:
        messages.error(request, 'Paciente não informado')
        return redirect('index')

    paciente = get_object_or_404(Paciente, id=id_paciente)
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('logar_usuario')

    context['active_tab'] = 'cadastro'
    form_usuario = UserForm(instance=paciente.usuario_id)
    form_paciente = PacienteForm(instance=paciente)

    if request.method == 'POST':
        if "form-usuario" in request.POST:
            form = UserForm(request.POST, instance=paciente.usuario_id)
            if form.is_valid():
                form.save()
            form_usuario = form

        if "form-paciente" in request.POST:
            form = PacienteForm(request.POST, instance=paciente)
            if form.is_valid():
                form.save()
            form_paciente = form
            context['active_tab'] = 'medico'

    context['form_usuario'] = form_usuario
    context['form_paciente'] = form_paciente
    return render(request, 'prontuario.html', context)
