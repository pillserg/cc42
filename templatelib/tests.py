from tddspry.django import HttpTestCase
from cc42.contacts.models import UserDetail
from cc42.templatelib.templatetags import extra_tags

class Test_obj_to_admin_link_tag(HttpTestCase):
    
    def test_tag(self):
        self.go('/')
        self.find('admin/contacts/userdetail/1')
        self.login_to_admin('admin','admin')
        self.go('/admin/contacts/userdetail/1/')
        UD = UserDetail.objects.get(id=1)
        self.find(UD.name)
        self.find(UD.last_name)
        self.find(UD.email)
        

    
    
        