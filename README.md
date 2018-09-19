Django 101 Introduction
=======================

These are the materials and the code snippets used in Django
training sessions presented by [Moez Bouhlel](https://lejenome.github.io/) and
[Firas Chaaben](https://firchatn.tik.tn/) from [Tik.tn](https://tik.tn).

This repository is composed of different Django apps:

- Demo app containing Hello World example and a responsive contact page.
- CV app containing an example of Bootstrap based CV page generated from JSON
  files.
- Weather app containing an example of using Yahoo Weather API to generate a
  weather page.
- TODO List app example.
- Blog app example using markdown to render the content.
- Database-backed CV app.

**Common Django Commands:**

```sh
django-admin startproject PROJECT_NAME . # create a django project on current dir
python manage.py startapp APP_NAME       # create an app
python manage.py runserver [IP:PORT]     # run server on address http://IP:PORT or http://127.0.0.1:8000
python manage.py makemigrations          # generate app migration files
python manage.py migrate                 # apply migration files
python manage.py createsuperuser         # create superuser account
```

**Common Django app dev steps:**

- add app name to `INSTALLED_APPS` array on `PROJECT_NAME/settings.py` file.
- add url pattern to `urlpatterns` array on `PROJECT_NAME/urls.py` file to include APP_NAME `urls.py` file.
- define view function (or class) on `APP_NAME/views.py`
- define url pattern releated to the view function on `APP_NAME/urls.py` and add `name`
- define our Databese models on `APP_NAME/models.py` based on `models.Model` class
- define `__str__` funtion for every model to have a better name
- register our models to the admin site on `APP_NAME/admin.py`
- add our templates files under `APP_NAME/templates/APP_NAME/TEMPLATE.html`

**Links:**

- [Open Class Room Django Tutorial](https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django)
  (French)
- [Django Official Documentation](https://docs.djangoproject.com/en/1.10):

  - [Django Official Tutorial](https://docs.djangoproject.com/en/1.10/intro/overview/)

Self Promotion
--------------

[Tik.tn](https://tik.tn) is a skilled software development and consulting
agency. We offer the following services:

- **Training:**
  High-quality training for cutting-edge technologies for individuals and
  enterprises.
- **Consulting:**
  Optimize software architecture and code. Fix hardest bugs.
- **Web Development:**
  From simple single web page to high scale modular web platforms.
- **Software & Application Development:**
  Reliable software highly optimized for your system and your workflow.
- **IOT:**
  Turn-key long-lasting Big Data backed IOT build and integration solutions.
- **Cloud & Web Hosting:**
  PaaS hosting solution to meet every need. Top-class server administration
  services.

For more details, contact us at <contact@tik.tn> or contact [Moez
Bouhlel](https://lejenome.github.io/) at <bmoez.j@gmail.com>.

License
-------

These materials and code snippets are licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Copyright © 2016-2018, [Moez Bouhlel](https://lejenome.github.io/)
(<bmoez.j@gmail.com>) & [Firas Chaaben](https://lejenome.github.io/)
(<firchatn@tik.tn>), [Tik.tn](https://tik.tn).
