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
                'body': "Dispassionate extraterrestrial observer a very small stage in a vast cosmic arena cosmic fugue white dwarf stirred by starlight the sky calls to us. Non consequat ea practitioner healer Reiki enlighten spirit guides. Full moon sage consequat, aute exercitation Chinese medicine enlighten laboris pendulum joy goddess. Cillum laborum ipsum dolore divine peace adipisicing meditate candles pariatur ut angels love. Divination chakra clearing incididunt Flower of Life, occaecat ut stones reincarnation non do card readings nisi exercitation. Aliqua practitioner in love healer. Essential Oils massage enim ea full moon, ipsum qui.",
        },
        {       'title': "Cosmic Colonies",
                'author': "Jenny Cosmos",
                'date': "September 13, 2022",
                'body': "Descended from astronomers muse about with pretty stories for which there's little good evidence colonies bits of moving fluff great turbulent clouds. Flower of Life Chinese medicine ut joy laboris love. Exercitation ea eu chanting voluptate pendulum adipisicing, fibonacci harmonic incididunt. Reiki nisi excepteur est exercitation massage chakras reprehenderit spirit guides. Candles dolore awakening harmonic esse ut divine officia commodo meditate excepteur full moon eu in elit. Ut enim culpa elit spiritual healing laboris. Minim magna energy healing laborum, crystals sint massage enlighten exercitation qui.",
        },
        {
                'title': "A Tranquil Adventure",
                'author': "Tom Stars",
                'date': "September 13, 2022",
                'body': "Sea of Tranquility tesseract realm of the galaxies paroxysm of global death prime number venture. Ex nulla spiritual healing exercitation Chinese medicine ut bells. Magna Reiki healing non incididunt. Ad Pink Himalayan Salt Flower of Life officia meditate laborum. Healer fugiat Sacred Geometry, chakra clearing empath angels velit pendulum exercitation fibonacci do culpa. Commodo aliqua dolore healer, goddess in ut. Nostrud spirit guides shamantic stones.",
        },
        {
                'title': "The Bearable Equation",
                'author': "Jim the Libra",
                'date': "September 13, 2022",
                'body': "Emerged into consciousness rich in heavy atoms how far away Drake Equation astonishment vastness is bearable only through love? Adipisicing angels labore, shamantic occaecat love cillum. Mollit sage ut Buddha Reiki ad cillum deserunt occaecat nulla reincarnation aliqua. Shamantic magna charms love. Massage enim in, veniam love Reiki eu cillum.",
        }
        ]
        return render_template('index.html', posts=posts)




app.run(debug=True)