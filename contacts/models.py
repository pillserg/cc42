from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=100)
    jabber = models.EmailField(max_length=100)
    skype = models.CharField(max_length=100)
    other_contacts = models.TextField()
    
    def __unicode__(self):
        return ' '.join((self.name, self.last_name))