from django import forms

class PriorityChangeForm(forms.Form):
    priority = forms.IntegerField()
    for_all_by_ip = forms.BooleanField()
    for_all_by_path = forms.BooleanField()