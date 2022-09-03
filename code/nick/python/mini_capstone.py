# Mini Capstone
# For your final Python project, build a program that solves a problem or accomplishes a task. Your program needs to utilize an external API.

# Python Tkinter GUI
# Spoonacular API - Search Recipes by Ingredients / Get Recipe Information
# Yelp API - Business Search 
'''
Input: individual ingredients available around the house to search for possible recipes to make
GET https://api.spoonacular.com/recipes/findByIngredients 
*** rate limit 60 requests/sec ***
GET https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=1
parameters = {
    ingredients = string / comma separated list 'apples,flour,sugar'
    ranking = number / maximize used ingredients (1)
    ignorePantry = True / Whether to ignore typical pantry items, such as water, salt, flour, etc.
}
GET https://api.spoonacular.com/recipes/{id}/information
parameters = {
    id = number / The id of the recipe. 716429
}
GET https://api.yelp.com/v3/businesses/search
parameters = {
    term = string / Search term from recipe
    location = string / zipcode
    radius = int / 16000 meters - 10 miles
}

return from spoonacular - search by ingredient:
image.jpg
["id"]
["title"]
["missedIngredients"]["user_entry"] & 

return from spoonacular - search by recipe id:
["spoonacularSourceUrl"]

return from yelp:
["businesses"]["user_entry"]
["businesses"]["url"]
["businesses"]["address1"], ["city"], ["state"], ["zip_code"]
'''

import tkinter as tk
from tkinter.ttk import *
import json, requests
from PIL import ImageTk, Image
from urllib.request import Request, urlopen
import time

#GUI
'''
e = tk.Entry(width=50)
e.pack()

def click_button():
    another = tk.Label(text=entry)
    another.pack()

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
label = tk.Label(text="user_entry")
entry = tk.Entry()
button = tk.Button(text="click", command=click_button)
user_input = entry.get()
greeting.pack()
label.pack()
entry.pack()
button.pack()
window.mainloop()
'''

# spoonacular API
api_key = '2ea088bd50764004aa833659f7ed7ed0'
user_term = 'carrot'
url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}"
headers = {
    'Content-Type': 'application/json'
}
parameters = {
    'ingredients': 'carrot,chicken,broccoli,cheese', 
    'number': 3,
    # 'ranking': 2, 
    'ignorePantry': True

}
response = requests.get(url, headers=headers, params=parameters)
data = json.loads(response)
print(data)

# data = [{'id': 633547, 'title': 'Baked Cinnamon Apple Slices', 'image': 'https://spoonacular.com/recipeImages/633547-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 1, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 2010, 'amount': 1.5, 'unit': 'tablespoons', 'unitLong': 'tablespoons', 'unitShort': 'Tbsp', 'aisle': 'Spices and Seasonings', 'user_entry': 'cinnamon', 'original': '1 1/2 tablespoons of Cinnamon', 'originaluser_entry': 'Cinnamon', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg'}, {'id': 9299, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Dried Fruits;Produce;Baking', 'user_entry': 'raisins', 'original': '1/2 cup of Raisins', 'originaluser_entry': 'Raisins', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/raisins.jpg'}], 'usedIngredients': [{'id': 9003, 'amount': 4.0, 'unit': '', 'unitLong': '', 'unitShort': '', 'aisle': 'Produce', 'user_entry': 'apples', 'original': '4 Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 'originaluser_entry': 'Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 'meta': ['peeled', 'sliced'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}], 'unusedIngredients': [], 'likes': 1}, {'id': 716433, 'title': 'Easiest Breakfast Ever: Sunny Fruit Parfait', 'image': 'https://spoonacular.com/recipeImages/716433-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 1, 'missedIngredientCount': 3, 'missedIngredients': [{'id': 9299, 'amount': 1.0, 'unit': 'serving', 'unitLong': 'serving', 'unitShort': 'serving', 'aisle': 'Dried Fruits;Produce;Baking', 'user_entry': 'raisins', 'original': 'organic raisins', 'originaluser_entry': 'organic raisins', 'meta': ['organic'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/raisins.jpg'}, {'id': 12036, 'amount': 1.0, 'unit': 'serving', 'unitLong': 'serving', 'unitShort': 'serving', 'aisle': 'Savory Snacks', 'user_entry': 'sunflower seeds', 'original': 'sunflower seeds', 'originaluser_entry': 'sunflower seeds', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/sunflower-seeds.jpg'}, {'id': 1116, 'amount': 1.0, 'unit': 'serving', 'unitLong': 'serving', 'unitShort': 'serving', 'aisle': 'Milk, Eggs, Other Dairy', 'user_entry': 'yogurt', 'original': 'plain yogurt, unsweetened (regular or greek)', 'originaluser_entry': 'plain yogurt, unsweetened (regular or greek)', 'meta': ['plain', 'unsweetened', '(regular or greek)'], 'extendeduser_entry': 'unsweetened plain yogurt', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/plain-yogurt.jpg'}], 'usedIngredients': [{'id': 9003, 'amount': 1.0, 'unit': 'serving', 'unitLong': 'serving', 'unitShort': 'serving', 'aisle': 'Produce', 'user_entry': 'apple', 'original': 'chopped organic apple, unpeeled (grated instead of chopped for very small children)', 'originaluser_entry': 'chopped organic apple, unpeeled (grated instead of chopped for very small children)', 'meta': ['organic', 'grated', 'unpeeled', 'chopped', 'for very small children)'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}], 'unusedIngredients': [], 'likes': 93}, {'id': 662665, 'title': 'Swiss Bircher Muesli', 'image': 'https://spoonacular.com/recipeImages/662665-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 1, 'missedIngredientCount': 3, 'missedIngredients': [{'id': 1077, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Milk, Eggs, Other Dairy', 'user_entry': 'milk', 'original': '1/2 cup of Milk', 'originaluser_entry': 'Milk', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/milk.png'}, {'id': 42184, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Cereal', 'user_entry': 'muesli', 'original': '1/2 cup muesli', 'originaluser_entry': 'muesli', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/granola.jpg'}, {'id': 43261, 'amount': 3.0, 'unit': 'tablespoons', 'unitLong': 'tablespoons', 'unitShort': 'Tbsp', 'aisle': 'Milk, Eggs, Other Dairy', 'user_entry': 'skim vanilla yoghurt', 'original': '3 tablespoons of plain or vanilla yoghurt', 'originaluser_entry': 'plain or vanilla yoghurt', 'meta': ['plain'], 'extendeduser_entry': 'plain skim vanilla yoghurt', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/vanilla-yogurt.png'}], 'usedIngredients': [{'id': 9003, 'amount': 1.0, 'unit': '', 'unitLong': '', 'unitShort': '', 'aisle': 'Produce', 'user_entry': 'apple', 'original': '1 Apple', 'originaluser_entry': 'Apple', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}], 'unusedIngredients': [], 'likes': 1}]
recipe_images = []
def get_recipe(): 
    for recipe in data:
        recipe_images.append(recipe["image"])
        print("RECIPE", recipe["id"], recipe["title"])  
        for ingredient in recipe["missedIngredients"]:
            print(ingredient["original"])
    print(recipe_images)


# for image in recipe_images:
#     # urllib.request.urlretrieve(image, "image")
#     # my_img = Image.open("image")
#     # my_img.show()
#     path = image
#     print(path)
#     img = ImageTk.PhotoImage(Image.open(path))
#     panel = tk.Label(window, image = img)
#     panel.pack(side = "bottom", fill = "both", expand = "yes")
#     window.mainloop()
#     break
 
root = tk.Tk()
root.title('MINI CAPSTONE')
root.geometry("400x400")
root.bind('<Return>', lambda event: button_click())

# ENTRY AREA
user_entry = tk.Entry(root, width=50)
user_entry.insert(0, 'Enter ingredient here')
user_entry.pack()

# BUTTON CLICK
def button_click():
    for recipe in data:
        recipe_images.append(recipe["image"])
        print("RECIPE", recipe["id"], recipe["title"])  
        the_entry = tk.Label(root, text=f'RECIPE {recipe["id"]} {recipe["title"]}')
        the_entry.pack()
        for ingredient in recipe["missedIngredients"]:
            other_entry = tk.Label(root, text=f'{ingredient["original"]}'.title())
            other_entry.pack()
        # print(recipe_images)
    #
    # the_entry = tk.Label(root, text=data)
    # the_entry.pack()

# SHOW IMAGE
def show_image():
    image_url = Request(
        url = 'https://spoonacular.com/recipeImages/633547-312x231.jpg', 
        headers= {'User-Agent': 'Mozilla/5.0'}
    )
    data_image = urlopen(image_url)
    image = ImageTk.PhotoImage(data=data_image.read()) 
    tk.Label(root, image=image).pack()

# RADIO BUTTON

def radio_button():
    list_recipe = tk.StringVar()
    list_recipe.get()
    for recipe in data:
        print(recipe)
        # recipe_images.append(recipe["image"])
        # print("RECIPE", recipe["id"], recipe["title"]) 
        tk.Radiobutton(
            root, text=f'RECIPE {recipe["id"]} {recipe["title"]}', 
            variable=list_recipe, value=f'RECIPE {recipe["id"]} {recipe["title"]}'
            ).pack()
        # the_entry = tk.Label(root, text=f'RECIPE {recipe["id"]} {recipe["title"]}')
        # the_entry.pack()
        for ingredient in recipe["missedIngredients"]:
            other_entry = tk.Label(root, text=f'{ingredient["original"]}'.title())
            other_entry.pack()

# SHOW BUTTON
# mybutton = tk.Button(root, text='Click', command=button_click)
# mybutton.pack()

#Progress Bar
def step():
    for i in range(5000000):
        root.update_idletasks()
        pb1['value'] += 20
        
        time.sleep(0.001)

pb1 = Progressbar(root, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
pb1.pack(expand=True)

Button(root, text='Start', command=step).pack()




# root.mainloop()


# INPUT ENTRY INTO FIELD WITH RADIO BUTTON
ingredient_list = []
list_ingredient = tk.StringVar(root)
# counter = 1
def clicked():
    # global counter 
    ingredient_list.append(user_entry.get())
    print(ingredient_list)
    global list_ingredient
    # list_ingredient.get()
    Radiobutton(root, text=user_entry.get(), variable=list_ingredient.get(), value=user_entry.get()).pack()
    # ingredient_list.append(ingredient)
    # ingredient = tk.Label(root, text=user_entry.get())
    # ingredient.pack()
    # counter += 1
    # return list_ingredient.get()
    # print(counter)

   
# LIST BOX
ingredient_listbox = tk.Listbox(root)
ingredient_listbox.pack()

# ADD ITEM TO LIST BOX
def add_listbox():
    global ingredient_list
    ingredient_list.append(user_entry.get())
    ingredient_listbox.insert(tk.END, user_entry.get())
    user_entry.delete(0, tk.END)
    print(ingredient_list)

# BUTTON TO DELETE
def delete_button():
    global ingredient_list
    removed_ingredient = ingredient_listbox.curselection()
    # print(removed_ingredient[0])
    ingredient_list.pop(removed_ingredient[0])
    ingredient_listbox.delete(tk.ANCHOR)
    print(ingredient_list)

# COMBINE LISTBOX ITEMS FOR API ENTRY
def submit():
    user_term = ",".join(ingredient_list)
    print(user_term)

add_button = tk.Button(root, text='ADD', command=add_listbox)
add_button.pack()

del_button = tk.Button(root, text='DELETE', command=delete_button)
del_button.pack()

submit_button = tk.Button(root, text='SUBMIT', command=submit)
submit_button.pack()
