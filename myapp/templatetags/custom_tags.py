from myapp.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('myapp/menu.html')
def draw_menu_templates(menu_name: str = None, menu_item: str = None):

    def get_menu(menu_item: str = None, submenu: list = None):
        menu = list(items.filter(parent=None)) if menu_item is None else list(items.filter(parent__name=menu_item))

        return menu



    items = MenuItem.objects.filter(menu__name=menu_name)



    return {'menu': get_menu()} if menu_name == menu_item else {'menu': get_menu(menu_item)}
