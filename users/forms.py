from django.forms import widgets
from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

import re
email_regex = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'first_name', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = None
		self.fields['username'].help_text = None
		self.fields['password2'].help_text = None
		self.fields['password2'].label = 'Confirm Password'
		self.fields['first_name'].label = 'First Name*'
		self.fields['email'].label = 'Email Address*'
		self.fields['email'].widget.attrs.update({'required': 'required'})
		self.fields['first_name'].widget.attrs.update({'required': 'required'})

	def clean(self):
		cleaned_data = self.cleaned_data
		cleaned_data['username']=cleaned_data['username'].lower()
		try:
			re.search(email_regex, cleaned_data['email'])
		except KeyError:
			raise ValidationError('Email you entered is invalid')

		# checking Email unique 
		try:
		    User.objects.get(email=cleaned_data['email'])

		except User.DoesNotExist:
		    pass
		else:
		    raise ValidationError('This Email address already exists! Try different one!')

		# checking User unique
		try:
		    User.objects.get(username=cleaned_data['username'])
		except User.DoesNotExist:
		    pass
		else:
		    raise forms.ValidationError('User already exists! Try different one!')
		return cleaned_data

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user_type']