from django import forms

class ScrapForm(forms.Form):

    hidden = forms.HiddenInput()