#Created by: Johji Iizuka and Elvis Ardon
#Date: 10/14/2023
#Description: This program will provide simple fortune telling services based the user's on mood, weather, and name.


# Elvis will be working on the gui for weather input.
# Much of the work i found was at this site https://www.pythontutorial.net/tkinter/tkinter-radio-button/

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('LBCC Fortune Teller')

# Function will display the users fortune in a separate dialogue box.
def ask_4_weather():
    showinfo(
        title='Your fotune is:',
        message=selected_weather.get()
    )


selected_weather = tk.StringVar()
weather_type = (('Sunny', 'Due to this beatiful weather, you will find more happiness outside'),
         ('Cold', 'You may want to stay inside because its cold. Try a new indoor activity. It will bring much joy'),
         ('Rainy', 'There is no time to waste. Make new memmories before they are lost in time. Like tears in the rain'),
         )

# label for radio buttons
label = ttk.Label(text="What is the weather like right now")
label.pack(fill='x', padx=5, pady=5)

# radio buttons. I think this loop iterates through the tuples from line 27 and creates the radio buttons.
for weather in weather_type:
    r = ttk.Radiobutton(
        root,
        text=weather_type[0],
        value=weather_type[1],
        variable=selected_weather
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Choose one of the buttons for the current weather",
    command=ask_4_weather)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()


