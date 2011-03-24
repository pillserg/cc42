from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from cc42.save_requests.models import SavedRequest
from cc42.save_requests.forms import PriorityChangeForm

def show_last_requests(request, sort_by='time'):
    
    if sort_by == 'priority':
        last_requests = SavedRequest.objects.order_by('-priority','time')[:10]
    elif sort_by == '-priority':
        last_requests = SavedRequest.objects.order_by('priority','time')[:10]
    else:
        last_requests = SavedRequest.objects.all()[:10]
        
        
    for req in last_requests:
            setattr(req, 'assigned_form', PriorityChangeForm())
            
    if request.method == 'POST':
        submited_request = last_requests[int(request.POST['form_num'])]
        setattr(submited_request, 'assigned_form',
                PriorityChangeForm(request.POST))
        form = submited_request.assigned_form
        if form.is_valid():
            cd = form.cleaned_data
            if cd['for_all_by_ip'] == True and cd['for_all_by_path'] == True:
                SavedRequest.objects.filter(ip=request.POST['request_ip'],
                    path =request.POST['request_path']).update(priority = cd['priority'])
            elif  form.cleaned_data['for_all_by_ip'] == True:
                SavedRequest.objects.filter(ip=request.POST
                        ['request_ip']).update(priority = cd['priority'])
            elif form.cleaned_data['for_all_by_path'] == True:
                SavedRequest.objects.filter(path=request.POST
                        ['request_path']).update(priority = cd['priority'])
            else:
                SR = SavedRequest.objects.get(id=int(request.POST
                        ['request_id']))
                SR.priority = cd['priority']
                SR.save()
           
            return HttpResponseRedirect(reverse('show_last_requests'))
            
        else:
            setattr(submited_request, 'assigned_form',
                PriorityChangeForm(request.POST))
            
    context = {'requests':last_requests}
    return render_to_response('last_requests.html',
                              context_instance=RequestContext(request, context))