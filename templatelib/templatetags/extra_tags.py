import re
from django import template

register = template.Library()

@register.simple_tag
def obj_to_admin(obj):
    """
    getting parts from obj.__class__ and
    constructing url to admin page for this object
    """
    # Rewrite this using reverse
    try:
        s = str(obj.__class__)
        ls = s[1:-1].replace("'",'').split()[1].split('.')
        url = '/'.join(('admin', ls[1], ls[-1].lower(), str(1)))
        return '<a href=%s>Edit(admin)</a>' % url
    except:
        return ''
    