from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'my-form',
            'placeholder': 'Напишите о своём отношении к Арт-объекту!',
            'rows': 5,
            'cols': 50
        }))

    class Meta:
        model = Comment
        fields = ['content']