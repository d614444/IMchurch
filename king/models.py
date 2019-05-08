from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	tel = PhoneNumberField(null=False, blank=False, unique=True)
	address = models.TextField(max_length=200)
	birth = models.DateField()
	christian = models.BooleanField()
	immember = models.BooleanField()

	class Meta:
		verbose_name='User Profile'

	def __str__(self):
		return str(self.user)	