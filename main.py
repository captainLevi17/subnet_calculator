from tkinter import *

root = Tk()

def calculate():
    result = Label(root, text="Calculating...")
    result.grid(row=2, column=1)
    

header = Label(root, text="MLSG Subnet Calculator", fg="blue", font=("Helvetica", 16))
result = Label(root, text="")
calculateBtn = Button(root, text="Calculate", padx=10, pady=10 , command=calculate, fg="white", bg="blue")

header.grid(row=0, column=1)
calculateBtn.grid(row=1, column=1)

root.mainloop()