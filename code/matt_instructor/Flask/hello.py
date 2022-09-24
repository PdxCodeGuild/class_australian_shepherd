from flask import Flask, render_template
app = Flask(__name__)
import random

num = random.randint(0, 100)
print(num)

colors = [
    {
        'name': 'red',
        'rgb': '(255, 0, 0)'
    },
    {
        'name': 'blue',
        'rgb': '(0, 0, 255)'
    },
]

@app.route('/')
def index():
    return render_template('index.html', number=num)


@app.route('/about')
def about():
    return render_template('about.html', colors=colors)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/test')
def test():
    return render_template('test.html')


# app.run() 




'''
setting up flask and running the app 

1: pip install flask
2: set the variable by terminal (one of these for what one you use)
	windows: set FLASK_APP=<appname>.py
	linux: export FLASK_APP=<appname>.py
	powershell: $env:FLASK_APP="<appname>.py"

3: flask run
'''