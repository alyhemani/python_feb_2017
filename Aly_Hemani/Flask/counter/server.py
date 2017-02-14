from flask import Flask, session, redirect, render_template, request

app= Flask(__name__)
app.secret_key= 'password'

@app.route('/', methods=['POST', 'GET'])
def main():
	if 'number' not in session:
		session['number']=0
	elif 'number' in session:
		session['number']+=1
	return render_template('index.html')

@app.route('/special', methods=['POST'])
def form():
	if 'ninja' in request.form:
		session['number']+=1
	if 'hacker' in request.form:
		session.clear()
	return redirect('/')

app.run(debug=True)

