from tddspry.django import HttpTestCase, DatabaseTestCase
from cc42.save_requests.models import SavedRequest
from django.core.urlresolvers import reverse

class DummyRequest(object):
    """simple request imitator"""
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

class TestLastRequestSavedToDB(DatabaseTestCase):
    
    def make_test_obj(self):
        r = SavedRequest()
        r.from_http_request(DummyRequest(),)
    
    def test_create(self):
        self.make_test_obj()
    
    def test_read(self):
        self.make_test_obj()
        self.assert_read(SavedRequest, method=DummyRequest().method)
 
    def test_update(self):
        self.make_test_obj()
        self.assert_update(SavedRequest, method='POST')
    
    def test_delete(self):
        self.make_test_obj()
        request_instance = SavedRequest.objects.all()[0]
        self.assert_delete(request_instance)
 
    def test_priority(self):
        saved_req = SavedRequest()
        saved_req.from_http_request(DummyRequest(), priority = 5)
        saved_req = SavedRequest.objects.all()[0]
        self.assert_equal(saved_req.priority, 5)


class TestLastRequestsShowsOnPage(HttpTestCase):
    
    def test_request_link(self):
        self.go(reverse('show_edit_contacts'))
        self.find('requests')
    
    def test_request_info_in_place(self):
        self.go(reverse('show_edit_contacts'))
        self.go(reverse('show_last_requests'))
        last_request = SavedRequest.objects.all()[0]
        self.find(last_request.ip)
        self.find(last_request.path)
        self.find(last_request.method)
        self.find(last_request.referer)
        self.find(last_request.user_agent)
        self.find(last_request.language)
        
    def test_exclude_paths(self):
        self.go('static/css/base.css')
        self.go(reverse('show_edit_contacts'))
        self.go(reverse('show_last_requests'))
        last_request = SavedRequest.objects.all()[0]
        self.notfind(' static/css/base.css')
            
    def test_if_priority_links_in_place(self):
        self.go(reverse('show_last_requests'))
        self.find('>sort by time<')
        self.find('>sort by priority<')

class TestLastRequestsByPriorityShowsOnPage(HttpTestCase):
    
    def test_page_accesibility(self):
        self.go(reverse('show_main_page'))
        self.go(reverse('show_last_requests_by_priority'))
        self.find('127.0.0.1')
        
    def test_priority_change_form(self):
        r = SavedRequest()
        r.from_http_request(DummyRequest(),priority=999)
        SavedRequest.objects.all().order_by('priority')
        self.go(reverse('show_last_requests_by_priority'))
        self.find('999')
    
    def test_chnage_priority(self):
        """also check if form accepts valid data"""
        self.go(reverse('show_last_requests'))
        self.fv('1','priority','999')
        self.fv('1','for_all_by_ip', '0')
        self.fv('1','for_all_by_path', '0')
        self.submit()
        test_request = SavedRequest.objects.get(priority=999)
    
    def test_change_priority_declines_invalid_data(self):
        self.go(reverse('show_last_requests'))
        self.fv('1','priority','asdfasd')
        self.fv('1','for_all_by_ip', '9090')
        self.fv('1','for_all_by_path', 'asdad')
        self.submit()
        self.find('errorlist')
        