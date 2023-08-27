#  from https://testdriven.io/blog/django-mailchimp
from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(label='',
                             max_length=128)
