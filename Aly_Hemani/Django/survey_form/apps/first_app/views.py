from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	print 'hi'
	return render(request, 'survey_form/index.html')

def process(request):
	print 'yes'
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		return redirect('/result')
	else:
		return redirect('/')
def result(request):
	print 'bye'
	return render(request, 'survey_form/result.html')