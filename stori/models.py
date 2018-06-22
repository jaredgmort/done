from django.db import models
from django.urls import reverse
from datetime import date


class Member(models.Model):
	full_name = models.CharField(max_length=250, blank=True)
	email = models.EmailField(max_length=250, blank=True)
	gender = models.CharField(max_length=250, blank=True)
	date_birth = models.DateField(null=True, blank=True)
	phone_number = models.CharField(max_length=250, default='0244231035', blank=True)
	address = models.CharField(max_length=250, blank=True)
	town_city = models.CharField(max_length=250, blank=True)
	country = models.CharField(max_length=250, blank=True)
	occupation = models.CharField(max_length=250, blank=True)
	pics = models.ImageField(default = 'default.jpg')


	def __str__(self):
		return self.full_name + '|' + self.phone_number

class Account(models.Model):
 	year = models.CharField(max_length=250, null=True, blank=True)	
 	month = models.CharField(max_length=250, null=True, blank=True)
 	offering_gotten = models.CharField(max_length=250, null=True, blank=True)	
 	offering_welfare = models.CharField(max_length=250, null=True, blank=True)
 	outstanding_offering = models.CharField(max_length=250, null=True, blank=True)	

 	def __str__(self):
 		return self.outstanding_offering


class Week(models.Model):
 	account = models.ForeignKey(Account, on_delete=models.CASCADE)
 	week1 = models.CharField(max_length=250, null=True, blank=True)
 	week2 = models.CharField(max_length=250, null=True, blank=True)
 	week3 = models.CharField(max_length=250, null=True, blank=True)
 	week4 = models.CharField(max_length=250, null=True, blank=True)






	