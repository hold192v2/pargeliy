from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 5,
            'cols': 50
        }))

    class Meta:
        model = Comment
        fields = ['content']