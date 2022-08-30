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


def search_cards():
    card_dict = {}
    u_input = input('Please enter a card name: ')
    card = Card.where(name=u_input).all()
    for index, item in enumerate(card):
        card_dict[index+1] = {
            "name": item.name,
            "set": item.set_name,
            "multiverse": item.multiverse_id
        }
        print(f'{index+1}: Name: {item.name}\n   Set: {item.set_name}')
    return card_dict


a = search_cards()
ok = int(input(
    'Please select the number of the card you would like to find out more about: '))
a_1 = (a.get(ok))
print(f"You have selected {a_1['name']} from the set {a_1['set']}.")
response = requests.get(
    f"https://api.scryfall.com/cards/multiverse/{a_1['multiverse']}")
data = json.loads(response.text)['image_uris']
data_2 = json.loads(response.text)['purchase_uris']
data_3 = json.loads(response.text)['prices']


kv = """

WindowManager:
    ImageWindow:
    InfoWindow:

<ImageWindow@Screen>:
    name: 'ImageWindow'
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
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.card_price
            size_hint_y: 1
            size_hint_x: 1
            height: 48
            font_size: 24
        Button:
            text: "Click here to buy!"
            size_hint_y: .75
            size_hint_x: 1
            heigh: 10
            font_size: 24
            on_release: 
                import webbrowser
                webbrowser.open(root.card_link)
        Button:
            text: 'Exit'
            size_hint_y: None
            height: 48
            on_press: app.stop()




"""


class ImageWindow(Screen):
    card_title = StringProperty()
    source = StringProperty()

    def on_pre_enter(self, *args):
        self.card_title = a_1['name']
        self.source = data['normal']


class InfoWindow(Screen):
    card_price = StringProperty()
    card_link = StringProperty()

    def on_pre_enter(self, *args):
        self.card_price = f" The current USD price is {data_3['usd']}."
        self.card_link = data_2['tcgplayer']


class WindowManager(ScreenManager):
    pass


class MTG_InformerApp(App):
    def build(self):
        return Builder.load_string(kv)


MTG_InformerApp().run()
