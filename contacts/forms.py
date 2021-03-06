from django import forms

from django.conf import settings
from cc42.contacts.models import UserDetail


class CalendarWidget(forms.TextInput):
    """date widget using datepicker from jQueryUI"""
    class Media:
        js = (settings.MEDIA_URL + "js/jquery.js",
              settings.MEDIA_URL + "js/jquery.form.js",
              # csrf token for AJAX POSTs
              settings.MEDIA_URL + "js/csrftoken.js",
              settings.MEDIA_URL + "js/initAjaxForm.js",
              settings.MEDIA_URL +
                "js/datepicker/jquery-ui-1.8.11.custom.min.js",
              settings.MEDIA_URL + "js/datepicker_init.js",
        )
        css = {
            'all': (settings.MEDIA_URL +
                    "css/datepicker/jquery-ui-1.8.11.custom.css",)}

    def __init__(self, attrs={}):
        """init super widget"""
        super(CalendarWidget, self).__init__(
            attrs={'class': 'vDateField', 'size': '10'})


class UserDetailForm(forms.ModelForm):
    """ModelForm for editing user details"""
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        #fields reversion
        self.fields.keyOrder.reverse()

    class Meta:
        model = UserDetail
        widgets = {
            'date_of_birth': CalendarWidget(),
        }
