# About

> A simple Django project.

## Usage

Install `pip` and `venv` to create virtual enviroments.

```
$ sudo apt install python3-pip python3-venv
```

Then, create a virtual enviroment for project.

```
$ python3 -m venv django-alura-course-env
$ cd django-alura-course-env
$ source bin/activate
```

Clone project inside virtual enviroment folder and run server.

```
$ git clone https://github.com/rfcaio/django-alura-course.git
$ cd django-alura-course
$ python manage.py runserver
```

Create a super user.

```
$ python manage.py createsuperuser
```
