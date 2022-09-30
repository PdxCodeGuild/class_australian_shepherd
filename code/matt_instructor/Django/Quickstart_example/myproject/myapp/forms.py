from django import forms

from .models import MyModel

class PostForm(forms.ModelForm):

    class Meta:
        model = MyModel
        fields = ('myfield', 'author',)