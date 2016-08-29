from django.forms import ModelForm
from models import *


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

    def save(self, commit=True):
        contact_form = super(ContactUsForm, self).save(commit=False)
        contact_form.name = self.cleaned_data.get('name')
        contact_form.email = self.cleaned_data.get('email')
        contact_form.message = self.cleaned_data.get('message')

        if commit:
            self.save()
        return contact_form
