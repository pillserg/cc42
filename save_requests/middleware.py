from cc42.save_requests.models import SavedRequest

class SaveEveryIncomingRequestToDB(object):
    def process_request(self, request):
        r = SavedRequest()
        r.from_http_request(request)