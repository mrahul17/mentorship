from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from program.forms import Login,Register
from program.models import *

def home(request):
	template = render_to_string('home.html')
	return HttpResponse(template)

def login(request):
	if request.method == 'GET':
		form = Login()
		return render(request,'login.html',{'form':form})
		
	else:
		response = HttpResponse()
		form = Login(request.POST)
		if form.is_valid():
			emailid = form.cleaned_data['emailid']
			password = form.cleaned_data['password']

			try:
				user = alumni.objects.get(emailid = emailid).firstname or students.objects.get(emailid=emailid)
				response.write('User Found in database')
			except alumni.DoesNotExist and students.DoesNotExist:
				user = None
				response.write('User Not Found')
			
			return response



def register(request):
	response = HttpResponse()
	if request.method == 'GET':
		form = Register()
		return render(request,'register.html',{'form':form})
	else:
		form = Register(request.POST)
		if form.is_valid():	
			password = form.cleaned_data['password']
			repassword = form.cleaned_data['repassword']
			if password!=repassword:
				return render(request,'register.html',{'form':form,'msg':'Passwords do not match'})

			else:	
				member = form.cleaned_data['member']
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				emailid = form.cleaned_data['emailid']
				contactnumber =form.cleaned_data['contactnumber']
				if member == 'alumni':
					alumni1 = alumni(firstname = firstname,lastname = lastname,emailid = emailid,password = password,contactnumber = contactnumber)
					alumni1.save()
					alum = alumni.objects.all()
				if member == 'student':
					student1 = students(firstname = firstname,lastname = lastname,emailid = emailid,password = password,contactnumber = contactnumber)
					student1.save()
					student = students.objects.all()
				response.write("dude you have registered")
				return response
		else:	
			errors = form.errors
			return render(request,'register.html',{'form':form,'msg':"errors"})
