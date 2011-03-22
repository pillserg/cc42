# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from cc42.save_requests.models import SavedRequest

def showLast10requests(request, sort_by='time'):
    
    if sort_by == 'priority':
        last_requests = SavedRequest.objects.order_by('-priority','time')[:10]
    else:
        last_requests = SavedRequest.objects.all()[:10]
    context = {
        'requests':last_requests
            }
    return render_to_response('last_requests.html',
                              context,
                              context_instance=RequestContext(request))