import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = 'My Home Page'
    html_ = f'''
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome to {my_title}</h1>
</body>
</html>
'''
    # html_file_path = this_dir / 'home.html'
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)