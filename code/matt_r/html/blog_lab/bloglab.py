from flask import Flask, render_template
app = Flask(__name__)






@app.route('/')
def index():
    posts = [{
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "September 23rd, 1989",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial."
    },
    {
        'title': "Chuck Norris haven't heard of them",
        'author': "Chuck Norris",
        'date': "October 23rd, 2017",
        'body': "The quickest way to a man's heart is with Chuck Norris' fist."
    },
    {
        'title': "insert title here",
        'author': "mr. Norris",
        'date': "October 11th, 1990",
        'body': "Chuck Norris, not the box jellyfish of northern Australia, is the most venomous creature on earth. "
    },
    {
        'title': "I ran out of ideas",
        'author': "Sir Chuck",
        'date': "May 23rd, 2010",
        'body': " When playing Modern Warfare 2, Chuck Norris can get a tactical nuke with the Spartan Laser from Halo 3."
    }
    ]
    # return f"hello world"
    return render_template('blogmain.html', posts=posts)



app.run(debug=True)