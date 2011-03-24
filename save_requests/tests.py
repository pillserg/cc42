from tddspry.django import HttpTestCase, DatabaseTestCase
from cc42.save_requests.models import SavedRequest
    
class TestLastRequestSavedToDB(DatabaseTestCase):
    
    class DummyRequest(object):
        
        def __init__(self):
            self.method = 'GET'
            self.path = '\\'
            self.is_secure = False
            self.is_ajax = False
            self.META = {}
            # User infomation
            self.META['ip'] = '74.125.87.99'
            self.META['referer'] = 'referer'
            self.META['user_agent'] = 'generic browser'
            self.META['language'] = 'en'
 
    dummy_request = DummyRequest()
    
    def make_test_obj(self):
        r = SavedRequest()
        r.from_http_request(self.dummy_request,)
    
    def test_create(self):
        self.make_test_obj()
    
    def test_read(self):
        self.make_test_obj()
        self.assert_read(SavedRequest, method=self.dummy_request.method)
 
    def test_update(self):
        self.make_test_obj()
        self.assert_update(SavedRequest, method='POST')
    
    def test_delete(self):
        self.make_test_obj()
        request_instance = SavedRequest.objects.all()[0]
        self.assert_delete(request_instance)
 
    #def test_priority(self):
    #    saved_req = SavedRequest()
    #    saved_req.from_http_request(self.dummy_request, priority = 5)
    #    saved_req = SavedRequest.objects.all().order_by('priority')[0]
    #    self.assert_equal(saved_req.priority, 5)


class TestLastRequestsShowsOnPage(HttpTestCase):
    
    def test_request_link(self):
        self.go('/')
        self.find('requests')
    
    def test_request_info_in_place(self):
        self.go('/')
        self.go('last-request/')
        last_request = SavedRequest.objects.all()[0]
        self.find(last_request.ip)
        self.find(last_request.path)
        self.find(last_request.method)
        self.find(last_request.referer)
        self.find(last_request.user_agent)
        self.find(last_request.language)
        
    def test_exclude_paths(self):
        self.go('static/css/base.css')
        self.go('/')
        self.go('last-requests/')
        last_request = SavedRequest.objects.all()[0]
        self.notfind(' static/css/base.css')
            
    def test_if_priority_links_in_place(self):
        self.go('last-requests/')
        self.find('>sort by time<')
        self.find('>sort by priority<')

    