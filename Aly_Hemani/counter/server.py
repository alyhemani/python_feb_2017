from flask import Flask, session, render_template, request
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/', methods=['POST','GET'])
def counter():
	if 'counter' not in session:
		session['counter']=0
	elif 'counter' in session:
		session['counter']+=1
	if 'ninja' in request.form:
		session['counter']+=1
	elif 'hacker' in request.form:
		session['counter']=0
	return render_template('counter.html')
app.run(debug=True)
