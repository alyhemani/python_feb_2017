from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'first_ninja/index.html')

def ninjas(request):
	return render(request, 'first_ninja/ninjas.html')

def color(request, color):
	if color == 'blue':
		img = '../../static/first_ninja/images/leonardo.jpg'
	elif color == 'orange':
		img = '../../static/first_ninja/images/michelangelo.jpg'
	elif color == 'red':
		img = '../../static/first_ninja/images/raphael.jpg'
	elif color == 'purple':
		img = '../../static/first_ninja/images/donatello.jpg'
	else:
		img = '../../static/first_ninja/images/notapril.jpg'

	context = {
	'img': img
	}


	return render(request, 'first_ninja/colors.html', context)