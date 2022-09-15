
from flask import Flask, render_template
app = Flask(__name__)

message = "Hello World!"

posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': " 14th, 2021",
        'body': "sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    },
    {
        'title': "Lorem ipsum dolor sit amet consectetur adipisicing.",
        'author': "Random MrRadom",
        'date': "November 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainabl butcher."
    },
    {
        'title': "ipsum dolor sit amet consectetur.",
        'author': "Blogger Whocaresalot",
        'date': "October 4th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    },
    {
        'title': "Lorem ipsum dolor, sit amet consectetur adipisicing",
        'author': "Blogger Dontthinkso",
        'date': "October 24th, 2021",
        'body': "knausgaard taiyaki narwhal sustainable portland tumblr mixtape sbrooklyn post-ironic meditation butcher."
    }
]

@app.route('/')
def index():
    return render_template('index.html', message=message, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

app.run()
