import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="How are you feeling:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_feeling = tk.StringVar()
feeling_cb = ttk.Combobox(root, textvariable=selected_feeling)

# get first 3 letters of every month name
feeling_cb['values'] = ['Happy', 'Sad', 'Angry']

# prevent typing a value
feeling_cb['state'] = 'readonly'

# place the widget
feeling_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_feeling.get()}!'
    )


feeling_cb.bind('<<ComboboxSelected>>', month_changed)

# Label for combobox
label_cb = "Choose a feeling from the dropdown menu"
feeling_cb.set(label_cb)

root.mainloop()