from flask import Flask, render_template
app = Flask(__name__)

greet = 'Hello World!'

posts = [
    {
        'title': "Title One",
        'author': "Some Person",
        'date': "Last Week",
        'blog': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                Ut vel dolor a elit efficitur rhoncus. Morbi nec ullamcorper \
                velit. Nunc quis lacinia enim. Fusce suscipit sodales urna, \
                quis pharetra est semper at. Etiam blandit arcu ac commodo \
                placerat. Nam volutpat rhoncus purus et rutrum. Suspendisse \
                potenti. Pellentesque habitant morbi tristique senectus et \
                netus et malesuada fames ac turpis egestas. "
    },
    {
        'title': "Title Two",
        'author': "Some Other Person",
        'date': "Yesterday",
        'blog': "Prow scuttle parrel provost Sail ho shrouds spirits boom \
                mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's \
                nest nipperkin grog yardarm hempen halter furl. Swab barque \
                interloper chantey doubloon starboard grog black jack gangway rutters.\
                Deadlights jack lad schooner scallywag dance the hempen jig carouser \
                broadside cable strike colors. Bring a spring upon her cable holystone \
                blow the man down spanker Shiver me timbers to go on account lookout \
                wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm \
                spyglass sheet transom heave to. Trysail Sail ho Corsair red ensign hulk \
                smartly boom jib rum gangway. Case shot Shiver me timbers gangplank crack \
                Jennys tea cup ballast Blimey lee snow crow's nest rutters. Fluke jib \
                scourge of the seven seas boatswain schooner gaff booty Jack Tar transom spirits."
    },
    {
        'title': "Title Three",
        'author': "Yet Another Person",
        'date': "Today",
        'blog': "I'm baby sus succulents green juice poke. Lomo PBR&B truffaut snackwave,\
                chartreuse paleo you probably haven't heard of them vinyl dreamcatcher jean\
                shorts. 8-bit wolf pug banh mi PBR&B, keffiyeh crucifix. Pinterest poke next \
                level lomo lumbersexual keytar before they sold out beard man braid actually \
                farm-to-table gastropub edison bulb woke. Tattooed thundercats locavore iceland \
                subway tile poutine skateboard raw denim organic try-hard gochujang cold-pressed \
                hexagon aesthetic. Adaptogen waistcoat everyday carry prism echo park."
    },
    {
        'title': "Title Four",
        'author': "The Last Person",
        'date': "Tomorrow",
        'blog': "Trillion made in the interiors of collapsing stars citizens of distant epochs \
        finite but unbounded Orion's sword Apollonius of Perga? Vastness is bearable only through \
        love Flatland Sea of Tranquility astonishment kindling the energy hidden in matter courage \
        of our questions. Take root and flourish Sea of Tranquility vanquish the impossible \
        extraplanetary Tunguska event with pretty stories for which there's little good evidence? \
        The sky calls to us a very small stage in a vast cosmic arena the only home we've ever known \
        the sky calls to us permanence of the stars a very small stage in a vast cosmic arena and \
        billions upon billions upon billions upon billions upon billions upon billions upon billions."
    },
]

@app.route('/')
def index():
    return render_template('index.html', greet=greet)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)     