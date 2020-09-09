import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image


root = tk.Tk()
root.resizable(width=False, height=False)

path_input = tk.StringVar()


def second_win():
    window = tk.Tk()
    window.title("welcome to the second window")


def extract():
    print("extracted")
    print(path_input.get())

def csv_extractor():
    if len(path_input.get())!= 0:
        extract() 
    else:
        print("no input ") 

root.geometry("1200x700")
root.title("watchtower")





name_label = tk.Label(root,text ="WATCHTOWER ", bg="sky blue",fg = "Dark Blue", font =("Gadugi",30)  )
name_label.pack(side ="top", fill = "x")



entry_label = tk.Label(root, text= "ENTER THE FILE PATH:",font =("Times",21,"bold"), bg ="light grey")
entry_label.pack(side = "left",padx=(0,5),pady = (5,5),fill ="both")





name_entry = ttk.Entry(root, width = 100 ,textvariable = path_input,)
name_entry.focus()
name_entry.pack(side = "left")

entry_button = tk.Button(root,text = "ENTER ",bd=4,command = csv_extractor)
entry_button.place(x=500,y=450)




root.mainloop()