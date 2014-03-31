from django import forms


__author__ = 'nem'


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    sender = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': '4'}))

    cc_myself = forms.BooleanField(required=False)


