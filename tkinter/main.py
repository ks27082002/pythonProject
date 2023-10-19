import tkinter
window = tkinter.Tk()
window.minsize(height=300, width=500)

label = tkinter.Label(text="I am Label")
label.pack()
def button_pressed():
    label["text"] = input.get()


button = tkinter.Button(text="Click me", command=button_pressed)
button.pack()

input = tkinter.Entry()
input.pack()



window.mainloop()