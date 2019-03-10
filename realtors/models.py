from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
	
	### REALTOR 
	name = models.CharField(max_length = 200)#: STR
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')#: STR
	description = models.TextField(blank = True)#: TEXT
	phone = models.CharField(max_length = 20)#: STR
	email = models.CharField(max_length = 50)#: STR
	is_mvp = models.BooleanField(default = False)#: BOOL [false]
	hire_date = models.DateTimeField(default=datetime.now, blank = True) #: DATE
	
	
	def __str__(self):
		return self.name