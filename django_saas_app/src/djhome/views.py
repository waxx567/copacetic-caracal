from django.http import HttpResponse

def home_page_view():

    return HttpResponse('<h1>Hello, Django!</h1>')