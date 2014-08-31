from django import forms

class Login(forms.Form):
	emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id','autofocus':'autofocus'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')

class Register(forms.Form):

	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','autofocus':'autofocus'}),label='')
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),label='')
	emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype Password'}),label='')
	contactnumber = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Number'}),label='')
	member = forms.ChoiceField(choices=[('student','student'),('alumni','alumni')],widget = forms.Select(attrs={'placeholder':'Login as','class':'form-control'}),label='')