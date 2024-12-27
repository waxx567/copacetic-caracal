# My developer notes

Django is a free and open source Python web framework.

Encourages rapid development.

Extensive support and security.

Scalable.

Activate virtual environment
`conda activate out312`

Install Django version
`pip install django==3.1.4`

Create requirements.txt
`pip freeze > requirements.txt`

Google python gitignore, go to github.Python.gitignore, copy and paste file to your own `.gitignore`

Create Django project
`django-admin startproject djcrm .`

Run server
`python manage.py runserver`

Apply unapplied migrations
`python manage.py migrate`

Run server again to check there are no issues
`python manage.py runserver`

`settings.py`
FOR PRODUCTION `SECRET KEY` MUST BE KEPT SECRET AND `DEBUG` MUST BE SET TO FALSE
