import os
from django.contrib.auth import get_user_model

# Configuração
USUARIO = os.environ.get("USUARIO", "nome.sobrenome")
NOME = os.environ.get("NOME", "Nome Sobrenome")
SENHA = os.environ.get("SENHA", "Mudar@123")

User = get_user_model()

u = User.objects.create_user(
    username=USUARIO,
    name=NOME,
    password=SENHA
)

print(f"✅ Usuário criado: ID={u.id} | username={u.username} | name={u.name}")
