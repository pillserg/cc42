from tddspry.django import HttpTestCase
from cc42.contacts.models import UserDetail

class TestObjToAdminLinkTag(HttpTestCase):
    
    def test_tag(self):
        self.go('/')
        self.find('admin/contacts/userdetail/1')
        self.login_to_admin('admin','admin')
        self.go('/admin/contacts/userdetail/1/')
        user_detail_instance = UserDetail.objects.get(id=1)
        self.find(user_detail_instance.name)
        self.find(user_detail_instance.last_name)
        self.find(user_detail_instance.email)
        

    
    
        