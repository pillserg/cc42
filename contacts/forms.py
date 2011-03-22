from django import forms
from django.forms.widgets import DateInput
from django.forms.extras.widgets import SelectDateWidget
import cc42.settings as settings


from cc42.contacts.models import UserDetail

class CalendarWidget(forms.TextInput):

    class Media:
        js = ('/admin/jsi18n/',
              settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'})

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        widgets = {
            'date_of_birth':CalendarWidget(),
        }
        


