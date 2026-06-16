import random
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

# Lista de nomes fictícios para criação em massa
nomes = [
    "Arthur Menezes", "Beatriz Figueiredo", "Caio Albuquerque", "Diana Sales",
    "Eduardo Tavares", "Fabiana Monteiro", "Guilherme Paes", "Helena Machado",
    "Isabela Porto", "João Azevedo", "Kauê Fernandes", "Letícia Moura",
    "Miguel Cardoso", "Nathalia Pinto", "Otávio Barbosa", "Paula Martins",
    "Quésia Ribeiro", "Rodrigo Sampaio", "Suelen Oliveira", "Thiago Fonseca",
    "Ulysses Carvalho", "Vitória Gomes", "Weslley Duarte", "Yuri Campos",
    "Zilda Nogueira", "Luana Barros", "Marcos Vinícius", "Patrícia Moreira",
    "Samuel Pimentel", "Talita Almeida"
]

# IDs dos grupos disponíveis no sistema
grupos_ids = [1, 2, 3, 4, 5, 6]

# Senha padrão para os usuários de teste
# Substitua por variável de ambiente em produção
senha = "Mudar@123"

for nome in nomes:
    partes = nome.split()
    username = f"{partes[0].lower()}.{partes[-1].lower()}"

    u = User.objects.create_user(
        username=username,
        name=nome,
        password=senha
    )

    grupo = Group.objects.get(id=random.choice(grupos_ids))
    u.groups.add(grupo)

    print(f"✅ CRIADO: ID={u.id} | username={username} | name={nome} | grupo={grupo.name}")

# Confirmação — lista os 30 últimos usuários criados
print("\n📋 Confirmação dos últimos 30 usuários criados:")
for u in User.objects.order_by('-id')[:30]:
    print(f"  ID={u.id} | {u.username} | grupos={[g.name for g in u.groups.all()]}")
