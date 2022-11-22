from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect, get_object_or_404

from appGH.forms import SignUpForm, UserForm, PacienteForm, MedicoForm, SecretarioForm
from appGH.models import Paciente, Medico, Secretario
from appGH.utils import redirect_if_not_logged_in


def cadastrar_usuario(request, *args, **kwargs):
    redirect_if_not_logged_in(request)

    context = {}
    user = request.user

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
    redirect_if_not_logged_in(request)

    return render(request, 'index.html', {})


def pacientes(request):
    redirect_if_not_logged_in(request)

    buscar = request.GET.get('buscar')
    if buscar:
        instances = Paciente.objects.annotate(
            full_name=Concat('usuario_id__first_name', Value(' '), 'usuario_id__last_name')
        ).filter(full_name__icontains=buscar)
    else:
        instances = Paciente.objects.all()

    context = {'pacientes': instances}
    return render(request, 'pacientes.html', context)


def prontuario(request, paciente_id):
    redirect_if_not_logged_in(request)

    if not paciente_id:
        return redirect('pacientes')

    paciente = get_object_or_404(Paciente, id=paciente_id)
    context = {'active_tab': 'cadastro'}

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


def medicos(request):
    redirect_if_not_logged_in(request)

    buscar = request.GET.get('buscar')
    if buscar:
        instances = Medico.objects.annotate(
            full_name=Concat('usuario_id__first_name', Value(' '), 'usuario_id__last_name')
        ).filter(full_name__icontains=buscar)
    else:
        instances = Medico.objects.all()

    context = {'medicos': instances}
    return render(request, 'medicos.html', context)


def medico(request, medico_id):
    redirect_if_not_logged_in(request)

    if not medico_id:
        return redirect('medicos')

    medico = get_object_or_404(Medico, id=medico_id)
    context = {'active_tab': 'cadastro'}

    form_usuario = UserForm(instance=medico.usuario_id)
    form_medico = MedicoForm(instance=medico)

    if request.method == 'POST':
        if "form-usuario" in request.POST:
            form = UserForm(request.POST, instance=medico.usuario_id)
            if form.is_valid():
                form.save()
            form_usuario = form

        if "form-medico" in request.POST:
            form = MedicoForm(request.POST, instance=medico)
            if form.is_valid():
                form.save()
            form_medico = form
            context['active_tab'] = 'medico'

    context['form_usuario'] = form_usuario
    context['form_medico'] = form_medico
    return render(request, 'medico.html', context)


def secretarios(request):
    redirect_if_not_logged_in(request)

    buscar = request.GET.get('buscar')
    if buscar:
        instances = Secretario.objects.annotate(
            full_name=Concat('usuario_id__first_name', Value(' '), 'usuario_id__last_name')
        ).filter(full_name__icontains=buscar)
    else:
        instances = Secretario.objects.all()

    context = {'secretarios': instances}
    return render(request, 'secretarios.html', context)


def secretario(request, secretario_id):
    redirect_if_not_logged_in(request)

    if not secretario_id:
        return redirect('secretarios')

    secretario = get_object_or_404(Secretario, id=secretario_id)
    context = {'active_tab': 'cadastro'}

    form_usuario = UserForm(instance=secretario.usuario_id)
    form_secretario = SecretarioForm(instance=secretario)

    if request.method == 'POST':
        if "form-usuario" in request.POST:
            form = UserForm(request.POST, instance=secretario.usuario_id)
            if form.is_valid():
                form.save()
            form_usuario = form

        if "form-secretario" in request.POST:
            form = SecretarioForm(request.POST, instance=secretario)
            if form.is_valid():
                form.save()
            form_secretario = form
            context['active_tab'] = 'secretario'

    context['form_usuario'] = form_usuario
    context['form_secretario'] = form_secretario
    return render(request, 'secretario.html', context)
