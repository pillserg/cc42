from django.shortcuts import render_to_response
from django.template import RequestContext

from cc42.save_requests.models import SavedRequest
from cc42.save_requests.forms import PriorityChangeForm

def show_last_requests(request, sort_by='time'):
    
    if sort_by == 'priority':
        last_requests = SavedRequest.objects.order_by('-priority','time')[:10]
    elif sort_by == '-priority':
        last_requests = SavedRequest.objects.order_by('priority','time')[:10]
    else:
        last_requests = SavedRequest.objects.all()[:10]
        
    
    if request.method == 'POST':
        for req in last_requests:
            setattr(req, 'assigned_form', PriorityChangeForm(request.POST))
        assert False        
    else:
        for req in last_requests:
            setattr(req, 'assigned_form', PriorityChangeForm())
    
    
    
    context = {'requests':last_requests}
    return render_to_response('last_requests.html',
                              context_instance=RequestContext(request, context))