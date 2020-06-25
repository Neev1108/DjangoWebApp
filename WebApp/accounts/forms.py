from django import forms
from .import models

class CreateAccount(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['balance', 'type']

