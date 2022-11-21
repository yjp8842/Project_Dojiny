from django import forms
from .models import VoteMovie

class VoteForm(forms.ModelForm):

    class Meta:
        model = VoteMovie
        fields = ('vote',)