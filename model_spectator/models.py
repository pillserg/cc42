from django.db import models
from django.db.models.signals import post_save, post_delete

# Create your models here.
class ModelChange(models.Model):
    CHOICES = (
                ('1', 'Created'),
                ('2', 'Updated'),
                ('3', 'Deleted')
              )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ['-timestamp',]
        
    def __unicode__(self):
        return u'%s was %s at %s' % (self.name,
                                     self.get_status_display(),
                                     self.timestamp)
        

def add_db_entry_on_model_save(sender, **kwargs):
    if kwargs['created']:
        status = '1'
    else:
        status = '2'
    instance = kwargs['instance']
    if instance.__class__ != ModelChange and \
                             'django.' not in str(instance.__class__):
        ModelChange.objects.create(name=str(kwargs['instance']), status=status)

def add_db_entry_on_model_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.__class__ != ModelChange and \
                             'django.' not in str(instance.__class__):
        ModelChange.objects.create(name=str(kwargs['instance']), status='3')

post_save.connect(add_db_entry_on_model_save)
post_delete.connect(add_db_entry_on_model_delete)
