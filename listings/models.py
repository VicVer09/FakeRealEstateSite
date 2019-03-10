from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
	
	### LISTING
	realtor = models.ForeignKey(Realtor, on_delete= models.DO_NOTHING)
	title = models.CharField(max_length = 200) 
	address = models.CharField(max_length = 200)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 20)
	zipcode = models.CharField(max_length = 200) 
	description = models.TextField(blank = True) #: TEXT
	price = models.IntegerField() #: INT
	bedrooms = models.IntegerField() #: INT
	bathrooms = models.DecimalField(max_digits = 2, decimal_places = 1) #: INT
	garage = models.IntegerField(default = 0) #: INT [0]
	sqft = models.IntegerField() #: INT
	lot_size = models.DecimalField(max_digits = 5, decimal_places = 1) #: FLOAT
	photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/') #: STR # blank = True allows it to be optional
	photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) #: STR
	is_published = models.BooleanField(default = True) #: BOOL [true]
	list_date = models.DateTimeField(default=datetime.now, blank = True) #: DATE

	def __str__(self):
		return self.title

