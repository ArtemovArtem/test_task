from django.shortcuts import render

# Create your views here.


from .models import Menu


def index(request):

    men = Menu.objects.all()

    return render(request, 'myapp/index.html', {'menus': men})


def draw_menu(request, path):
    spisok_punkty = path.split('/')

    return render(request, 'myapp/index.html', {'menu_name': spisok_punkty[0], 'menu_item': spisok_punkty[-1]})


