#forms.py

from django import forms



class URLForm(forms.Form):
	url = forms.URLField(label='Enter a Job Link', max_length=200)