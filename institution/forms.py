from django import forms

class InstituteForm(forms.Form):
    token = forms.CharField(max_length=50)
    