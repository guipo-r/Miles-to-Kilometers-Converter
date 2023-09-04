from tkinter import *


# Conversion function
def conversion():
    miles = float(input1.get())
    kms = round(miles * 1.609344, 2)
    converted_label.config(text=f"{kms}", font=("Arial", 10, "bold"))


# Window
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)  # Minimum size, it can be bigger if we add things in it
window.config(padx=40, pady=40)

# Miles Entry
input1 = Entry(width=8)
input1.grid(column=1, row=0)

# "Miles" text
miles_label = Label(text='Miles', font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

# "Is equal to" text
equal_to_label = Label(text='is equal to', font=("Arial", 10, "bold"))
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=5, pady=10)

# Kms count text
converted_label = Label(text='0', font=("Arial", 10, "bold"))
converted_label.grid(column=1, row=1)

# "Km" text
km_label = Label(text='Km', font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

# Calculate Button
button = Button(text='Calculate', command=conversion)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)




window.mainloop()  # Keeps the window on screen