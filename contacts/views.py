from django.shortcuts import render_to_response, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse

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
    if request.method == 'POST':
        form = UserDetailForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_main_page'))
        else:
            form = UserDetailForm(request.POST, instance=contacts)
<<<<<<< HEAD
            context = {
                       'contacts':contacts,
                       'form':form,
                       }
            return render_to_response('edit-contacts.html',
                                      context,
                                      context_instance =
                                      RequestContext(request))
        
    form = UserDetailForm(instance=contacts)
    context = {
        'contacts':contacts,
        'form':form,
    }
    return render_to_response('edit-contacts.html',
                              context,
                              context_instance = RequestContext(request))

=======
    else:
        form = UserDetailForm(instance=contacts)
    
    context = {'contacts':contacts,'form':form}
    return render_to_response('edit-contacts.html',
                        context_instance = RequestContext(request, context))
    
>>>>>>> t7_form_reverse_redo
