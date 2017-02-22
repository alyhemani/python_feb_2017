from django.shortcuts import render, redirect
from .models import Email 
import re 
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
	context = {
	"emails": Email.objects.all()
	}
	return render(request, 'first_email/index.html', context)

def process(request):
	if EMAIL_REGEX.match(request.POST['email']):
		Email.objects.create(email=request.POST['email'])
		email = request.POST['email']
		messages.success(request, 'Your Email Address Is Valid:' + email)
	elif not EMAIL_REGEX.match(request.POST['email']):
		messages.warning(request, 'Invalid Email Address')
	return redirect('/')

def remove(request, id):
	Email.objects.filter(id=id).delete()
	return redirect('/')