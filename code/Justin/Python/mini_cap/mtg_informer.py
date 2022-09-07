import requests
import json
from mtgsdk import Card
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout

# Defining the windows and layout in Kivy module, we return the card image, card price, and a link to buy the card you searched for
kv = """
WindowManager:
    ImageWindow:
    InfoWindow:

<ImageWindow@Screen>:
    name: 'ImageWindow'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'mana symbols.jpg'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.card_title
            size_hint_y: None
            height: 48
            font_size: 24
        AsyncImage:
            source: root.source
        Button:
            text: 'See Information'
            size_hint_y: None
            height: 48
            on_release: app.root.current = 'InfoWindow'
<InfoWindow@Screen>:
    name: 'InfoWindow'
    RelativeLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'mana symbols.jpg'
        Label:
            text: root.card_price
            size_hint: (0.2, 0.2)
            pos_hint: {'x': 0.4, 'top': 1}
            height: 30
            font_size: 30
        Button:
            text: "Click here to buy!"
            size_hint: (.5, .24)
            pos_hint: {'left': 1, 'bottom': 1}
            font_size: 24
            on_release: 
                import webbrowser
                webbrowser.open(root.card_link)
        Button:
            text: "Need a deck idea?"
            size_hint: (.5, .24)
            pos_hint: {'right': 1, 'bottom': 1}
            font_size: 24
            on_release: 
                import webbrowser
                webbrowser.open(root.deck_link)
        Button:
            text: 'Exit'
            size_hint_y: None
            height: 30
            on_press: app.stop()
"""

# Creating our app window


class ImageWindow(Screen):
    card_title = StringProperty()
    source = StringProperty()
    # Calling our requests from our API

    def on_pre_enter(self, *args):
        self.card_title = card_info['name']
        self.source = data['normal']


class InfoWindow(Screen):
    card_price = StringProperty()
    card_link = StringProperty()

    def on_pre_enter(self, *args):
        self.card_price = f" The current USD price is {data_3['usd']}."
        self.card_link = data_2['tcgplayer']
        self.deck_link = data_4['tcgplayer_infinite_decks']

# Creating our manager for our screens


class WindowManager(ScreenManager):
    pass

# Creating our Kivy app


class MTG_InformerApp(App):
    def build(self):
        return Builder.load_string(kv)


# Using the MTG SDK I downloaded from WoTC, which is an API provided by the parent company, create a function to search and return card information based on values selected.


def search_cards():
    card_dict = {}
    u_input = input('Please enter a card name: ')
    card = Card.where(name=u_input).all()
    card_list = []
    # Using a for loop to ensure that only cards that are able to be pulled from scryfall gets added to our list
    for item in card:
        if (item.multiverse_id is not None):
            card_list.append(item)
    # Creating a dictionary to store our information that we need for our later function
    for index, item in enumerate(card_list):
        card_dict[index+1] = {
            "name": item.name,
            "set": item.set_name,
            "multiverse": item.multiverse_id
        }
        print(f'{index+1}: Name: {item.name}\n   Set: {item.set_name}')
    return card_dict


# Calling our function
fun = search_cards()

# Creating a while loop to get the correct input from a user
while True:
    # Using try to check and make sure an integer is entered into the user input
    try:
        # Taking a user input to search for exact card you are looking for
        card_num = int(input(
            'Please select the number of the card you would like to find out more about: '))
        # Running checks to validate the user input
        if card_num in fun.keys():
            card_info = (fun.get(card_num))
            # Using f statements in to print our card information as well as linking to our appropriate site page
            print(
                f"You have selected {card_info['name']} from the set {card_info['set']}.")
            response = requests.get(
                f"https://api.scryfall.com/cards/multiverse/{card_info['multiverse']}")

            # Returning the information we need to process for our app
            data = json.loads(response.text)['image_uris']
            data_2 = json.loads(response.text)['purchase_uris']
            data_3 = json.loads(response.text)['prices']
            data_4 = json.loads(response.text)['related_uris']
            # Calling our application
            MTG_InformerApp().run()
            break
        else:
            print('Invalid selection, please try again.')
    # Using except to print out invalid selections
    except:
        print('Invalid selection, please try again.')
