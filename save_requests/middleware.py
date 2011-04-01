from cc42.save_requests.models import SavedRequest


class SaveEveryIncomingRequestToDB(object):
    def process_request(self, request):
        def _include():
            """checks if current request realy must be added to DB"""
            if request.path.startswith('/last-requests/'):
                return False
            if request.path.startswith('/static/'):
                return False
            return True

        if _include():
            req = SavedRequest()
            req.from_http_request(request)
