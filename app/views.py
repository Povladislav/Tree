from django.shortcuts import render
from app.models import Item, Menu


def index(request, menu_id):
    menus_before = Menu.objects.filter(id__lt=menu_id)
    menus_after = Menu.objects.filter(id__gt=menu_id)
    menu = Menu.objects.get(id=menu_id)
    items = Item.objects.filter(in_menu_id=menu_id)
    context = {
        "menu": menu,
        "menus_before": menus_before,
        "menus_after": menus_after,
        "items": items,
    }
    return render(request, "menu/menu.html", context=context)
