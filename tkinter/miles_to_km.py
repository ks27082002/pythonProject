import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=400)
window.title("miles to km")
window.config(padx=20, pady=20)

def find():

    label2.config(text=int(float(entry.get())*1.6 ))

label1 = tkinter.Label(text= "is equal to")
label1.grid(row=1, column=0)
label2 = tkinter.Label(text="0")
label2.grid(row=1, column=1)
label3 = tkinter.Label(text="km")
label3.grid(row=1, column=2)
label4 = tkinter.Label(text="miles")
label4.grid(row=0, column=2)

entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)
button = tkinter.Button(text="Calculate", command=find)
button.grid(row=2, column=1)











window.mainloop()