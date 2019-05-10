from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields  import PhoneNumberField
import re

def email_check(email):
	pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}][email protected]\w+\.\w+)\"?")
	return re.match(pattern, email)

class RegistrationForm(forms.Form):
	username = forms.CharField(label='inputaccount', max_length=50,)
	email = forms.EmailField(label='Email',)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
	address = forms.CharField(max_length=200)
	phonenumber = forms.RegexField(regex=r'^[09]\d{9,10}$')

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if len(username) < 6:
			raise forms.ValidationError("Your username must be at least 6 characters long.")
		elif len(username) > 50:
			raise forms.ValidationError("Your username is too long.")
		else:
			filter_result = User.objects.filter(username__exact=username)
		if len(filter_result) > 0:
			raise forms.ValidationError("Your username already exists.")

		return username		


	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Account'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Password'
		self.fields['address'].widget.attrs['class'] = 'form-control'
		self.fields['address'].widget.attrs['placeholder'] = 'address'
		self.fields['phonenumber'].widget.attrs['class'] = 'form-control'

