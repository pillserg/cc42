from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=100, verbose_name='first name')
    last_name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    jabber = models.EmailField(max_length=100)
    skype = models.CharField(max_length=100)
    other_contacts = models.TextField()
    bio = models.TextField()
    date_of_birth = models.DateField()
    
    def __unicode__(self):
        return ' '.join((self.name, self.last_name))