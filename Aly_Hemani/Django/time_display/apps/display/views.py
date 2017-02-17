from django.shortcuts import render
import time 
from datetime import datetime

# Create your views here.

def index(request):
	print datetime.now()
	context = {
	"datetime":datetime.now()
	}
	return render(request, 'display/index.html', context)
