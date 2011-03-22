from tddspry.django import DatabaseTestCase
from cc42.model_spectator.models import ModelChange

class Test_onModelChangeEntryMustBeAddeToDB(DatabaseTestCase):
        
    def test_create(self):
        self.assert_create(ModelChange, full_name='test')
    
    def test_read(self):
        ModelChange.objects.create(full_name='test12345')
        self.assert_read(ModelChange, full_name='test12345')
        
    def test_update(self):
        MC = ModelChange(full_name='test12345')
        MC.save()
        self.assert_update(MC, full_name='test54321')

