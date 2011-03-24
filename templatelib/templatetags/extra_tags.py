import re

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def obj_to_admin(obj):
    """
    getting parts from obj.__class__ and
    constructing url to admin page for this object
    """
    # Rewrite this using reverse
    try:
        return reverse("admin:%s_%s_change" % (obj._meta.app_label,
                                           obj._meta.module_name),
                                           args=(obj.id,))
    except:
        return ''