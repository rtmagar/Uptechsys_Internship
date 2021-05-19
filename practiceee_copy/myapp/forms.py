from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='description')
    image = forms.FileField()
