from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from appGH.forms import SignUpForm


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
    return render(request, 'index.html', {})
