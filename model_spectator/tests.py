from tddspry.django import DatabaseTestCase
from django.contrib.auth.models import User

from cc42.model_spectator.models import ModelChange


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

    def test_other_model(self):
        CHOICES = (
                ('1', 'Created_or_Updated'),
                ('2', 'Deleted'),
            )
    
        User.objects.create_user('test_user','test@user.user')
        u = User.objects.get(email='test@user.user')
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name, u.username)
        self.assert_equal(last_entry.status, '1')
        u.name = 'test_user2'
        u.save()
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name, u.username)
        self.assert_equal(last_entry.status, '1')
        u.delete()
        last_entry = ModelChange.objects.all()[0]
        self.assert_equal(last_entry.name, 'test_user2')
        self.assert_equal(last_entry.status, '2')
        
