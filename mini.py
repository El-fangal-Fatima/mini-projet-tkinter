from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Employee.db")




root = Tk()
root.title('mini projet en python')
root.geometry('1210x615+0+0')
root.resizable(False,False)
root.configure(bg='#343535')

# logo = PhotoImage(file='images(1).jpg')
# lbl_logo=Label(root, image=logo)
# lbl_logo.place(x=80,y=520)

name = StringVar()
filier = StringVar()
sexe = StringVar()
CEF = StringVar()
Email = StringVar()
Id = StringVar()




#fram
entries_frame = Frame(root, bg='#343535')
entries_frame.place(x=1,y=1 ,width=360 ,height=510)
title=Label(entries_frame,text='stagaire',font=('Calibri',18,'bold'),background='#343535',fg='#DCDCDC')
title.place(x=10,y=1)

lblname=Label(entries_frame,text="Name",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblname.place(x=10,y=50)
txtName=Entry(entries_frame ,textvariable=name,width=20, font=('Calibri',15,))
txtName.place(x=120,y=50)

lblfil=Label(entries_frame ,text="Filier" ,font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblfil.place(x=10,y=90)
txtfil=Entry(entries_frame ,textvariable=filier,width=20, font=('Calibri',15,))
txtfil.place(x=120,y=90)

lblsexe=Label(entries_frame,text="sexe",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblsexe.place(x=10,y=130)
sexe= ttk.Combobox(entries_frame ,textvariable=sexe,state='readonly',width=18 ,font=('Calibri',15))
sexe['values'] = ("male",'Female')
sexe.place(x=120 ,y=130)

lblCEF=Label(entries_frame,text="CEF",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblCEF.place(x=10,y=170)
txtCEF=Entry(entries_frame ,textvariable=CEF,width=20, font=('Calibri',15,))
txtCEF.place(x=120,y=170)

lblmail = Label(entries_frame,text="Email",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblmail.place(x=10,y=210)
txtmail = Entry(entries_frame ,textvariable=Email,width=20, font=('Calibri',15,))
txtmail.place(x=120,y=210)

lblID = Label(entries_frame,text="Id",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lblID.place(x=10,y=250)
txtID = Entry(entries_frame ,textvariable=Id,width=20, font=('Calibri',15,))
txtID.place(x=120,y=250)

lbladd = Label(entries_frame,text="address : ",font=('Calibri',15),background='#343535',fg='#DCDCDC')
lbladd.place(x=10,y=290)
txtadd = Text(entries_frame,width=30 ,height=2 ,font=('Calibri',15))
txtadd.place(x=10,y=330)

#===== dif =====

def hide():
    root.geometry("360x530")
def show():
    root.geometry('1210x615+0+0')
btnhide = Button(entries_frame , text='HIDE', bg='white' ,bd=1 , relief=SOLID ,cursor="hand2" , command=hide)
btnhide.place(x=200, y=10)
btnshow = Button(entries_frame , text='SHOW',bg='white' ,bd=1 , relief=SOLID , cursor="hand2" , command=show)
btnshow.place(x=270 , y=10)


def getData(event) :
    seleted_row = tv.focus()
    data = tv.item(seleted_row)
    global row
    row = data["values"]
    name.set(row[1])
    filier.set(row[2])
    sexe.set(row[3])
    CEF.set(row[4])
    Email.set(row[5])
    Id.set(row[6])
    txtadd.delete(1.0, END)
    txtadd.insert(END ,row[7])

def delete() :
    db.remove(row[0])
    Clear()
    displayAll()

def Clear():
    name.set("")
    filier.set("")
    sexe.set("")
    CEF.set("")
    Email.set("")
    Id.set("")
    txtadd.delete(1.0,END)

def update():
    if txtName.get()=="" or txtfil.get()== "" or sexe.get()=="" or txtCEF.get()=="" or txtID.get()=="" or txtmail.get()=="" or txtadd.get(1.0,END)== "" :
        messagebox.showerror("errore"," les formation ")
        return
    db.update(row[0],
        txtName.get(),
        txtfil.get() ,
        sexe.get(),
        txtCEF.get(),
        txtmail.get(),
        txtID.get(),
        txtadd.get(1.0,END))
    messagebox.showinfo('success',"Sure ??")
    Clear()
    displayAll()





def displayAll():
    tv.delete(*tv.get_children())
    for row in db .fetch():
        tv.insert("" ,END,values=row)

def add_employee():
    if txtName.get()=="" or txtfil.get()== "" or sexe.get()=="" or txtCEF.get()=="" or txtID.get()=="" or txtmail.get()=="" or txtadd.get(1.0,END)== "" :
        messagebox.showerror("errore","  les formation ? ")
        return
    
    db.insert(
        txtName.get(),
        txtfil.get() ,
        sexe.get(),
        txtCEF.get(),
        txtmail.get(),
        txtID.get(),
        txtadd.get(1.0,END)
        
        )
    messagebox.showinfo("Succes","ajoutez nouvaux stagaire")
    Clear()
    displayAll()



#btn
btn_frame = Frame(entries_frame,bg="#343535",relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btnADD = Button(btn_frame ,
                text='ajouter',
                width=14,
                height=1,
                font=('Calibri',15),
                fg = 'white',
                bg='#3D9F78',
                bd=0 ,
                command=add_employee
            ).place(x=4  , y=5)

btnEdit = Button(btn_frame ,
                text='Edit',
                width=14,
                height=1,
                font=('Calibri',15),
                fg = 'white',
                bg='#2980b9',
                bd=0 ,
                command=update 
            ).place(x=4  , y=50)

btnsup = Button(btn_frame ,
                text='suprimer',
                width=14,
                height=1,
                font=('Calibri',15),
                fg = 'white',
                bg='#FA3737',
                bd=0,
                command=delete
            ).place(x=170 , y=5)

btnClear = Button(btn_frame ,
                text='clear',
                width=14,
                height=1,
                font=('Calibri',15),
                fg = 'white',
                bg='#C79F4B',
                bd=0,
                command=Clear
            ).place(x=170  , y=50)



# TABLE
tree_frame = Frame(root , bg='black')
tree_frame.place(x=365 ,y=1, width=875 , height=610)

style=ttk.Style()
style.configure("mystyle.Treeview", font=('calibri',13) ,rowheight=50)
style.configure( "mystyle.Treeview.Heading",font=('calibri',13))
tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1" ,text="N")
tv.column("1" , width="30")
tv.heading("2" ,text="Name")
tv.column("2" , width="140")
tv.heading("3" ,text="Filier")
tv.column("3" , width="70")
tv.heading("4" ,text="Sexe")
tv.column("4" , width="60")
tv.heading("5" ,text="CEF")
tv.column("5" , width="140")
tv.heading("6" ,text="Email")
tv.column("6" , width="160")
tv.heading("7" ,text="Id")
tv.column("7" , width="90")
tv.heading("8" ,text="Adress")
tv.column("8" , width="170")
tv['show']= 'headings'

tv.bind("<ButtonRelease-1>" , getData)

tv.place(x=1 ,y=1 ,height=610)

displayAll()


root.mainloop()