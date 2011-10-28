from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	)
	
PAYMENT_METHOD_CHOICES = (
	('1', 'Cheque'),
	('2', 'Credit Card'),
	('3', 'Net Banking'),
	('4', 'Cash'),
	)
	
class UserProfile(models.Model):
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	date_of_birth = models.DateField(blank=True, null=True)
	batch = models.IntegerField(blank=True, null=True)
	occupation = models.CharField(max_length=30, blank=True)
	address_1 = models.CharField(max_length=50, blank=True)
	address_2 = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=30, blank=True)
	state = models.CharField(max_length=30, blank=True)
	pin = models.CharField(max_length=20, blank=True)
	country = models.CharField(max_length=20, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=80, blank=True)
	payment_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	payment_method = models.CharField(max_length=1, choices=PAYMENT_METHOD_CHOICES, blank=True)
	user = models.OneToOneField(User, primary_key=True)
	
