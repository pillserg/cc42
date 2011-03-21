from django.conf.urls.defaults import *
from django.contrib import admin

from cc42.contacts.views import showMainPage

admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', showMainPage)
)
