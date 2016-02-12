from django import forms
from .models import Post

class DriverForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	id_start = forms.CharField(max_length=500)
	id_end = forms.CharField(max_length=500)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PostForm(forms.ModelForm):
	class Meta:
	    model = Post
	    fields = ('title', 'text',)