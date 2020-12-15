## Brooklyn's Market

### Sumário
1. [Sobre](#Sobre)
2. [Screenshots](#Screenshots)
3. [Tecnologias](#Tecnologias)
4. [Execução](#Execução)

### Sobre
O Brooklyn's Market se trata de uma loja virtual de uma Açaíteria. O cliente poderá ver o cardápio, fazer pedidos e ver os produtos no carrinho de compras.

### Screenshots
##### Home
![Home Page](/screenshots/home.png)

##### Login
![Home Page](/screenshots/login.png)

##### Signup
![Home Page](/screenshots/signup.png)

### Tecnologias
Utilizaremos a linguagem de programação Python junto com o framework Django, junto a ele faremos o uso do PostgreSQL para acesso ao banco de dados e da biblioteca de estilo Bootstrap.

1. [Python3](https://www.python.org/) 
2. [Django](https://www.djangoproject.com/)
3. [PostgreSQL](https://www.postgresql.org/)
4. [Bootstrap](https://getbootstrap.com/)

### Execução

1. Criando ambiente virtual
    > python3 -m venv myvenv

2. Ativando ambiente virtual  
    2.1 Linux
    > source myvenv/bin/activate

    2.2 Windows
    > myvenv/Scripts/activate

3. Instale as dependências
    > pip install -r requirements.txt

4. Criando um Superuser
    > python manage.py createsuperuser

5.  Criando banco de dados
    > python manage.py makemigrations

6.  Atualizando tabelas do banco de dados
    > python manage.py migrate

7. Para rodar o server execute
    > python manage.py runserver
