import requests, json, random
from rich.console import Console
from rich.table import Table
from tkinter import *
import webview

with open('art.json') as f:
  object_ids = json.load(f)

table_list = []

table = Table(title="[bold cyan]Thank you for playing. Here is a report of your results:[/bold cyan]")
table.add_column("Rating", justify="center", style="bold magenta")
table.add_column("Department", justify="center", style="bold green")
table.add_column("Title", justify="center", style="yellow")
table.add_column("URL",  justify="center", style="cyan")
table.add_column("Liked",  justify="center", style="green")
table.add_column("Disliked",  justify="center", style="red")

console = Console()

console.print('''\n[bold]THINKER OR STINKER?[/bold]\n
\nThis exercise allows users to view pieces of art selected at random from the Met Museum archives.
\nAfter each object is generated, close the pop-up window and return to the terminal and submit information regarding your enjoyment of the piece before continuing on.
\nWhen you feel sufficiently cultured and decide to quit the program, a report will be returned to you with the information associated with each piece you viewed.
\n[dim yellow]The content presented is not curated and lack of user control over the selection process is intentional. The goal of this exercise is to provide an opportunity for spontanaiety, self-reflection, and enjoyment through the appreciation of art.[/dim yellow]\n''', justify="center", style="yellow")

play = console.input("[underline italic]Would you like to check out some random art?[/underline italic] [bold green]Y[/bold green]/[bold red]N[/bold red]: ")

if play == 'n':
  print('Alrighty then, bye!')

while play == 'y':

  try:

    object = random.choice(object_ids)

    url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object}'

    response = requests.get(
        url, headers={'Accept': 'application/json'})

    data = json.loads(response.text)

    title = data['title']
    url = data['objectURL']
    artist = data['artistDisplayName']
    department = data['department']

  except:
    continue

  else:

    print_result = f"""\n
      [bold]Title[/bold]: {title}
      [bold]Artist[/bold]: {artist}
      [bold]Department[/bold]: {department}
      """
    console.print(print_result)

    tk = Tk()
    tk.geometry("100x100")
    webview.create_window(title, url)
    webview.start()

    rating = console.input("\n[bold cyan]Enter a number from the following list that corresponds to your level of enjoyment of this piece:[/bold cyan]\n\n1 - [magenta]NOT COOL AT ALL[/magenta]\n2 - [red]Not completely terrible[/red]\n3 - [yellow]Has some redeeming qualities[/yellow]\n4 -[green] I frick w/ this[/green]\n5 - [cyan]THIS. IS. MY. SHIZZZ!!![/cyan]\n")

    liked = console.input("\nEnter one word to describe what you liked best about the piece: \n")

    disliked = console.input("\nEnter one word to describe what you liked least: \n")

    table.add_row(rating, department, title, url, liked, disliked)

    table_result = {
      "Rating": rating,
      "Department": department,
      "Title": title,
      "URL": url,
      "Liked": liked,
      "Disliked": disliked
    }

    table_list.append(table_result)

    play = console.input("\n[italic]Would you like to see [underline]more[/underline] art?[/italic] [bold green]Y[/bold green]/[bold red]N[/bold red]: \n")

  if play == 'n':
    console.print(table)

    with open('art_table_report.json', 'w') as outfile:
      json.dump(table_list, outfile)
