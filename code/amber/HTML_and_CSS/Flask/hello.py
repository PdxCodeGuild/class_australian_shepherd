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

app.run()
