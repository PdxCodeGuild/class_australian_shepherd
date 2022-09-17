from flask import Flask, render_template
app = Flask(__name__)
import random

posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    }, 
    {
        'title': "Corporate Ipsum",
        'author': "Agile McFramework",
        'date': "November 14th, 2021",
        'body': "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment."
    }, 
    {
        'title': "Let's Generate Some Cheese!",
        'author': "Chessey McLactase",
        'date': "December 14th, 2021",
        'body': "Emmental camembert de normandie danish fontina. Chalk and cheese stilton gouda ricotta camembert de normandie smelly cheese goat rubber cheese. Pecorino feta hard cheese cheeseburger queso bavarian bergkase squirty cheese danish fontina. Cheese and wine cheeseburger cheesy feet."
    }, 
    {
        'title': "A Meatier Lorem Ipsum Generator",
        'author': "Porky McPigface",
        'date': "January 14th, 2022",
        'body': "Ham hock tongue buffalo brisket capicola landjaeger pork chop ribeye bresaola. Andouille bresaola ribeye pork chop pork belly. Andouille tri-tip chicken pancetta tail. Corned beef fatback jerky chuck ham hock porchetta pork beef, capicola pork chop hamburger ribeye turkey tenderloin. Alcatra pig shankle tongue jerky short loin. Flank pancetta sausage pork loin, jerky porchetta bresaola kielbasa brisket salami meatball ribeye. Bacon tri-tip ham hock alcatra kevin picanha turducken chuck."
    }, 
    {
        'title': "Yar Pirate Ipsum",
        'author': "Davy Jones",
        'date': "Feburary 14th, 2022",
        'body': "Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to."
    }, 
    {
        'title': "The Māori text generator with Bang!",
        'author': "Tumeke Pahu",
        'date': "March 14th, 2022",
        'body': "Ko te moemoea a Maui kia haere ngatahi ai ratou ko ona tuakana ki te hii ika. I te hokinga mai o ona tuakana ki tatahi, ka kii atu a Maui, “ka taea e au te haramai i to koutou na taha ki te hii ika?” Engari, ko te whakautu o ona tuakana ki a ia ano, “Kao, he rangatahi noa iho koe. Kaore he wahi mau kei te waka nei, na reira me noho tau ki tatahi ke”."
    }
]

# for blog in random.sample(posts,k=4):
#     print(blog)

@app.route('/')
def index():
    return render_template('index.html', random=random, posts=posts)

@app.route('/randomize')
def randomize():
    return render_template('randomize.html', random=random, posts=posts)

@app.route('/sorted')
def sorted():
    return render_template('sorted.html', posts=posts) 

app.run() 



