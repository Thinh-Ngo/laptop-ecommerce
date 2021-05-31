from django import forms
from tinymce import TinyMCE
from .models import Help, PolicyContent


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PolicyForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10, }
        )
    )

    class Meta:
        model = PolicyContent
        fields = ('from_date', 'to_date', 'content')


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = '__all__'
