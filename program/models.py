from django.db import models

class alumni(models.Model):
	firstname = models.CharField(max_length =100)
	lastname = models.CharField(max_length =100)
	password = models.CharField(max_length = 100)
	emailid = models.EmailField()
	password = models.CharField(max_length =100)
	contactnumber = models.CharField(max_length =15)
	organization = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)

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
	department = models.ForeignKey(departments)
	cgpa = models.DecimalField(max_digits = 3,decimal_places=2)
	interest1 = models.ForeignKey(interest,related_name = 'studentpreferences_interest1',null = True)
	interest2 = models.ForeignKey(interest,related_name = 'studentpreferences_interest2',null = True)
	interest3 = models.ForeignKey(interest,related_name = 'studentpreferences_interest3',null = True)
	interest4 = models.ForeignKey(interest,related_name = 'studentpreferences_interest4',null = True)
	mentorid1 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid1',null=True)
	mentorid2 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid2',null=True)
	mentorid3 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid3',null=True)
	mentorid4 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid4',null=True)
	mentorid5 = models.ForeignKey(alumni,related_name = 'studentpreferences_mentorid5',null=True)


class alumnipreferences(models.Model):
	id = models.ForeignKey(alumni,primary_key = True)

	department = models.ForeignKey(departments,related_name='alumnipreferences_department')
	interest = models.ForeignKey(interest,related_name='alumnipreferences_interest')
	noofmentees = models.IntegerField()
	