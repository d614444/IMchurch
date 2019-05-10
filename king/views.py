from django.shortcuts import render
from .forms import RegistrationForm
from .models import UserProfile
from django.contrib.auth.models import User
# Create your views here.

def mainpage(request):
	return render(request, 'main.html')

def login_page(request):
	return render(request, 'login.html')

def registeredpage(request):

	if request.method == 'POST':

		form = RegistrationForm(request.POST)
		
		if form.is_valid() :
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password2']
			address = form.cleaned_data['address']
			tel = form.cleaned_data['phonenumber']
			print (tel)
			user = User.objects.create_user(username=username, password=password, email=email)
			UserProfiletest = UserProfile(user=user, address=address, phone_number=tel)
			UserProfiletest.save()
	else:
		form = 	RegistrationForm()	
		
	return render(request, 'registered.html', {'form' : form,
												

		})		