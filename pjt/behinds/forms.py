from django import forms
from .models import Behind

class BehindForm(forms.ModelForm):

    class Meta:
        model = Behind
        fields = ('title', 'content')