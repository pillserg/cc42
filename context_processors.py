"""custom context processors"""
from django.conf import settings


def settings_context_processor(request):
    """adds request instance to RequestContext"""
    return {'settings': settings}
