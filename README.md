# Flask-Blog-API (GraphQL-and-REST)
Comparing GraphQL and REST web services

Blog API is a simple application built with Flask(a micro web-framework based on python).
The intent is mainly to compare REST and GRAPHQL in how queries and data manipulations are 
made in both web services.

## TECHNOLOGIES USED
- **Python**: [Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively
- **Flask**: [Flask](http://flask.pocoo.org/) is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
- **Flask Restful**: [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) is an extension for Flask that adds support for quickly building REST APIs
- **Graphene**: [Graphene-Python](http://graphene-python.org/) is a library for building GraphQL APIs in Python easily.
- **GraphQL**: [GraphQL](https://graphql.org/) is a query language for APIs and a runtime for fulfilling those queries with your existing data
- **Flask-Sqlalchemy**: [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) is an extension for Flask that adds support for SQLAlchemy to your application.
- **SQLAlchemy**: [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **Postgresql**: [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
-  **Pipenv**: [Pipenv](https://docs.pipenv.org/) is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.
- **Psycopg2**: [Psycopg](http://initd.org/psycopg/) is the most popular PostgreSQL adapter for the Python programming language.

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
$ pipenv install
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

### FOR REST
```
$ cd rest
```
**Run migrations and create database tables**
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
**Run the application**
```
$ python manage.py runserver
```
Use [postman](https://www.getpostman.com/) with the url **localhost:5000** to 
test out the endpoints

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

**Basic queries**

Get all users with user details
```
{
  users {
    id
    username
    email
  }
}
```

Get a single user
```
{
  user(userId: $id) {
    id
    username
    email
  }
}
$id is an integer number(positive)
```

Retrieve all articles
```
{
  articles {
    id
    title
    content
    category {
      name
      description
    }
  }
}
```

Retrieve a single article
```
{
  article(articleId: $id) {
    id
    title
    content
    category {
      name
      description
    }
  }
}
$id is an integer number(positive)
```

Retrieve articles by specific user
```
{
  userArticles(userId: $id) {
    id
    title
    content
    category {
      name
      description
    }
  }
}
$id is an integer number(positive)
```

**Basic mutations**

Create user
```
mutation {
  createUser(username: "name", email: "email", password: "password") {
    user {
      id
      username
      email
    }
  }
}
```

Create an article category
```
mutation {
  createCategory(name: "category name", description: "Text description") {
    category {
      id
      name
      description
    }
  }
}
```

Create an article
```
mutation {
  createArticle(title: "Article title", content: "Text content", userId: 1, categoryId: 1) {
    article {
      id
      title
      content
    }
  }
}
```

Edit an article
```
mutation {
  editArticle(articleId: 1, title: "New title", content: "New content"){
    article{
      id
      title
      content
    }
  }
}
```

Delete an article
```
mutation {
  deleteArticle(articleId: 1){
    article{
      id
    }
  }
}
```
