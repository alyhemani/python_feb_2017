from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
import re 
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


# Create your views here.
def index(request):
	context = {
	'users': User.objects.all()
	}
	return render(request, 'login_app/index.html', context)

def register(request):
	if len(request.POST['first_name'])<2:
		messages.warning(request, 'Please Enter Valid First Name')
	elif len(request.POST['last_name'])<2:
		messages.warning(request, 'Please Enter Valid Last Name')
	elif len(request.POST['email'])<1:
		messages.warning(request, 'Email is Required')
	elif len(request.POST['password'])<1:
		messages.warning(request, 'Password is Required')
	elif len(request.POST['confirmation'])<1:
		messages.warning(request, 'Both Password Fields are Required')
	elif request.POST['password'] != request.POST['confirmation']:
		messages.warning(request, 'Password Confirmation must match Password')
	elif not EMAIL_REGEX.match(request.POST['email']):
		messages.warning(request, 'Invalid Email Address. Please Enter a Valid Email')
	elif not NAME_REGEX.match(request.POST['first_name']):
		messages.warning(request, 'Please Enter Valid First Name')
	elif not NAME_REGEX.match(request.POST['last_name']):
		messages.warning(request, 'Please Enter Valid Last Name')
	else:
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		messages.success(request, 'Successfully Created New User')
		request.session['user_id']= request.POST['first_name']
		return redirect('/success')
	return redirect('/')

def success(request):
	return render(request, 'login_app/success.html')

def login(request):
	login = User.objects.login(request.POST)
	if login[0]:
		request.session['user_id'] = login[1].first_name
		return redirect('/success')
	return redirect('/')

	return redirect('/')












