from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result')
def result():
	return render_template('result.html')
	return "you GETed here!"
@app.route('/results', methods=['POST'])
def info():
   print "Got Post Info"
   name = request.form['name']
   # return redirect('/')
app.run(debug=True)