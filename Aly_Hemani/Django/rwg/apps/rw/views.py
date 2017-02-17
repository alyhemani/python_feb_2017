from django.shortcuts import render, redirect
import string, random

# Create your views here.
def index(request):
    def random_generator(size=14, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    request.session['random']=(random_generator())
    return render(request, 'rwt/index.html')

def run(request):
	return redirect('/')