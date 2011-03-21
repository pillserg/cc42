from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from django.conf import settings

from cc42.contacts.models import UserDetail

test_data = {
    'name':'Serg',
    'last_name':'Piljavsky',
    'contacts':'063-00-00-00',
    'email':'pill@i.ua',
    'jabber':'pillserg@jabber.ru',
    'skype':'pillserg',
    'other_contacts':'pill.sv0@gmail.com\
                      ICQ:289861503',
    'bio':'Born in Kiev (1987) \
           Graduated from NAU (2010)\
           Currently looking for work.',
    'date_of_birth':'1987-09-03',
    }

class Test_contacts_UserDetailModel(DatabaseTestCase):

    new_name = 'Jane'
    
    def make_test_obj(self):
        kw_str = ', '.join(['='.join((str(k),("'''"+str(v)+"'''"))) for k,v in test_data.items()])
        run_str = 'self.assert_create(UserDetail, %s)'%kw_str
        eval(run_str)
    
    def test_create(self):
        self.make_test_obj()
    
    def test_read(self):
        self.make_test_obj()
        self.assert_read(UserDetail, name = test_data['name'])
        
    def test_update(self):
        self.make_test_obj()
        self.assert_update(UserDetail, name=self.new_name)
    
    def test_delete(self):
        self.make_test_obj()
        UD = UserDetail.objects.get(name=test_data['name'])
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
        
class TestContactsForm(NoseTestCase):

    def test_aceppting_valid_data(self):
        from cc42.contacts.forms import UserDetailForm
        from cc42.contacts.models import UserDetail

        form = UserDetailForm(instance=UserDetail.objects.get(id=1))
        self.assert_false(form.is_bound)
        form = UserDetailForm(test_data, instance=UserDetail.objects.get(id=1))
        self.assert_true(form.is_bound)
        self.assert_true(form.is_valid())

    def test_not_accepting_invalid_data(self):
        pass

class TestContactFormPage(HttpTestCase):
    def test_show_form(self):
        self.go('/edit-contacts/')
        
    
class TestContactForm(DatabaseTestCase):
    
    def test_save_form(self):
        from cc42.contacts.forms import UserDetailForm
        from cc42.contacts.models import UserDetail
        
        form = UserDetailForm(test_data, instance=UserDetail.objects.get(id=1))
        form.save()
        UD = UserDetail.objects.get(id=1)
        self.assert_equal(UD.name, test_data['name'])
    