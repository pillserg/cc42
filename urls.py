from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

from cc42.contacts.views import showMainPage, showEditContactsPage
from cc42.save_requests.views import showLast10requests
from cc42 import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', showMainPage, name='show_main_page'),
    url(r'^last-requests/$',showLast10requests, name='show_last_requests'),
    url(r'^edit-contacts/$',showEditContactsPage, name='show_edit_contacts'),
    url(r'^last-requests/by-priority$',
        showLast10requests,
        {'sort_by':'priority'},
        name='show_last_requests_by_priority'),
    
    
    #auth
    url(r'^accounts/login/$',
        auth_views.login,
        {'template_name': 'login.html'},
        name='auth_login'),
    url(r'^accounts/logout/$',
        auth_views.logout,
        {'template_name': 'logout.html',
         'next_page':'/'},
        name='auth_logout'),
    
    
    
)

urlpatterns += patterns('',
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )