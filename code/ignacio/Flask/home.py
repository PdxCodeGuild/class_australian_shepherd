from flask import Flask,render_template
app = Flask('spiderman')

posts = [
    {
        'title': 'unanswered calls',
        'author': 'nick furry',
        'date': 'July 15 2022',
        'body': ''
    },{
        'title': 'chimichanga',
        'author': 'deadpool',
        'date': 'December 3 2022',
        'body': ''
    },{
        'title': 'bark',
        'author': 'olive',
        'date': 'April 7 2022',
        'body': ''
    },{
        'title': 'photographs',
        'author': 'J. Jonah Jameson',
        'date': 'Sep 14 2022',
        'body': ''
    }
]
# for items in posts
# post1= posts[0]['title']

@app.route('/',)
def index():
    return render_template('index.html',posts=posts)

