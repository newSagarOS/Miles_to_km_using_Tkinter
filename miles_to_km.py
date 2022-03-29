from tkinter import *


def calculate():
    value = float(inp.get())
    in_km = value * 1.609
    answer.config(text=f"{in_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(pady=20, padx=20)


inp = Entry(width=7)
inp.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

tex = Label(text="is equal to")
tex.grid(column=0,row=1)

answer = Label(text="0")
answer.grid(column=1,row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)

window.mainloop()