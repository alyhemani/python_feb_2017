from flask import Flask, render_template, request, flash, redirect
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app =Flask(__name__)
app.secret_key='whatsupbro'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) <1:
		flash('missing fields')
	elif len(request.form['first_name']) <1:
		flash('missing fields')
	elif len(request.form['last_name']) <1:
		flash('missing fields')
	elif len(request.form['password']) <1:
		flash('missing fields')
	elif len(request.form['password_confirmation']) <1:
		flash('missing fields')
	elif len(request.form['password']) <8:
		flash('password not long enough')
	elif request.form['password'] != request.form['password_confirmation']:
		flash('password does not match confirmation')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('invalid email address')
	else:
		flash('SUCCESS')
	return redirect('/')


app.run(debug=True)
