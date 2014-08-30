from django.db import models

class alumni(models.Model):
	emailid = models.EmailField()
	password = models.CharField(max_length =100)

