from tkinter import *

KM = 1.609344


def convert():
    miles = float(entry_box.get())
    km = round(miles * KM, 1)
    return_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(width=200, height=200, padx=20, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

return_label = Label(text=0)
return_label.grid(column=1, row=1)

entry_box = Entry(width=7)
entry_box.grid(column=1, row=0)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()
