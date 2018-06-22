from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import  ModelForm
from .models import Member
#from django.forms import extras

#class SignUpForm(UserCreationForm):
   
   # class Meta:
   #     model = User
   #     fields = ('username','password1')


class MemberForm(ModelForm):
	

	class Meta:
		model = Member
		fields = ['full_name', 'email', 'gender', 'date_birth', 'phone_number', 'address', 'town_city', 'country', 'occupation']














