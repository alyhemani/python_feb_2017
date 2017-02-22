from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
	'courses': Course.objects.all()
	}
	return render(request, 'first_course/index.html', context)

def process(request):
	Course.objects.create(name=request.POST['course'], description=request.POST['description'])
	return redirect('/')

def remove(request, id):
	context={
	'course': Course.objects.get(id=id)
	}
	return render(request, 'first_course/delete.html', context)

def confirm(request, id):
	Course.objects.filter(id=id).delete()
	return redirect('/')