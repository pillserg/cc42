from tddspry import NoseTestCase
from tddspry.django import HttpTestCase

from django.template import Template, Context, RequestContext
from django.http import HttpRequest
from django.shortcuts import render_to_response

from cc42.settings import MEDIA_URL


class TestDjangoSettingsContextProcessor(NoseTestCase):
    def test_it(self):
        request = HttpRequest()
        print request
        context = {}
        res = str(render_to_response('test.html',
                              context,
                              context_instance=RequestContext(request)))
        self.find_in(MEDIA_URL, res)


class TestAuth(HttpTestCase):
    
    def test_login(self):
        self.login('admin','admin', url='accounts/login/', formid=0)

    def test_logout(self):
        self.logout(url='accounts/logout/')
    
    
        
