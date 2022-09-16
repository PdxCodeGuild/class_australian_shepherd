from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "hello"
    # return render_template('templates/blogmain.html')

# posts = [
#     {
#         'title': "Chillwave offal you probably haven't heard of them",
#         'author': "Blogger McBlogface",
#         'date': "October 14th, 2021",
#         'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
#     }
    

# ]





# app.run()