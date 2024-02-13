from .models import Comment
from django.forms import ModelForm, HiddenInput, TextInput
from django import forms


class CommentForm(forms.Form):
    nickname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your nickname'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your comment'}))


'''class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'content']

        widgets = {

            'nickname': TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'Nickname',
                                         'required': False}),
            'content': TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Your message',
                                        'required': True})
        }
'''
