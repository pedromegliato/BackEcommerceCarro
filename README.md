# BackEcommerceCarro
Antes de tudo é necessário que vc tenha o python e o virtualenv nistalados em sua máquina


1 - Após fazer clone do projeto, instale suas dependencias através dos comandos

abra o terminal dentro da raiz do projeto e rode:

`virtualenv env`

`env\Scripts\Activate` (windows)
`. env/bin/activate` (linux)

`pip install -r requeriments.txt`

# rodando o projeto

apos a conclusão dos comandos anterioress, execute 

`python manage.py runserver 0.0.0.0:8000` que o projeto será executado na porta 8000, caso mude a porta, vc tera que atualizar a rota da chamada de api no FrontEnd tambem

# Banco de Dados
para facilitar o projeto, deixei vinculado ao Sqlite, ele ja esta com algumas informações preenchidas para teste

Caso queira outro SGBD em settings dentro da pasta controlador Main vc consegue ver a esrutura para linkar outro SGBD

por padrao novos usuarios são setados como admin, não foi implementado a regra para niveis de acesso


