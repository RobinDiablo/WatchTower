import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import csv
from tkinter import filedialog


root = tk.Tk()
root.resizable(width=False, height=False)
root.configure(background='white')

fulldate={}
complete_date=[]

path_input = tk.StringVar()

def extract():
    print("extraced")
    print(path_input.get())



def csv_extractor():
    if len(path_input.get())!= 0:
        extract()
        root.destroy()
    else:
        messagebox.showwarning("Warning", "ENTER A CORRECT PATH")

def openfn():
    filename = filedialog.askopenfilename(title='open csv')
    path_input.set(filename)        


root.geometry("1200x700")
root.title("EXCEL SCANNER ")




name_label = tk.Label(root,text ="EXCEL SCANNER  ", bg="sky blue",fg = "Dark Blue", font =("Gadugi",30)  )
name_label.pack(side="top", fill="x")


entry_label = tk.Label(root, text= "ENTER THE FILE PATH:", font =("Times",17), fg ="blue")
entry_label.place(x=480,y=350)


name_entry = ttk.Entry(root, width = 100 ,textvariable = path_input)
name_entry.focus()
name_entry.place(x=300,y=410)

entry_button = tk.Button(root,text = "ENTER ",bd=4,padx=10,pady=3,font="20",command = csv_extractor)
entry_button.place(x=630,y=510)



btn = tk.Button(root, text='BROWSE',bd=4,padx=10,pady=3,font="20", command=openfn)
btn.place(x='480',y='510')


root.mainloop()

