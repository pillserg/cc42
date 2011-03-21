def settings_context_processor(request):
    from cc42 import settings
    return {'settings':settings}