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

#class TestMainPageBio(HttpTestCase, DatabaseTestCase):
#    def userDetailMustBeOnMainPage(self):
#        """
#           Next things must be present on main page:
#           Name, Last name, Contacts, Email: email, Jabber: JID,
#           Skype: id, Other contacts: Multiline, Bio:, Multiline
#           Date of birth"""
#    details = UserDetail.objects.all()[0]
#    self.go('/')
#    self.find(details.name)
#    self.find(details.last_name)
#    self.find(details.contacts)
#    self.find(details.email)
#    self.find(details.jabber)
#    self.find(details.skype)
#    self.find(details.other_contacts)
#    self.find(details.bio)
#    self.find(details.date_of_birth)


    

