from django import forms
from twitter.models import Twit

class TwitForm(forms.ModelForm):
    class Meta:
        model = Twit
        fields = ['content', 'parent']