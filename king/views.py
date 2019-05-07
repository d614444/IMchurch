from django.shortcuts import render

# Create your views here.

def mainpage(request):
	return render(request, 'main.html')

def login_page(request):
	return render(request, 'login.html')

def registeredpage(request):
	return render(request, 'registered.html')		