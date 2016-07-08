from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle form submission

# defined which HTTP methods are allowed by this route
@app.route('/results', methods=['POST'])
def info():
   print "Got Post Info"
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True)