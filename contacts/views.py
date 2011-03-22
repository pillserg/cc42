from django.shortcuts import render_to_response, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from cc42.contacts.models import UserDetail
from cc42.contacts.forms import UserDetailForm

def showMainPage(request):
    context = {
        'contacts':UserDetail.objects.all()[0]
            }
    return render_to_response('mainpage.html',
                              context,
                              context_instance=RequestContext(request))
@login_required
def showEditContactsPage(request):
    contacts = get_object_or_404(UserDetail, id=1)
    if request.method == 'POST':
        form = UserDetailForm(request.POST, instance=contacts)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
        
    form = UserDetailForm(instance=contacts)    
    context = {
        'contacts':contacts,
        'form':form,
        'fields_left':['name','last_name', 'date_of_birth', 'form.bio',],
        'fields_right':['email','jabber','contacts','skype','other_contacts',]
        
            
    }
    return render_to_response('edit-contacts.html',
                              context,
                              context_instance = RequestContext(request))
    
