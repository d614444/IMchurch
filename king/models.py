from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	phone_regex = RegexValidator(regex=r'^[09]\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
	address = models.TextField(max_length=200)
	birth = models.DateField(null=True, blank=True,)
	christian = models.BooleanField(null=True, blank=True)
	immember = models.BooleanField(null=True, blank=True)

	class Meta:
		verbose_name='User Profile'

	def __str__(self):
		return str(self.user)


