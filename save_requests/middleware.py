from cc42.save_requests.models import SavedRequest

class SaveEveryIncomingRequestToDB(object):
    def process_request(self, request):
        
        def include():
            exclude_paths = ['/last-requests/']
            if request.path in exclude_paths:
                return False
            if request.path.startswith('/static/'):
                return False
            return True
        
        if include():
            r = SavedRequest()
            r.from_http_request(request)
            