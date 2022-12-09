# BackEcommerceCarro

1 - Após fazer clone do projeto, instale suas dependencias através do comando (feito no windows)

abra o terminal dentro da raiz do projeto e rode:

`virtualenv env`

`env\Scripts\Activate`

`pip install -r requeriments.txt`

# rodando o projeto

apos os comando anterios, execute 

`python manage.py runserver 0.0.0.0:8000`

# Banco de Dados
para facilitar o projeto, deixei vinculado ao Sqlite, ele ja esta com algumas informações preenchidas para teste


por padrao novos usuarios nao são setados como admin

para isso, sete manualmente no banco de dados os campos 

`is_staff = true`

`is_superuser = true`


