from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('survey.html')

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['message']
	return render_template('result.html', name= name, location= location, language= language, comment= comment)

app.run(debug =True)