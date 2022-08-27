import requests, json, random
from rich.console import Console
from rich.table import Table
#from rich.theme import Theme
from tkinter import *
import webview

with open('art.json') as f:
  object_ids = json.load(f)

table = Table(title="Thank you for playing. Here is a report of your results:")
table.add_column("Rating", justify="center", style="bold green")
table.add_column("Title", justify="center", style="yellow")
table.add_column("URL",  justify="center", style="cyan")
table.add_column("Liked",  justify="center", style="green")
table.add_column("Disliked",  justify="center", style="magenta")
