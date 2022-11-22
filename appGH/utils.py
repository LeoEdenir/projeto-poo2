from django.shortcuts import redirect


def redirect_if_not_logged_in(request):
    if not request.user.is_authenticated:
        return redirect('logar_usuario')
