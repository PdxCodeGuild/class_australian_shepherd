from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    }, 
    {
        'title': "Godfather ipsum dolor sit amet",
        'author': "Michael Corleone",
        'date': "January 1st, 1972",
        'body': "If anything in this life is certain, if history has taught us anything, it is that you can kill anyone. You talk about vengeance. Is vengeance going to bring your son back to you? Or my boy to me? Never hate your enemies. It affects your judgment. I do not like violence, Tom. I am a businessman; blood is a big expense."
    }, 
    {
        'title': "Touch water with paw then recoil in horror",
        'author': "Felix Kohnle",
        'date': "June 10th, 2009",
        'body': " I shall purr myself to sleep. I do no work yet get food, shelter, and lots of stuff just like man who lives with us drink water out of the faucet being gorgeous with belly side up, i vomit in the bed in the middle of the night or taco cat backwards spells taco cat and i do no work yet get food, shelter, and lots of stuff just like man who lives with us. Chew the plant the dog smells bad paw your face to wake you up in the morning."
    },
    {
        'title': "Arrested Development",
        'author': "Michael Bluth",
        'date': "December 29th, 2010",
        'body': "The only person that gets Lucille this excited is Gene. For there's a man inside me, and only when he's finally out, can I walk free of pain. I know, I just call her Annabelle cause she's shaped like a… she's the belle of the ball! The only thing I found in the fridge was a dead dove in a bag. Gob: You didn't eat that, did you? However, she mistook the drowsy eye alcohol warning for a winking eye alcohol suggestion. No borders, no limits… go ahead, touch the Cornballer… you know best? Mom always taught us to curl up in a ball and remain motionless when confronted."
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts)


app.run() 
