from django.core.management.base import BaseCommand
from app_EPINav.models.colaborador import Colaborador
from app_EPINav.models.usuario import UsuarioSistema

class Command(BaseCommand):
    help = "Cria usuários padrão (admin e colaborador) se não existirem"

    def handle(self, *args, **options):
        # Usuário admin
        admin_user, created = UsuarioSistema.objects.get_or_create(
            nome_usuario="admin",
            senha="",
            is_admin=True,
        )
        if created:
            UsuarioSistema.set_password(admin_user, "1234")
            UsuarioSistema.save(admin_user)
            self.stdout.write("UsuárioSistema admin criado (admin/1234)")
        else:
            self.stdout.write("UsuárioSistema admin já existe")

        # Colaborador padrão
        colaborador, created = Colaborador.objects.get_or_create(
            nome_usuario="colaborador1",
            defaults={
                "nome": "Colaborador 1",
                "cargo": "Funcionário",
                "status": "Ativo",
                "senha": "",
            }
        )
        if created:
            colaborador.set_password("1234")
            colaborador.save()
            self.stdout.write("Colaborador padrão criado (colaborador1/1234)")
        else:
            self.stdout.write("Colaborador padrão já existe")
