#Step one- Hello World (Flask Notes for Class; Flask Docs)-----> Lines 02-06

# @app.route('/')
# def index():
#         return 'Hello World!'
# app.run(debug=True)


from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def index():
        return 'Hello World!'

@app.route('/bloglab')
def home():


#Step two- List of dicts; #Step three- Create the Template

        posts= [
        {
                'title': "The stars and cars",
                'author': "Jean-François Champollion",
                'date': "September 13, 2022",
                'body': "Dispassionate extraterrestrial observer a very small stage in a vast cosmic arena cosmic fugue white dwarf stirred by starlight the sky calls to us.",
        },
        {       'title': "Cosmic Colonies",
                'author': "Jenny Cosmos",
                'date': "September 13, 2022",
                'body': "Descended from astronomers muse about with pretty stories for which there's little good evidence colonies bits of moving fluff great turbulent clouds.",
        },
        {
                'title': "A Tranquil Adventure",
                'author': "Tom Stars",
                'date': "September 13, 2022",
                'body': "Sea of Tranquility tesseract realm of the galaxies paroxysm of global death prime number venture.",
        },
        {
                'title': "The Bearable Equation",
                'author': "Jim the Libra",
                'date': "September 13, 2022",
                'body': "Emerged into consciousness rich in heavy atoms how far away Drake Equation astonishment vastness is bearable only through love?",
        }
        ]
        return render_template('index.html', posts=posts)




app.run(debug=True)