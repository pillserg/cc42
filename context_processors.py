def settings_context_processor(request):
    """adds request instance to RequestContext"""
    from cc42 import settings
    return {'settings':settings}