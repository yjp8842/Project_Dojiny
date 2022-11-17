from django import forms
from .models import Behind, Comment

class BehindForm(forms.ModelForm):

    class Meta:
        model = Behind
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=50,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Comment
        fields = [
        'content',
        ]