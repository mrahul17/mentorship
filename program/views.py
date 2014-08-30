from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string
from program.forms import Login
from program.models import *

def home(request):
	template = render_to_string('home.html')
	return HttpResponse(template)

def alumnilogin(request):
	if request.method == 'GET':
		form = Login()
		return render(request,'alumnilogin.html',{'form':form})
		
	else:
		response = HttpResponseRedirect()
		form = Login(request.POST)
		if form.is_valid():
			emailid = form.cleaned_data['emailid']
			password = form.cleaned_data['password']

			try:
				user = alumni.objects.get(emailid = emailid).emailid
			except alumni.DoesNotExist:
				user = None
			response.write('User Found in database')
			return response