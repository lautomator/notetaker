# Notetaker

Journaling web application (Django)

## Overview
The purpose of this web application is to have a place to take and store daily notes for possible investments and speculation. This application was created using [Django](https://www.djangoproject.com/). It should be used locally only, as it is not protected with user or login features.

## Development
You will need:

* Python 3 (venv module and PIP): see `requirements.txt`

* Django

* nodejs v12.22.5

* npm v6.14.14

You can use node [NVM](https://github.com/nvm-sh/nvm#about) -- node version control -- to emulate this environment.

`journal/package.json` has all of the listed dependencies and build details. The dependencies are:

* minify

* npm-watch

* sass

### Setup/Virtual Environment
Download this repository. To get the virtual environment running, cd into `notetaker` and run `python3 -m venv env`. Check the [Python docs](https://docs.python.org/3/library/venv.html) for more information about the *venv* module.

Run the virtual environment: `. env/bin/activate`.

Install the dependencies (including Django): `pip install -r requirements.txt`.

cd into `journal/` and run `npm install` to install all the of the node modules needed for development.

To run the Django server, cd back into the top directory and run `python manage.py runserver`. You can then navigate to the url displayed in the console.

### CSS and SASS
Don't edit any `.css` files. The CSS files are auto-generated when you run the build script or watch scripts. Make all edits to the SASS files in `journal/static/scss/` directory.

### Django Commands

get all of the manage.py commanes:
    `python manage.py help`

start a project:
    `django-admin startproject <project_name>`

run the server:
    `python manage.py runserver`

create an app:
    `python manage.py startapp <app_name>`

after creating or editing models:
    `python manage.py makemigrations <app_name>`

    `python manage.py migrate`

use the shell:
    `python manage.py shell`

admin create a superuser:
    `python manage.py createsuperuser`
