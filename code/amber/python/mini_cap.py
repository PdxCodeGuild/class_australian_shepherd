import requests, json, random
from rich.console import Console
from rich.table import Table
#from rich.theme import Theme
from tkinter import *
import webview

with open('art.json') as f:
  object_ids = json.load(f)
