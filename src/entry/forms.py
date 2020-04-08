from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            'first_name',
            'last_name',
            'email',
            'gender',
            'D_O_B',
            'street',
            'city',
            'state',
            'zipcode',
        ]