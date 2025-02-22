from django import template
import freedombooks_core.views as views
from freedombooks_core.models import BookModel, TagsModel, TextModel

register = template.Library()

@register.inclusion_tag('main/includes/list_categories.html')
def show_categories(cat_selected=0):
    cats = TagsModel.objects.all()
    return {'cats':cats, 'cat_selected':cat_selected}