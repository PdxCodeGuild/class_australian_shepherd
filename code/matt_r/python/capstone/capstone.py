


import tkinter
import tkinter.messagebox
import json
import requests
from tkinter.ttk import Label
from config import API_KEY 





year  = input('What year are you looking for?:  \n')
make  = input('What make are you looking for?:  \n')
model = input('What model are you looking for?: \n')            
# year  = '2012'
# make  = 'honda'
# model = 'civic'


api_url = f'https://api.api-ninjas.com/v1/cars?make={make}&year={year}&limit=1&model={model}'
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

data = json.loads(response.text)
results = data[0]


data = f"{year}, {make}, {model}\n"
data2 = f"This vehicle has a(n) {results['displacement']}L engine,\n"
data3 = f" a combined mpg of {results['combination_mpg']},\n"
data4 = f"and is {results['drive']}"
# path = 


root = tkinter.Tk()
root.title('Vehicle info Search By Matt R')
root.iconbitmap(f'C:\capstoneimages')
root.geometry('800x500')

car = tkinter.PhotoImage(file=f'C:\capstoneimages\{make}.png')
my_label = tkinter.Label(root,image=car)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


frame_tasks = tkinter.Frame(root)
frame_tasks.pack()


my_text = Label(root, text=data + data2 + data3 + data4)
my_text.pack(pady=50)



root.mainloop()