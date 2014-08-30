from django import forms

class Login(forms.Form):
	#emailid = forms.EmailField(attrs=	{'class':'form-control'},label='Email Id')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='assword')
