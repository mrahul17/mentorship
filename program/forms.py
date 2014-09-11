from django import forms
from program.models import *

class Login(forms.Form):
	emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id','autofocus':'autofocus'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')
	member = forms.ChoiceField(choices=[('student','student'),('alumni','alumni')],widget = forms.Select(attrs={'placeholder':'Login as','class':'form-control'}),label='')

class Register(forms.Form):

	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','autofocus':'autofocus'}),label='')
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),label='')
	emailid = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id'}),label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label='')
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype Password'}),label='')
	contactnumber = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Number'}),label='')
	member = forms.ChoiceField(choices=[('student','student'),('alumni','alumni')],widget = forms.Select(attrs={'placeholder':'Register as','class':'form-control'}),label='')

class EditStudentProfile(forms.Form):
	list1 = []
	list2 = []
	for department in departments.objects.all().values():
		list1.append(department.values()[::-1])
	for interesting in interest.objects.all().values():
		list2.append(interesting.values())
	department = forms.ChoiceField(choices =list1 ,widget=forms.Select(attrs={'class':'form-control','placeholder':'Department','autofocus':'autofocus'}),label='')
	cgpa = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CGPA'}),label='')
	interest1 = forms.ChoiceField(choices =list2 ,widget=forms.Select(attrs={'class':'form-control','placeholder':'1st Interest'}),label='')
	interest2 = forms.ChoiceField(choices =list2 ,widget=forms.Select(attrs={'class':'form-control','placeholder':'2nd Interest'}),label='')
	interest3 = forms.ChoiceField(choices =list2 ,widget=forms.Select(attrs={'class':'form-control','placeholder':'3rd Interest'}),label='')
	interest4 = forms.ChoiceField(choices =list2 ,widget=forms.Select(attrs={'class':'form-control','placeholder':'4th Interest'}),label='')

class EditAlumniProfile(forms.Form):
	list1 = []
	list2 = []
	for department in departments.objects.all().values():
		list1.append(department.values()[::-1])
	for interesting in interest.objects.all().values():
		list2.append(interesting.values())
	department = forms.ChoiceField(choices = list1,widget=forms.Select(attrs={'class':'form-control','placeholder':'Your Department at IIT Kgp','autofocus':'autofocus'}),label='')
	interest = forms.ChoiceField(choices = list2,widget=forms.Select(attrs={'class':'form-control','placeholder':'Area you would like to give guidance about'}),label='')
	noofmentees = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Mentees'}),label='')
	organization = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Company or organization'}),label='')
	designation = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),label='')