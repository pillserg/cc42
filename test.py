from tddspry.django import HttpTestCase

from django.template import Template, Context, RequestContext
from django.http import HttpRequest
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse

class TestDjangoSettingsContextProcessor(HttpTestCase):
    def test_it(self):
        self.go(reverse('show_main_page'))
        self.find(settings.MEDIA_URL)
        self.find(settings.TIME_ZONE)
        

class TestAuth(HttpTestCase):
    
    def test_login(self):
        self.login('admin','admin', url='accounts/login/', formid=0)

    def test_logout(self):
        self.logout(url='accounts/logout/')
    
    
        
