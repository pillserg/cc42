from django.shortcuts import render_to_response
from django.template import RequestContext

from cc42.contacts.models import UserDetail

def showMainPage(request):
    context = {
        'contacts':UserDetail.objects.all()[0]
            }
    return render_to_response('mainpage.html',
                              context,
                              context_instance=RequestContext(request))
    