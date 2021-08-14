from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    kilo_result.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

kilo_result = Label(text="0")
kilo_result.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)



window.mainloop()