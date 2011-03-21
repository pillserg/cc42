from tddspry.django import HttpTestCase, DatabaseTestCase

from django.conf import settings

from cc42.contacts.models import UserDetail

class Test_contacts_UserDetailModel(DatabaseTestCase):
    
    test_details = {
        'name':'Jone',
        'last_name':'Dow',
        'contacts':'Kiev',
        'email':'jd@i.ua',
        'jabber':'jd@jabber.ru',
        'skype':'12314325',
        'other_contacts':'twitter\nfacebook',
        'bio':'born here\nlived there',
        'date_of_birth':'1987-10-25'
        
    }
    
    new_name = 'Jane'
    
    def make_test_obj(self):
        kw_str = ', '.join(['='.join((str(k),("'''"+str(v)+"'''"))) for k,v in self.test_details.items()])
        run_str = 'self.assert_create(UserDetail, %s)'%kw_str
        eval(run_str)
    
    def test_create(self):
        self.make_test_obj()
    
    def test_read(self):
        self.make_test_obj()
        self.assert_read(UserDetail, name = self.test_details['name'])
        
    def test_update(self):
        self.make_test_obj()
        self.assert_update(UserDetail, name=self.new_name)
    
    def test_delete(self):
        self.make_test_obj()
        UD = UserDetail.objects.get(name=self.test_details['name'])
        self.assert_delete(UD)


class Test_MainPageBio(HttpTestCase):
    
    def test_userDetailMustBeOnMainPage(self):
        """
           Next things must be present on main page:
           Name, Last name, Contacts, Email: email, Jabber: JID,
           Skype: id, Other contacts: Multiline, Bio:, Multiline
           Date of birth"""
           
        details = UserDetail.objects.all()[0]
        print details.name
        self.go('/')
        self.find(details.name)
        self.find(details.last_name)
        self.find(details.contacts)
        self.find(details.email)
        self.find(details.jabber)
        self.find(details.skype)
        self.find(details.other_contacts)
        self.find(details.bio, flat=True)
        self.find(str(details.date_of_birth))

#-------------------I'm here now
        
class Test_last_request_middleware_shows_on_DB_page(HttpTestCase):
    
    def test_last_request_on_page(self):
        from cc42.save_requests.models import SavedRequests
        last_rq = SavedRequests.objects.order_by('timestamp')[0]
        self.go('/last_requests/')
        self.find(last_rq) # change to some actually checkable value
        
    def test_new_request_gets_into_DB(self):
        from cc42.save_requests.models import SavedRequests
        # assumes thet requests in DB are ordered by date 
        prew_rq = SavedRequests.objects.order_by('timestamp')[0]
        self.go('/')
        last_rq = SavedRequests.objects.order_by('timestamp')[0]
        self.assertNotEqual(prew_rq, last_rq)
        
        
    
class Test_last_request_middleware_to_DB(DatabaseTestCase):
    
    from cc42.save_requests.models import SavedRequests
    dummy_request = 'Dummy_request'
    def make_test_obj(self):
        SavedRequest.create(req=self.dummy_request)
    
    def test_create(self):
        self.make_test_obj()
    
    def test_read(self):
        self.make_test_obj()
        self.assert_read(SavedRequest, req=self.dummy_request)
        
    def test_update(self):
        self.make_test_obj()
        self.assert_update(UserDetail, req='new_dummy_request')
    
    def test_delete(self):
        self.make_test_obj()
        ReqObj = UserDetail.objects.get(req=self.dummy_request)
        self.assert_delete(ReqObj)
    

    