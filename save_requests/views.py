# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from cc42.save_requests.models import SavedRequest

def showLast10requests(request):
    context = {
        'requests':SavedRequest.objects.all()[:10]
            }
    return render_to_response('last_requests.html',
                              context,
                              context_instance=RequestContext(request))