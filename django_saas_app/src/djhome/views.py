import pathlib
from django.http import HttpResponse

this_file = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    print(this_file)
    return HttpResponse('<h1>Hello, Django!</h1>')