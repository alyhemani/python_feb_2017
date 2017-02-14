from flask import Flask, render_template, redirect, session, request
app =Flask(__name__)
app.secret_key='password'
import random

@app.route('/')
def main():
	if 'value' not in session:
		session['value']=random.randrange(0,101)
		print session['value']
	if 'value' in session:
		print session['value']
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] =int(request.form['number'])
	print session['guess']
	if session['guess'] == session['value']:
		session['answer'] = 'correct'
	elif session['guess'] > session['value']:
		session['answer'] = 'too high'
	elif session['guess'] < session['value']:
		session['answer'] = 'too low'
	print session['answer']
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)