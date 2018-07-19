# Flask-Blog-API (GraphQL-and-REST)
Comparing GraphQL and REST web services

Blog API is a simple application built with Flask(a micro web-framework based on python).
The intent is mainly to compare REST and GRAPHQL in how queries and data manipulations are 
made in both web services.

## SETTING UP THE PROJECT

### Clone the project
```
$ git clone https://github.com/PatrickCmd/Flask-Blog-API-GraphQL-and-REST-.git
$ cd Flask-Blog-API-GraphQL-and-REST-
```

### Active the virtual environment
```
$ pip install pipenv
$ pipenv shell
```

### Install the requirements
```
pipenv install
```

## SETTING UP THE DATABASE
Execute the commands in the terminal/console as stated below

### ON WINDOWS
Follow the [Link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) on how to download 
and install postgres(>=10) on windows platform

**Create Database**
```
$ psql -U postgres
$postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ SET DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname} Where port is the port number for the postgres instance
```

### ON MAC/UBUNTU
**Install postgres**
**MAC Users**
```
$ brew install postgres
```
Follow the [link](https://brew.sh/) on how to setup brew if not yet installed
**Ubuntu users**
Follow the [Link](https://www.postgresql.org/download/linux/ubuntu/) on how to setup 
and install postgres(>=10) on Ubuntu-linux platform

**Create Database**
```
$ psql -U postgres
$postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ export DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname} Where port is the port number for the postgres instance
```

### STARTING THE APPLICATION

### FOR GRAPHQL
```
$ cd graphql
```
**Create database tables**
```
$ python manage.py create_db
```
**Run the application**
```
$ python manage.py runserver
```
Follow the link **localhost:5000/blog_api** in the browser address and get the **GraphiQL** 
the GraphQL web client and follow the document in the **Documentation Explorer** to start
running the queries and mutations
