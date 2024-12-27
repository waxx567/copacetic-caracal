import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    print(this_file)
    html_ = ''
    html_file_path = this_dir / 'home.html'

    return HttpResponse('<h1>Hello, Django!</h1>')