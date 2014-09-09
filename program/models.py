from django.db import models

class alumni(models.Model):
	firstname = models.CharField(max_length =100)
	lastname = models.CharField(max_length =100)
	password = models.CharField(max_length = 100)
	emailid = models.EmailField()
	password = models.CharField(max_length =100)
	contactnumber = models.CharField(max_length =15)

class students(models.Model):
	firstname = models.CharField(max_length =100)
	lastname = models.CharField(max_length =100)
	password = models.CharField(max_length = 100)
	emailid = models.EmailField()
	password = models.CharField(max_length =100)
	contactnumber = models.CharField(max_length =15)

class departments(models.Model):
	department = models.CharField(max_length=100) 

class interest(models.Model):
	interest = models.CharField(max_length = 100)	

class studentpreferences(models.Model):
	id = models.ForeignKey(students,primary_key = True)
	department = models.CharField(max_length =100)
	cgpa = models.DecimalField(max_digits = 3,decimal_places=2)
	interest1 = models.CharField(max_length=100)	
	interest2 = models.CharField(max_length=100)
	interest3 = models.CharField(max_length=100)
	interest4 = models.CharField(max_length=100)
	mentorid1 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid1',null=True)
	mentorid2 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid2',null=True)
	mentorid3 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid3',null=True)
	mentorid4 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid4',null=True)
	mentorid5 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid5',null=True)


