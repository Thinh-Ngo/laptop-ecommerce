from .models import Client
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('profile_picture', 'full_name')
