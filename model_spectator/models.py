from django.db import models

# Create your models here.
class ModelChange(models.Model):
    CHOICES = (
                ('1', 'Created_or_Updated'),
                ('2', 'Deleted'),
              )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ['-timestamp',]
    def __unicode__(self):
        return u'%s was %s at %s' % (self.name, self.status, self.timestamp)