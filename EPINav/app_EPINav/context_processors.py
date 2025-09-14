from app_EPINav.models import Colaborador

def user_context(request):
    colaborador = None
    if request.session.get("tipo_usuario") == "colaborador":
        try:
            colaborador = Colaborador.objects.get(id=request.session.get("usuario_id"))
        except Colaborador.DoesNotExist:
            colaborador = None

    return {
        "colaborador_logado": colaborador,
        "tipo_usuario": request.session.get("tipo_usuario"),
        "nome_usuario": request.session.get("nome_usuario"),
    }
