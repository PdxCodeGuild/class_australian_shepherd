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

console = Console()

console.print('''\n[bold]F*CK ____ ... LET'S ART![/bold]\n
\nThis exercise allows the user to view pieces of art selected at random from the Met Museum archives.
\nAfter each piece is generated, you must click on the URL provided in order to view it. Afterward, you can return to the terminal and submit information regarding your enjoyment of the piece before continuing on.
\nWhen you are done playing, a report will be returned to you with the information associated with each piece you viewed.
\n[dim yellow]The goal of this exercise is to provide an opportunity for spontanaiety, self-reflection, and enjoyment through the appreciation of art.[/dim yellow]\n''', justify="center", style="yellow")

play = console.input("[underline italic]Would you like to check out some random art?[/underline italic] [bold green]Y[/bold green]/[bold red]N[/bold red]: ")
