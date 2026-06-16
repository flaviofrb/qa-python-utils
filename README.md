# qa-python-utils

Repositório com scripts utilitários em Python desenvolvidos como suporte ao processo de QA em aplicações Django.

---

## Contexto e Objetivo

Durante a atuação em projetos com aplicações web desenvolvidas em Django, surgiu a necessidade de popular o banco de dados com usuários de teste de forma rápida e controlada.

A criação manual de usuários um a um via interface era ineficiente e consumia tempo desnecessário antes da execução dos testes. Para resolver isso, foram desenvolvidos scripts via **Django shell** que permitem:

- Criar um único usuário com username, nome e senha definidos
- Criar múltiplos usuários em massa com perfis/grupos atribuídos aleatoriamente
- Confirmar os registros criados diretamente no terminal
- Vincular usuários a perfis manualmente via SQL no pgAdmin, quando necessário

O objetivo principal era **preparar o ambiente de testes de forma ágil**, garantindo que os cenários de teste pudessem ser executados com dados reais e variados, simulando diferentes perfis de usuário no sistema.

---

## Pré-requisitos

- Python 3.x
- Django configurado no projeto
- Acesso ao banco de dados (PostgreSQL via pgAdmin para scripts SQL)

---

## Scripts

### criar_usuario.py
Cria um único usuário no sistema via Django shell.

**Quando usar:** quando precisar criar um usuário específico com username, nome e senha definidos manualmente.

**Como usar:**
```bash
# Acesse o shell do Django
python manage.py shell

# Execute o script
exec(open('criar_usuario.py').read())
```

Ou defina as variáveis de ambiente antes de rodar:
```bash
USUARIO=joao.silva NOME="João Silva" SENHA=SuaSenha python manage.py shell
```

**O que o script faz:**
1. Lê as variáveis de ambiente (ou usa valores padrão)
2. Cria o usuário no banco via `create_user`
3. Exibe o ID, username e nome do usuário criado

---

### criar_usuarios_massa.py
Cria 30 usuários fictícios de uma vez, com grupos/perfis atribuídos aleatoriamente.

**Quando usar:** quando precisar popular o ambiente de testes com vários usuários de perfis diferentes para cobrir cenários distintos — por exemplo, testar comportamentos por nível de acesso (administrador, editor, leitor etc.).

**Como usar:**
```bash
# Acesse o shell do Django
python manage.py shell

# Execute o script
exec(open('criar_usuarios_massa.py').read())
```

**O que o script faz:**
1. Define uma lista de 30 nomes fictícios
2. Gera o username automaticamente no formato `nome.sobrenome`
3. Cria cada usuário com senha padrão via `create_user`
4. Atribui aleatoriamente um dos grupos disponíveis no sistema (IDs 1 a 6)
5. Exibe no terminal cada usuário criado com seu respectivo grupo
6. Ao final, lista os 30 últimos usuários criados para confirmação

**Exemplo de saída:**
```
✅ CRIADO: ID=45 | username=arthur.menezes | name=Arthur Menezes | grupo=Administrador
✅ CRIADO: ID=46 | username=beatriz.figueiredo | name=Beatriz Figueiredo | grupo=Leitor
...

📋 Confirmação dos últimos 30 usuários criados:
  ID=74 | talita.almeida | grupos=['Editor']
  ID=73 | samuel.pimentel | grupos=['Administrador']
  ...
```

---

## SQL — Vincular usuário a perfil manualmente via pgAdmin

Em alguns casos, foi necessário vincular um usuário a um grupo diretamente no banco de dados usando o **Query Tool do pgAdmin**, sem passar pela interface do sistema.

**Quando usar:** quando a interface não permitia a vinculação, ou quando era necessário agilizar o processo durante a preparação do ambiente de testes.

**Inserir vínculo:**
```sql
-- Substitua os valores pelo ID real do usuário e do grupo desejado
INSERT INTO account_user_groups (id_user, id_group)
VALUES (44, 3);
```

**Confirmar vínculos criados:**
```sql
SELECT u.id, u.username, g.name AS grupo
FROM auth_user u
JOIN account_user_groups aug ON u.id = aug.id_user
JOIN auth_group g ON g.id = aug.id_group
ORDER BY u.id DESC
LIMIT 30;
```

---

## Fluxo completo utilizado

```
1. Acessar o Django shell via terminal
       ↓
2. Rodar criar_usuario.py (usuário individual)
   ou criar_usuarios_massa.py (30 usuários com grupos aleatórios)
       ↓
3. Confirmar criação no terminal
       ↓
4. Se necessário, vincular perfil manualmente via SQL no pgAdmin
       ↓
5. Ambiente de testes pronto para execução dos cenários
```

---

## Sobre

Scripts desenvolvidos durante atuação como QA Engineer, com o objetivo de agilizar a preparação de ambientes de teste em aplicações Django. A abordagem via Django shell permitiu criar e configurar usuários de forma rápida, segura e reproduzível, sem depender de processos manuais demorados.
