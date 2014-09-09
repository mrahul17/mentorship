from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from program.forms import Login,Register
from program.models import *

def home(request):
	template = render_to_string('home.html')
	return HttpResponse(template)

def login(request):
	userid = ''
	firstname = ''
	if request.method == 'GET':
		form = Login()
		return render(request,'login.html',{'form':form})
		
	elif request.method == 'POST':
		response = HttpResponse()
		form = Login(request.POST)
		response.write('jfnn222')	
		response.write(form.is_valid())
		if (form.is_valid()):
			emailid = form.cleaned_data['emailid']
			password = form.cleaned_data['password']
			membertype = form.cleaned_data['member']
			if membertype=='student':
				try:
					userid1 = students.objects.filter(emailid = emailid)[:1].values()[0]['id']
					firstname = students.objects.filter(emailid = emailid)[:1].values()[0]['firstname']
				except students.DoesNotExist:
					userid1 = None
			elif membertype =='alumni':		
				try:
					userid1 = alumni.objects.filter(emailid = emailid)
				except alumni.DoesNotExist:
					userid1 = None

			
			if userid1:
				request.session['id'] = userid1
				request.session['firstname'] = firstname
				return showProfile(request,userid1,membertype)
				
				#return render(request,'profile.html',{'firstname':request.session['firstname'],'msg':response})
				
				#return response
			elif userid1==None:
				
				return response
		else:
			response.write('Error')	

		for error in form.errors:
			response.write(error)
		
		return response	



def register(request):
	response = HttpResponse()
	user = ''
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
					try:
						user = alumni.objects.get(emailid = emailid)
					except alumni.DoesNotExist:
						user = None
					if user!=None:
						return render(request,'register.html',{'form':form,'msg':'This emailid id already exists'})
					else:
						
						#render(request,'register.html',{'form':form,'msg':'This email id already exists'})
						alumni1 = alumni(firstname = firstname,lastname = lastname,emailid = emailid,password = password,contactnumber = contactnumber)
						alumni1.save()
						alum = alumni.objects.all()
				elif member == 'student':
					try:
						user = students.objects.get(emailid = emailid)
					except students.DoesNotExist:
						user = None
					if user!=None :
						return render(request,'register.html',{'form':form,'msg':'This email id already exists'})

					else:	
						student1 = students(firstname = firstname,lastname = lastname,emailid = emailid,password = password,contactnumber = contactnumber)
						student1.save()
				return render(request,'home.html',{'msg':'Congrats, You have successfully registered,you can login now.'})
		else:	
			errors = form.errors
			return render(request,'register.html',{'form':form,'msg':"Please see the errors: ",'errors':errors})

def editProfile(request):
	from program.forms import EditProfile
	form = EditProfile(request.POST)
	if form.is_valid():	
		department = form.cleaned_data['department']
		cgpa = form.cleaned_data['cgpa']
		interest1 = form.cleaned_data['interest1']
		interest2 = form.cleaned_data['interest2']
		interest3 = form.cleaned_data['interest3']
		interest4 = form.cleaned_data['interest4']
		preference = studentpreferences(department=department,cgpa=cgpa,interest1=interest1,interest2=interest2,interest3=interest3,interest4=interest4) 
		preference.save()
		return render(request,'home.html',{'msg':'Your preferences have been saved'})
	else:
		errors = form.errors
		return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form,'msg':'Please see the errors','errors':errors })

def showProfile(request,userid1,membertype):
	if membertype=='student':
		try:
			preferences = studentpreferences.objects.get(id = 1)
		except studentpreferences.DoesNotExist:
			from program.forms import EditProfile
			form = EditProfile()
			return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form})
		
		#return render(request,'profile.html',{'preferences':preferences,'msg':'Fool Ya Fool'})
