from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from program.forms import Login,Register
from program.models import *
from django.http import HttpResponseRedirect

def home(request):
	if 'firstname' not in request.session:
		request.session['firstname'] = "Guest"
	return render(request,'home.html',{'firstname':request.session['firstname']})

def accessCheck(request):
	if 'id' not in request.session:
		return 0
	else:
		return 1

def login(request):
	result = accessCheck(request)
	if result==1:
 	   return HttpResponseRedirect("dashboard")

	userid = ''
	firstname = ''
	if request.method == 'GET':
		form = Login()
		return render(request,'login.html',{'form':form})
		
	elif request.method == 'POST':
		response = HttpResponse()
		form = Login(request.POST)
		if (form.is_valid()):
			emailid = form.cleaned_data['emailid']
			password = form.cleaned_data['password']
			membertype = form.cleaned_data['member']
			if membertype=='student':
				try:
					userid1 = students.objects.get(emailid = emailid).id
					firstname = students.objects.get(emailid = emailid).firstname
				except students.DoesNotExist:
					userid1 = None
			elif membertype =='alumni':		
				try:
					userid1 = alumni.objects.get(emailid = emailid).id
					firstname = alumni.objects.get(emailid = emailid).firstname
				except alumni.DoesNotExist:
					userid1 = None

			
			if userid1:
				request.session['id'] = userid1
				request.session['firstname'] = firstname
				request.session['membertype'] = membertype
				return showProfile(request)
				
				#return render(request,'profile.html',{'firstname':request.session['firstname'],'msg':response})
				
				#return response
			elif userid1==None:
				
				return render(request,'home.html',{'msg' :'Username Password combination incorrect'})
		else:
			response.write('Error')	

		for error in form.errors:
			response.write(error)
		
		return response	



def register(request):
	result = accessCheck(request)
	if result==1:
 	   return HttpResponseRedirect("dashboard")
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
	result = accessCheck(request)
	if result==0:
 	   return HttpResponseRedirect("home")
	from program.forms import EditStudentProfile, EditAlumniProfile
	from program.models import interest
	form = ''
	if request.method=='GET' and request.session['membertype']=="student":
		try:
			filleddata = studentpreferences.objects.get(id = students.objects.get(id = request.session['id']))
			form = EditStudentProfile({'department':filleddata.department.id,'cgpa':filleddata.cgpa,'interest1':filleddata.interest1.id,'interest2':filleddata.interest2.id,'interest3':filleddata.interest3.id,'interest4':filleddata.interest4.id})
		except studentpreferences.DoesNotExist:
			form = EditStudentProfile()
		return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form,'msg':''})
	if request.method=='GET' and request.session['membertype']=="alumni":
		try:
			filleddata = alumnipreferences.objects.get(id = alumni.objects.get(id = request.session['id']))
			filleddata2 = alumni.objects.get(id=request.session['id'])
			form = EditAlumniProfile({'department':filleddata.department.id,'interest':filleddata.interest.id,'noofmentees':filleddata.noofmentees,'organization':filleddata2.organization,'designation':filleddata2.designation})
		except alumnipreferences.DoesNotExist:
			form = EditAlumniProfile()
		return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form,'msg':''})

	else:
		if request.session['membertype']=='student':
			form = EditStudentProfile(request.POST)
			if form.is_valid():	
				interest1 = interest.objects.get(id = form.cleaned_data['interest1'])
				interest2 = interest.objects.get(id = form.cleaned_data['interest2'])
				interest3 = interest.objects.get(id = form.cleaned_data['interest3'])
				interest4 = interest.objects.get(id = form.cleaned_data['interest4'])
				department = departments.objects.get(id =form.cleaned_data['department'])
				cgpa = form.cleaned_data['cgpa']
				obj = students.objects.get(id = request.session['id'])
				try:
					preference = studentpreferences.objects.get(id = obj)
					preference.department = department
					preference.interest1 = interest1
					preference.interest2 = interest2
					preference.interest3 = interest3
					preference.interest4 = interest4
					preference.cgpa = cgpa
					preference.save()
				except studentpreferences.DoesNotExist:
					preference = studentpreferences(id =obj, department=department,cgpa=cgpa,interest1=interest1,interest2=interest2,interest3=interest3,interest4=interest4) 
					preference.save()
				return render(request,'home.html',{'msg':'Your preferences have been updated.'})
			else:
				errors = form.errors
				return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form,'msg':'Please see the errors','errors':errors })
		else:
			form = EditAlumniProfile(request.POST)
			if form.is_valid():	
				department = departments.objects.get(id =form.cleaned_data['department'])
				interest = interest.objects.get(id = form.cleaned_data['interest'])	
				noofmentees = form.cleaned_data['noofmentees']	
				organization = form.cleaned_data['organization']
				designation = form.cleaned_data['designation']	
				obj = alumni.objects.get(id = request.session['id'])
				try:
					preference = alumnipreferences.objects.get(id=obj)
					preference.department = department
					preference.interest = interest
					preference.noofmentees = noofmentees
					preference.save()
				except alumnipreferences.DoesNotExist:
					preference = alumnipreferences(id =obj, department=department,interest=interest,noofmentees = noofmentees) 
					preference.save()
					
				alumni.objects.filter(id = request.session['id']).update(designation = designation,organization=organization)

				return render(request,'home.html',{'msg':'Your preferences have been updated.'})
			else:
				errors = form.errors
				return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form,'msg':'Please see the errors','errors':errors })

def showProfile(request):
	result = accessCheck(request)
	if result==0:
 	   return HttpResponseRedirect("home")
	userid1 = request.session['id']
	membertype = request.session['membertype']
	preferences = {}
	if membertype=='student':
		try:
			preferences = studentpreferences.objects.get(id = userid1)
		except studentpreferences.DoesNotExist:
			from program.forms import EditStudentProfile
			form = EditStudentProfile()
			return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form})
		
		return render(request,'profile.html',{'preferences':preferences,'msg':'','membertype':membertype,'firstname':request.session['firstname']})

	elif membertype=='alumni':
		try:
			preferences = alumnipreferences.objects.get(id = userid1)
		except alumnipreferences.DoesNotExist:
			from program.forms import EditAlumniProfile
			form = EditAlumniProfile()
			return render(request,'editProfile.html',{'firstname':request.session['firstname'],'form':form})
		
		return render(request,'profile.html',{'preferences':preferences,'msg':'','membertype':membertype,'firstname':request.session['firstname']})

def mentorlist(request,suggest="off"):
	result = accessCheck(request)
	if result==0:
 	   return HttpResponseRedirect("home")
	response = HttpResponse()
	al1=[]
	al2=[]
	al3=[]
	al4=[]
	match = ''
	userid = request.session['id']
	user = students.objects.get(id=userid)
	preference=''
	if suggest=="off":
		try:
			preference = studentpreferences.objects.get(id =user )

		except studentpreferences.DoesNotExist:
			preference = None

	
		if preference:
		#response.write("We have your preference stored")
			interest1 = preference.interest1
			interest2 = preference.interest2
			interest3 = preference.interest3
			interest4 = preference.interest4
		
			match1 = alumnipreferences.objects.filter(interest = interest1).values('id','department','interest')
			match2 = alumnipreferences.objects.filter(interest = interest2).values('id','department','interest')
			match3 = alumnipreferences.objects.filter(interest = interest3).values('id','department','interest')
			match4 = alumnipreferences.objects.filter(interest = interest4).values('id','department','interest')
			if match1:
				for match in match1:
					alum = alumni.objects.get(id = match['id'])
					match['department'] = departments.objects.get(id=match['department']).department
					match['interest'] = interest.objects.get(id=match['interest']).interest
					match['organization'] = alum.organization
					match['designation'] = alum.designation
					al1.append([match['id'],match['department'],match['interest'],match['organization'],match['designation']])
			if match2:
				for match in match2:
					alum = alumni.objects.get(id = match['id'])
					match['department'] = departments.objects.get(id=match['department']).department
					match['interest'] = interest.objects.get(id=match['interest']).interest
					match['organization'] = alum.organization
					match['designation'] = alum.designation
					al2.append([match['id'],match['department'],match['interest'],match['organization'],match['designation']])

			if match3:
				for match in match3:
					alum = alumni.objects.get(id = match['id'])
					match['department'] = departments.objects.get(id=match['department']).department
					match['interest'] = interest.objects.get(id=match['interest']).interest
					match['organization'] = alum.organization
					match['designation'] = alum.designation
					al3.append([match['id'],match['department'],match['interest'],match['organization'],match['designation']])

			if match4:
				for match in match4:
					alum = alumni.objects.get(id = match['id'])
					match['department'] = departments.objects.get(id=match['department']).department
					match['interest'] = interest.objects.get(id=match['interest']).interest
					match['organization'] = alum.organization
					match['designation'] = alum.designation	
					al4.append([match['id'],match['department'],match['interest'],match['organization'],match['designation']])
			return render(request,'mentorlist.html',{'match1':al1,'match2':al2,'match3':al3,'match4':al4})
		else:
			response.write("Boo")
			response.write(preference)
		return response

	else:
		pass

def dashboard(request):
	response = HttpResponse()
	response.write('this is dasg')
	return response

