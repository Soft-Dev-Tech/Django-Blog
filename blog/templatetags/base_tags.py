from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title():
    return "Django Blog"


@register.inclusion_tag("blog/partials/category_nav_tag.html")
def category_navbar():
    return {
        "categories": Category.objects.filter(status=True)
    }

@register.inclusion_tag("registration/partials/link.html")
def activ_link(request, link_name, content, icon):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{}". format(link_name),
        "content": content, 
        "icon" : icon,
    }
