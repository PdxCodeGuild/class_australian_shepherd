from flask import Flask,render_template
app = Flask('spiderman')

@app.route('/',)
def index():
    posts = [
        {
            'title': 'Unanswered Calls',
            'author': 'Nick Furry',
            'date': 'July 15 2022',
            'body': "Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass."
        },{
            'title': 'Chimichanga!!',
            'author': 'Deadpool',
            'date': 'December 3 2022',
            'body': 'Lorem fistrum ahorarr amatomaa benemeritaar va usté muy cargadoo condemor llevame al sircoo me cago en tus muelas. Amatomaa a peich me cago en tus muelas por la gloria de mi madre. Te voy a borrar el cerito quietooor qué dise usteer amatomaa la caidita pupita pupita tiene musho peligro no puedor de la pradera a gramenawer. A gramenawer te voy a borrar el cerito al ataquerl al ataquerl papaar papaar de la pradera papaar papaar a wan. Diodenoo sexuarl jarl ese hombree condemor no puedor sexuarl. Mamaar a peich hasta luego Lucas jarl. Va usté muy cargadoo no puedor te voy a borrar el cerito qué dise usteer torpedo no te digo trigo por no llamarte Rodrigor apetecan apetecan la caidita por la gloria de mi madre. Quietooor está la cosa muy malar me cago en tus muelas al ataquerl ese hombree está la cosa muy malar hasta luego Lucas fistro.'
        },{
            'title': 'Bark, *Tail wag*',
            'author': 'Olive Chimenti',
            'date': 'April 7 2022',
            'body': 'Doggo ipsum puggo such treat he made many woofs pupper very hand that feed shibe, shooberino doge. Very jealous pupper waggy wags most angery pupper I have ever seen shoober pupper smol borking doggo with a long snoot for pats very taste wow I am bekom fat, pupperino porgo very good spot shibe stop it fren. Big ol pupper maximum borkdrive pupper you are doin me a concern, heckin angery woofer. Smol borking doggo with a long snoot for pats ruff yapper heckin angery woofer, puggo. Long bois many pats shoob, length boy. Snoot borkf extremely cuuuuuute heckin, sub woofer.'
        },{
            'title': 'Menace',
            'author': 'J. Jonah Jameson',
            'date': 'Sep 14 2022',
            'body': 'Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition. Organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment.'
        }
    ]
    return render_template('index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')