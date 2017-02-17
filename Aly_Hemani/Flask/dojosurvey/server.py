from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key='bannana'

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def info():
	if len(request.form['name']) < 1:
		flash('missing field(s)')
		return redirect('/')
	if len(request.form['comment'])< 1:
		flash('missing field(s)')
		return redirect('/')
	if len(request.form['comment'])>120:
		flash('Comment is too long. Must be less than 120 characters')
		return redirect('/')
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)