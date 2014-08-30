from django import forms

class Login(forms.Form):
	emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name','autofocus':'autofocus'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')
