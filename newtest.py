import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import csv

creation_list=[]
Deleted_files=[]
Deleted_files_names=[]
modified_files=[]
global tex 
global v

root = tk.Tk()
root.resizable(width=False, height=False)
def extract():
    print("extraced")
    print(path_input.get())



    

path_input = tk.StringVar()


def csv_extractor():
    if len(path_input.get())!= 0:
        extract()
        second_win() 
        root.destroy()
    else:
        messagebox.showwarning("Warning", "ENTER A CORRECT PATH")


root.geometry("1200x700")
root.title("watchtower")





name_label = tk.Label(root,text ="WATCHTOWER ", bg="sky blue",fg = "Dark Blue", font =("Gadugi",30)  )
name_label.pack(side ="top", fill = "x")



entry_label = tk.Label(root, text= "ENTER THE FILE PATH:",font =("Times",21,"bold"), bg ="light grey")
entry_label.pack(side = "left",padx=(0,5),pady = (5,5),fill ="both")





name_entry = ttk.Entry(root, width = 100 ,textvariable = path_input)
name_entry.focus()
name_entry.pack(side = "left")

entry_button = tk.Button(root,text = "ENTER ",bd=4,command = csv_extractor)
entry_button.place(x=500,y=450)




fulldate={}
complete_date=[]

def clickbut_year(number):
    year = number 
    fulldate["YEAR"]=year
    print(year)
def clickbut_date(number):
    date = number 
    fulldate["DATE"]=date
    print(date)
def clickbut_month(number):
    month = number 
    fulldate["MONTH"]=month
    print(month) 

def overall_date():
    fulldate["MONTH"]=int(fulldate["MONTH"])
    fulldate["DATE"]=int(fulldate["DATE"])
    
    if fulldate["DATE"]<10:
        fulldate["DATE"]=str(fulldate["DATE"])
        fulldate["DATE"]=fulldate["DATE"].zfill(2)
    if fulldate["MONTH"]<10:
        fulldate["MONTH"]=str(fulldate["MONTH"])
        fulldate["MONTH"]=fulldate["MONTH"].zfill(2)
    main_date=str(fulldate["YEAR"])+"-"+str(fulldate["MONTH"])+"-"+str(fulldate["DATE"])
    return main_date
    





def second_win():
    window = tk.Tk()
    window.title("welcome to the second window")
    window.geometry("1200x700")
    window.title('watchtower')
    window.resizable( height="false",width="false")
    labelTitle = tk.Label(window,text="WatchTower",bg='powder blue',fg='dark blue')
    labelTitle.pack(fill="x")




    canvas=tk.Canvas(window,width=1200,height=700)
    canvas.pack(side='left')
    blackline=canvas.create_line(180,10,180,700)
    box=canvas.create_rectangle(200,10,1190,500,fill="light gray")
    box=canvas.create_rectangle(200,510,1190,660,fill="powder blue")
    blackline=canvas.create_line(203,430,1190,430)
    v= tk.IntVar()



    def destroy_Second_window():
        
        window.destroy()
        temporary=overall_date()
        print(temporary)
        complete_date.append(temporary)
        file_extractor()
        
    
    
    
    
    def file_extractor():
        count=0
        count1=0
        count2=0
        flag=0
        flag1=0
        filename = path_input.get()
        with open(filename,"r",encoding="utf8") as csvfile:
             csv_reader = csv.reader(csvfile)
             next(csv_reader)
             for col in csv_reader:
                temp=col[18].split(" ")
                creation_list.append(temp)
                xyz=col[20].split(" ")
                modified_files.append(xyz)
                if col[12] == "DELETED":
                   temp2 = col[21].split(" ")
                   temp2.append(col[10])
                   Deleted_files.append(temp2)
             
        for r in range(0,len(creation_list)):
             if complete_date[0]==creation_list[r][0]:
                count=count+1
                flag=1
        for r in range(0,len(modified_files)):
            if complete_date[0]==modified_files[r][0]:
                count2=count2+1
                flag1=1
        if flag==1:
            print("Number of created Files:",count)
        else:
            print("No File was created")
        if flag1==1:
            print("Number of modified files:",count2)
        else:
            print("No file was modified")
#|-----------------------DELETED FILES-------------------------------|
        flag=0
        for r in range(0,len(Deleted_files)):
            if complete_date[0]==Deleted_files[r][0]:
                count1=count1+1
                flag=1
                Deleted_files_names.append(Deleted_files[r][2])
        
        if flag==1:
            print("Number of files deleted",count1)

        else:
            print("No File was deleted")
        view_File(count,count1,count2,v)
        


           






    topframe=tk.Frame(window,height=150,bg='powder blue',bd=5)
    topframe.pack(side="top",fill="x")
    leftframe=tk.Frame(window,height=550,width=400,bg='light green',bd=5)
    leftframe.pack(side="left")
    rightframe=tk.Frame(window,height=550,width=800,bg='white',bd=5)
    rightframe.pack(side="right")







#********************************************************** months ****************************************************************


    but1 = tk.Button(window, padx=30, pady=7, bd=2, bg='dark gray', text="JANUARY",font=("Courier New", 15, 'bold'),command =lambda: clickbut_month(1) )
    but1.place(x=5, y=24)
    but1 = tk.Button(window, padx=24, pady=7, bd=2, bg='dark gray', text="FEBRUARY",font=("Courier New", 15, 'bold'),command = lambda: clickbut_month(2))
    but1.place(x=5, y=80)
    but1 = tk.Button(window, padx=42, pady=7, bd=2, bg='dark gray', text="MARCH",font=("Courier New", 15, 'bold'), command = lambda: clickbut_month(3) )
    but1.place(x=5, y=136)
    but1 = tk.Button(window, padx=43, pady=7, bd=2, bg='dark gray', text="APRIL",font=("Courier New", 15, 'bold'), command = lambda: clickbut_month(4) )
    but1.place(x=5, y=192)
    but1 = tk.Button(window, padx=55, pady=7, bd=2, bg='dark gray', text="MAY",font=("Courier New", 15, 'bold'), command =lambda: clickbut_month(5) )
    but1.place(x=5, y=248)
    but1 = tk.Button(window, padx=49, pady=7, bd=2, bg='dark gray', text="JUNE",font=("Courier New", 15, 'bold') , command = lambda: clickbut_month(6))
    but1.place(x=5, y=304)
    but1 = tk.Button(window, padx=49, pady=7, bd=2, bg='dark gray', text="JULY",font=("Courier New", 15, 'bold'), command = lambda: clickbut_month(7))
    but1.place(x=5, y=360)
    but1 = tk.Button(window, padx=38, pady=7, bd=2, bg='dark gray', text="AUGUST",font=("Courier New", 15, 'bold'),command = lambda: clickbut_month(8))
    but1.place(x=5, y=416)
    but1 = tk.Button(window, padx=19, pady=7, bd=2, bg='dark gray', text="SEPTEMBER",font=("Courier New", 15, 'bold'), command = lambda: clickbut_month(9))
    but1.place(x=5, y=472)
    but1 = tk.Button(window, padx=31, pady=7, bd=2, bg='dark gray', text="OCTOBER",font=("Courier New", 15, 'bold'), command =lambda: clickbut_month(10) )
    but1.place(x=5, y=528)
    but1 = tk.Button(window, padx=25, pady=7, bd=2, bg='dark gray', text="NOVEMBER",font=("Courier New", 15, 'bold'), command =lambda: clickbut_month(11) )
    but1.place(x=5, y=584)
    but1 = tk.Button(window, padx=25, pady=7, bd=2, bg='dark gray', text="DECEMBER",font=("Courier New", 15, 'bold'), command = lambda: clickbut_month(12))
    but1.place(x=5, y=642)



#********************************************************************** dates *************************************************************
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="1",font=("Courier New", 15, 'bold'), command =lambda: clickbut_date(1) )
    but1.place(x=860, y=48)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="2",font=("Courier New", 15, 'bold'), command =lambda: clickbut_date(2) )
    but1.place(x=940, y=48)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="3",font=("Courier New", 15, 'bold'), command = lambda: clickbut_date(3))
    but1.place(x=1020, y=48)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="4",font=("Courier New", 15, 'bold'), command =lambda: clickbut_date(4) )
    but1.place(x=1100, y=48)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="5",font=("Courier New", 15, 'bold'), command = lambda: clickbut_date(5))
    but1.place(x=300, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="6",font=("Courier New", 15, 'bold'), command =lambda: clickbut_date(6) )
    but1.place(x=380, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="7",font=("Courier New", 15, 'bold'), command =lambda: clickbut_date(7) )
    but1.place(x=460, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="8",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(8))
    but1.place(x=540, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="9",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(9))
    but1.place(x=620, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="10",font=("Courier New", 15, 'bold'), command = lambda: clickbut_date(10))
    but1.place(x=700, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="11",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(11))
    but1.place(x=780, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="12",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(12))
    but1.place(x=860, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="13",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(13))
    but1.place(x=940, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="14",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(14))
    but1.place(x=1020, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="15",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(15))
    but1.place(x=1100, y=150)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="16",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(16))
    but1.place(x=300, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="17",font=("Courier New", 15, 'bold'), command = lambda: clickbut_date(17))
    but1.place(x=380, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="18",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(18))
    but1.place(x=460, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="19",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(19))
    but1.place(x=540, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="20",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(20))
    but1.place(x=620, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="21",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(21))
    but1.place(x=700, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="22",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(22))
    but1.place(x=780, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="23",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(23))
    but1.place(x=860, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="24",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(24))
    but1.place(x=940, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="25",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(25))
    but1.place(x=1020, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="26",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(26))
    but1.place(x=1100, y=250)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="27",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(27))
    but1.place(x=300, y=350)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="28",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(28))
    but1.place(x=380, y=350)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="29",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(29))
    but1.place(x=460, y=350)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="30",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(30))
    but1.place(x=540, y=350)
    but1 = tk.Button(window, padx=15, pady=15, bd=2, bg='light blue', text="31",font=("Courier New", 15, 'bold'), command = lambda:clickbut_date(31))
    but1.place(x=620, y=350)
    







#******************************************************************year**************************************************************************************#    
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2014",font=("Courier New", 15, 'bold'),command = lambda: clickbut_year(2014))
    but1.place(x=300, y=470)
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2015",font=("Courier New", 15, 'bold'),command = lambda:clickbut_year(2015))
    but1.place(x=400, y=470)
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2016",font=("Courier New", 15, 'bold'),command = lambda:clickbut_year(2016))
    but1.place(x=500, y=470)
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2017",font=("Courier New", 15, 'bold'),command = lambda:clickbut_year(2017))
    but1.place(x=600, y=470)
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2018",font=("Courier New", 15, 'bold'),command = lambda:clickbut_year(2018))
    but1.place(x=700, y=470)
    but1 = tk.Button(window, padx=15, pady=3, bd=2, bg='dark gray', text="2019",font=("Courier New", 15, 'bold'),command = lambda:clickbut_year(2019))
    but1.place(x=800, y=470)


    but1 = tk.Button(window, padx=5, pady=2, bd=2, bg='dark gray', text="NEXT ",font=("Courier New", 15) , command = destroy_Second_window)
    but1.place(x=1100, y=630)






def view_File(count,count1,count2,v):
    


    window1=tk.Tk()
    window1.geometry("1200x700")
    window1.title('watchtower')
    window1.resizable(height="false", width="false")
    labelTitle = tk.Label(window1, text="WatchTower", bg='powder blue', fg='dark blue')
    labelTitle.pack(fill="x")

    
    but2 = tk.Button(window1, text='Quit', font="Arial 8 bold ", activebackground="powder blue", width=20, height=5,command=window1.quit)
    but2.place(x=1025, y=610)

    
    tex = tk.Listbox(master=window1,width=180,height=37,bg='light gray',font=('Arial', 8, 'bold'),bd='7')
    tex1 = tk.Listbox(master=window1, width=40, height=4, bg='light gray', font=('Arial', 8, 'bold'), bd='7')


    scr=tk.Scrollbar(window1, orient='vertical', command=tex.yview, width=20, highlightcolor='powder blue', troughcolor='dark gray',elementborderwidth='6',activebackground='powder blue')
    scr.place(x=1125,y=30)
    tex.place(x=30,y=30)
    tex.config(yscrollcommand=scr.set, font=('Arial', 8, 'bold', 'italic'))
   
    for i in Deleted_files_names:
        tex.insert('end', i + "\n")

    x = count 
    y = count1 
    z = count2
    var1 = tk.StringVar()
    var1.set(f"No. of files  created = {x}")
    var2 = tk.StringVar()
    var2.set(f"No. of files modified  = {z}")
    var3 = tk.StringVar()
    var3.set(f"No. of files deleted = {y}")
    tex1.insert('active', f" no. of files created {count}")
    tex1.insert('anchor', f" no. of files modified {count2}")
    tex1.insert('end', f" no. of files deleted {count1}")





           
    but2 = tk.Button(window1, text='Quit', font="Arial 8 bold ", activebackground="powder blue", width=20, height=5,command=window1.quit)
    but2.place(x=1025, y=610)


root.mainloop()
