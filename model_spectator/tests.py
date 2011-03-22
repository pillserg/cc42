from tddspry.django import DatabaseTestCase

from cc42.model_spectator.models import ModelChange
from cc42.contacts.models import UserDetail

test_data = {
    'name':'Test',
    'last_name':'Testovich',
    'contacts':'063-00-00-00',
    'email':'test@i.ua',
    'jabber':'pillserg@jabber.ru',
    'skype':'pillserg',
    'other_contacts':'pill.sv0@gmail.com\
                      ICQ:289861503',
    'bio':'Born in Kiev (1987) \
           Graduated from NAU (2010)\
           Currently looking for work.',
    'date_of_birth':'1987-09-03',
    }

def make_test_obj():
    kw_str = ', '.join(['='.join((str(k),("'''"+str(v)+"'''"))) for k,v in test_data.items()])
    run_str = 'UserDetail.objects.create(%s)'%kw_str
    eval(run_str)

class Test_onModelChangeEntryMustBeAddeToDB(DatabaseTestCase):
        
    def test_create(self):
        self.assert_create(ModelChange, name='test')
    
    def test_read(self):
        ModelChange.objects.create(name='test12345')
        self.assert_read(ModelChange, name='test12345')
        
    def test_update(self):
        MC = ModelChange(name='test12345')
        MC.save()
        self.assert_update(MC, name='test54321')

    def test_create_signal(self):
        make_test_obj()
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name,
                          str(UserDetail.objects.get(name=test_data['name'])))
        self.assert_equal(last_entry.get_status_display(), 'Created')
    
    def test_update_signal(self):
        make_test_obj()
        UD = UserDetail.objects.get(name=test_data['name'])
        UD.name = 'Dummy'
        UD.save()
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name, str(UD))
        self.assert_equal(last_entry.get_status_display(), 'Updated')
    
    def test_delete_signal(self):
        make_test_obj()
        UD = UserDetail.objects.get(name=test_data['name'])
        temp_repr = str(UD)
        UD.delete()
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name, temp_repr)
        self.assert_equal(last_entry.get_status_display(), 'Deleted')
        
