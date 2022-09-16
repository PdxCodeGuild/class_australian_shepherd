from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'title': "Why Tobias Fünke Matters",
        'author': "TobeHead143",
        'date': "October 69th, 2021",
        'body': "Interfere? I ought to pull down your pants and spank your ass raw. I'm sorry, have we met? My brother wasn't optimistic it could be done, but I didn't take 'wasn't optimistic it could be done' for an answer. Well excuse me for liking the way they frame my junk! It seems like only yesterday you were bursting forth from your mother's fertile womb. Although George Michael had only got to second base, he'd gone in head first, like Pete Rose. Buster, you remember when we were kissing last night? Buster: It was a wild, wild ride."
    },
     {
        'title': "George Michael is My God",
        'author': "CarefulWhisperer",
        'date': "October 1th, 2021",
        'body': "Let me give that oatmeal some brown sugar. Hey, if I can't find a horny immigrant by then, I don't deserve to stay. I made a huge tiny mistake. But where did the lighter fluid come from? Oh, hi, Mom. I have the afternoon free. Really? Did 'nothing' cancel? Teamocil. Please refrain from discussing or engaging in any sort of interoffice [bleep] or [bleep] or finger[bleep] or [bleep]sting or [bleep] or even [bleep]."
    },
     {
        'title': "Can Will Arnett Wear Socks?",
        'author': "AnkleBiter311",
        'date': "October 2th, 2021",
        'body': "Smack of ham. What is she doing at a beauty pageant? Is she running the lights or something? A million [bleep]ing diamonds! Stop it, stop it. This objectification of women has to stop. Michael: It's just Mom and whores. Obviously this blue part here is the land. Or it could be your colon. I'd want to get in there and find some answers. Pound is tic-tac-toe, right? Buster's in what we like to call a light to no coma. In laymans terms, it might be considered a very heavy nap."
    },
     {
        'title': "Buster & Lucille II: Great Couple or Greatest Couple?",
        'author': "TeamAustero",
        'date': "October 3th, 2021",
        'body': "I'll buy you a hundred George Michaels that you can teach to drive! Teamocil. You want your belt to buckle, not your chair. If that man's straight, then I am sober. No, I was ashamed to be SEEN with you. I like being with you. Here he comes. Here comes John Wayne. Mr. Zuckerkorn, you've been warned about touching. You said spanking. Maybe it was the eleven months he spent in the womb. The doctor said there were claw marks on the walls of her uterus. Don't worry, these young beauties have been nowhere near the bananas. A million ****ing diamonds! How do you know Steve Holt? Are you in AA? Heyyyyy, hermano. Did you enjoy your lunch, mom? You drank it fast enough. I'm tired of trying to find happiness through lies and self-medicating. If you need me, I'll be at the bar. If I wanted something your thumb touched, I'd eat the inside of your ear. No, no, it's pronounced a-nal-ra-pist. It wasn't really the pronunciation that bothered me. These are my awards, Mother. From Army. The seal is for marksmanship, and the gorilla is for sand racing. And although the intervention didn't work, it turned into one of the Bluth family's better parties."
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)
