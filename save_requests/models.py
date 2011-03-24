from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class SavedRequest(models.Model):
    # Request infomation
    method = models.CharField(default='GET', max_length=7)
    path = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(default=0)
    # User infomation
    ip = models.IPAddressField()
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='user')
    referer = models.URLField(verify_exists=False, max_length=255,
                              blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'saved_request'
        verbose_name_plural = 'saved_requests'
        ordering = ['-time',]
    
    def __unicode__(self):
        return (u'request from %s to "%s" method %s at %s, priority: %s' %
                    (self.ip, self.path, self.method,
                     self.time.strftime('%Y-%m-%d %H:%M:%S'), self.priority))
    from datetime import datetime
    
    def from_http_request(self, request, commit=True, priority=0):
        # Request infomation
        self.method = request.method
        self.path = request.path
        # User infomation
        self.ip = request.META.get('REMOTE_ADDR', '')
        self.referer = request.META.get('HTTP_REFERER', '')[:255]
        self.user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
        self.language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')[:255]
        
        if getattr(request, 'user', False):
            if request.user.is_authenticated():
                self.user = request.user
        if priority != 0:
            self.priority = priority
        
        if commit:
            self.save()
    