# Mini Capstone
# For your final Python project, build a program that solves a problem or accomplishes a task. Your program needs to utilize an external API.

# Python Tkinter GUI
# Spoonacular API - Search Recipes by Ingredients / Get Recipe Information

import tkinter as tk
from tkinter.ttk import *
import json, requests
from PIL import ImageTk, Image
from urllib.request import Request, urlopen

root = tk.Tk()
root.title('MINI CAPSTONE')
root.geometry("600x400")
root.bind('<Return>', lambda event: add_listbox())


intro_text = tk.Label(root, text='BANANA BREAD', font=("Rockwell Extra Bold", 35), fg= 'black').pack()

user_entry = tk.Entry(root, width=50)
user_entry.insert(0, 'Enter ingredient here')
user_entry.pack()

# LIST BOX
ingredient_list = []
ingredient_listbox = tk.Listbox(root)
ingredient_listbox.pack()

# ADD ITEM TO LIST BOX
def add_listbox():
    global ingredient_list
    ingredient_list.append(user_entry.get())
    ingredient_listbox.insert(tk.END, user_entry.get())
    user_entry.delete(0, tk.END)
    print(ingredient_list)

# DELETE FROM LIST BOX
def delete_button():
    global ingredient_list
    removed_ingredient = ingredient_listbox.curselection()
    # print(removed_ingredient[0]) - returns tuple with index pos
    ingredient_list.pop(removed_ingredient[0])
    ingredient_listbox.delete(tk.ANCHOR)
    print(ingredient_list)

# SHOW IMAGE
# def show_image(value):
#     api_key = '2ea088bd50764004aa833659f7ed7ed0'
#     url = f"https://api.spoonacular.com/recipes/{value}/information?apiKey={api_key}"
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers)
#     new_data = json.loads(response.text)
#     recipe_url = new_data["spoonacularSourceUrl"]
#     webbrowser.open(recipe_url)
    # global top
    # image_url = Request(
    #     url = 'https://spoonacular.com/recipeImages/633547-312x231.jpg', 
    #     headers= {'User-Agent': 'Mozilla/5.0'}
    # )
    # data_image = urlopen(image_url)
    # image = ImageTk.PhotoImage(data=data_image.read()) 
    # tk.Label(top, image=image).pack()

# COMBINE LISTBOX ITEMS FOR API ENTRY
def submit():
    user_term = ",".join(ingredient_list)
    global top
    top = tk.Toplevel()
    top.geometry("600x400")
    top.title(f"RECIPES - {'/'.join(ingredient_list).title()}")
    api_key = ''
    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}"
    headers = {
        'Content-Type': 'application/json'
    }
    parameters = {
        'ingredients': user_term, 
        'number': 3,
        'ranking': 2, 
        'ignorePantry': True

    }
    response = requests.get(url, headers=headers, params=parameters)
    data = json.loads(response.text)
    for recipe in data:
        # print("RECIPE", recipe["id"], recipe["title"])  
        the_entry = tk.Label(top, text=f'RECIPE {recipe["id"]} {recipe["title"]}', font=20)
        the_entry.pack()
        for ingredient in recipe["missedIngredients"]:
            other_entry = tk.Label(top, text=f'{ingredient["original"]}'.title())
            other_entry.pack()
    

add_button = tk.Button(root, text='ADD', command=add_listbox)
add_button.pack()

del_button = tk.Button(root, text='DELETE', command=delete_button)
del_button.pack()

submit_button = tk.Button(root, text='SUBMIT', command=submit)
submit_button.pack()

root.mainloop()