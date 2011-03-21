from django.conf.urls.defaults import *
from django.contrib import admin

from cc42.contacts.views import showMainPage
from cc42.save_requests.views import showLast10requests

admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', showMainPage, name='show_main_page'),
    url(r'^last-requests/$',showLast10requests, name='show_last_requests')
    

    
)
