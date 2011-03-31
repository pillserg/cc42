from django.shortcuts import render_to_response, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.http import HttpResponse
from django.template.loader import render_to_string

from cc42.contacts.models import UserDetail
from cc42.contacts.forms import UserDetailForm

def show_main_page(request):
    context = {
        'contacts':UserDetail.objects.all()[0]
            }
    return render_to_response('mainpage.html',
                        context_instance=RequestContext(request,context))

@login_required
def show_edit_contacts_page(request):
    contacts = get_object_or_404(UserDetail, id=1)
    if request.method == 'POST' and request.is_ajax():
        form = UserDetailForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
        response_text = render_to_string("edit-ajax-resp.html",
                                context_instance = RequestContext(request,
                                                          {'form': form}))
        return HttpResponse(response_text, mimetype='application/javascript')
        
    # left for old tests and users with disabled js
    elif request.method == 'POST' and not request.is_ajax():
        form = UserDetailForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            
    else:
        form = UserDetailForm(instance=contacts)
    
    context = {'contacts': contacts, 'form': form}
    return render_to_response('edit-contacts.html',
                        context_instance = RequestContext(request, context))
    
    
    
    
