from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'password'
import random 

@app.route('/')
def main():
	if 'gold' not in session:
		session['gold']=0
	if 'log' not in session:
		session['log']=''
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def gold():
	if 'farm' in request.form:
		number = random.randrange(10,21)
		session['gold']+= number
		session['log'] += 'Earned ' +str(number)+ ' gold from the farm!'
	elif 'cave' in request.form:
		number = random.randrange(5,11)
		session['gold']+= number
		session['log'] += 'Earned ' +str(number)+ ' gold from the farm!'
	elif 'house' in request.form:
		number = random.randrange(2,6)
		session['log'] += 'Earned ' +str(number)+ ' gold from the farm!'
		session['gold']+= number
	elif 'casino' in request.form:
		number = random.randrange(-51,51)
		session['gold']+= number
		if number > 0:
			session['log'] += 'Earned ' +str(number)+ ' gold from the farm!'
		elif number == 0:
			session['log'] += 'Earned 0 gold from the casino!'
		elif number < 0:
			session['log'] += 'OUCH!!! Lost ' +str(number)+ ' gold from the casino!'
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)