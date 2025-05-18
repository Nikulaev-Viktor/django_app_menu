from django import template
from django.urls import reverse, NoReverseMatch
from tree_menu.models import Menu, MenuItem

register = template.Library()


def get_expanded_ids(active_item):
    expanded_ids = set()
    if active_item:
        while active_item.parent:
            expanded_ids.add(active_item.parent_id)
            active_item = active_item.parent
    return expanded_ids


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': [], 'expanded_ids': set(), 'current_path': current_path}

    items = list(MenuItem.objects.filter(menu=menu).select_related('parent'))

    active_item = None
    for item in items:
        try:
            if current_path == item.get_absolute_url():
                active_item = item
                break
        except NoReverseMatch:
            continue

    expanded_ids = get_expanded_ids(active_item)

    return {
        'menu_items': items,
        'current_path': current_path,
        'expanded_ids': expanded_ids
    }


@register.filter
def children_of(items, parent):
    return [item for item in items if item.parent_id == parent.id]