from django import forms
from django.forms.widgets import DateInput
from django.forms.extras.widgets import SelectDateWidget

from cc42.contacts.models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        #widgets = {
        #    'date_of_birth':SelectDateWidget(),
        #}