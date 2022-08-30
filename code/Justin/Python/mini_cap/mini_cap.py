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

headers = {}


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
# img = Image.open(requests.get(
#     data['normal'], stream=True).raw)
# img.show()
# print(data['normal'])

kv = """


<ReadWriteScreen>:
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
            text: 'Exit Application'
            size_hint_y: None
            height: 48
            on_press: app.stop()
ScreenManager:
    ReadWriteScreen:
        name: 'card'            

"""


class ReadWriteScreen(Screen):
    card_title = StringProperty()
    source = StringProperty()

    def on_pre_enter(self, *args):
        self.card_title = a_1['name']
        self.source = data['normal']


class MTG_InformerApp(App):
    def build(self):
        return Builder.load_string(kv)


MTG_InformerApp().run()
