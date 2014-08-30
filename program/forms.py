from django import forms

class Login(forms.Form):
	emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name','autofocus':'autofocus'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')

class Regsiter(forms.Form):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),'placeholder':'First Name')
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),'placeholder':'Last Name')
	emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name','autofocus':'autofocus'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype Password'}),label='')