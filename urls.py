from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

from cc42.contacts.views import show_main_page, show_edit_contacts_page
from cc42.save_requests.views import show_last_requests
from cc42 import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', show_main_page, name='show_main_page'),
    url(r'^last-requests/$',show_last_requests, name='show_last_requests'),
    url(r'^edit-contacts/$',show_edit_contacts_page, name='show_edit_contacts'),
    url(r'^last-requests/by-priority$',
        show_last_requests,
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