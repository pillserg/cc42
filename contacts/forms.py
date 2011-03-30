from django import forms
from django.forms.widgets import DateInput

import cc42.settings as settings
from cc42.contacts.models import UserDetail

class CalendarWidget(forms.TextInput):

    class Media:
        js = (settings.MEDIA_URL + "js/jquery.js",
              settings.MEDIA_URL + "js/jquery.form.js",
              settings.MEDIA_URL + "js/datepicker/jquery-ui-1.8.11.custom.min.js",
        )
        css = {
            'all': (settings.MEDIA_URL +
                    "css/datepicker/jquery-ui-1.8.11.custom.css",)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(
            attrs={'class': 'vDateField', 'size': '10'}
            )


class UserDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        #fields reversion
        self.fields.keyOrder.reverse()

    class Meta:
        model = UserDetail

        widgets = {
            'date_of_birth':CalendarWidget(),
        }
        
    

