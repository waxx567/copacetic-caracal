# My developer notes

## 2024/12/27

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

`db.sqlite3`
OK FOR DEVELOPMENT ENVIRONMENT BUT NOT RECOMMENDED FOR PRODUCTION

`settings.py`
FOR PRODUCTION `SECRET KEY` MUST BE KEPT SECRET

`settings.py`
FOR PRODUCTION `DEBUG` MUST BE SET TO FALSE

`settings.py`
`ALLOWED HOSTS` is a list of hosts that this project is permitted to be hosted on eg. `ALLOWED HOSTS = ['mydomain.com']` no need for http or https

`settings.py`
`TEMPLATES 'DIRS': []` is a list of directories. Our own folders or template we want use need to be specified here so that Django is aware of them.

Create leads app
`python manage.py startapp leads`

Add `'leads'` to INSTALLED APPS list in `djcrm/settings.py`

### Creating a class

When creating a class in Django (in `leads/models.py`), you need to run
`python manage.py makemigrations`
to create a list of operations to apply to the database when creating models.
This `Migration` class (stored in `leads/migrations/0001_initial.py`, for example) is a representation of what we want to happen to the database whenever we create a schema.
This is a blueprint. The database `db.sqlite3` has not been altered yet.
Then run
`python manage.py migrate`
which causes Django to look through inside the migrations folders of all of our apps and run through all of the migration files inside those apps, applying all those which haven't been applied yet.
Now the database has been updated.

It would be preferable to have a customer records app that can add leads later.

Also better to use MySQL for production.

Let's plan things better beforehand this time.

My investigations lead me to believe PostgreSQL is favored by most players in the industry.

## 2024/12/29 (1:18:58)

### Prepare for Production Environment

I am going to try to deploy to production. I am doing this because I think it is important to be able to do this quickly and easily if I'm going to be maintaining applications regularly.

I know the app is not production ready, and I will not be changing the `SECRET KEY` and `Debug=True` in `settings.py` yet. I'm keeping them on because I'm testing my production environment, not pushing into production for other people to use.

`1:25:30`
Deploy Django to Railway with Docker Containers
Created a branch `Base-code` with the code as it stands.
[Reference Blog Post](https://www.codingforentrepreneurs.com/blog/deploy-django-on-railway-with-this-dockerfile)
