from django.shortcuts import redirect

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('usuario_id'):  # verifica se o usuário está logado
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  # redireciona para login se não estiver logado
    return wrapper
