# py_sns

## create venv

```
$ python3 -m venv venv_app
$ source venv_app/bin/activate
```

## add package

```
$ cd venv_app
$ pip install (modules)
$ pip freeze > requirements.txt
```

## create project

```
$ cd venv_app/py_sns
$ django-admin startproject py_sns_project
```

## create app

```
$ cd venv_app/py_sns/py_sns_project
$ python manage.py startapp py_sns_app
```

## start app

```
$ python manage.py runserver
```

http://127.0.0.1:8000/

## clone

```
$ source venv_app/bin/activate
$ pip install -r requirements.txt
```
