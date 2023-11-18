from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
root =Tk()
root.geometry("950x600")
root.resizable(False,False)
Label(root,text="Faculty Details ",font=("Arial",40,"bold"),padx=15,pady=15,border=0,relief=GROOVE,bg="teal",foreground="white").pack(side=TOP,fill=X)
Label(root,relief=SUNKEN).pack(side=BOTTOM,fill=X)
frame=LabelFrame(root,text="List of Faculties",font=("Arial",14),relief=GROOVE,width=400,height=500)
frame.place(x=485,y=120)
def clear():
    fid_entry.delete(0,END)
    passw_entry.delete(0,END)
    conf_passw_entry.delete(0,END)
    name_entry.delete(0,END)
    roll_entry.delete(0,END)
    sec_entry.delete(0,END)
    SEM_entry.delete(0,END)
def details():
    db=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Anuj@1310", database="anujdb")
    cursor=db.cursor()
    cursor.execute("select FID, NAME ,DEPT, FACULTY from faculty")
    result=cursor.fetchall()
    count=0
    for i in result:
        my_tree.insert(parent='',index='end',iid=count,text='',values=i)
        count+=1
    db.commit()
    db.close()
def update_treeview():
    for row in my_tree.get_children():
        my_tree.delete(row)
    db=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Anuj@1310", database="anujdb")
    cursor=db.cursor()
    cursor.execute("select FID, NAME,DEPT, FACULTY from faculty")
    result=cursor.fetchall()
    for row in result:
        my_tree.insert("",0,values=(row[0], row[1], row[2],row[3]))
    my_tree.place()
    db.commit()
    db.close()
def add_data():
    fid = str(fid_entry.get())
    passw = str(passw_entry.get())
    conf_passw = str(conf_passw_entry.get())
    name = str(name_entry.get())
    email = str(roll_entry.get())
    course = str(sec_entry.get())
    sem=str(SEM_entry.get())
    if fid == "" or passw == "" or \
        conf_passw == "" or name == "" or \
        email == "" or course == "" or sem=="":
        messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
        return

    if passw != conf_passw:
        messagebox.showerror("Passwords mismatch", "Password and confirm password didnt match. Try again!")
        passw_entry.delete(0, END)
        conf_passw_entry.delete(0, END)
        return
    messagebox.showinfo("Database","Successfully Inserted")
    update_treeview()
    fid_entry.delete(0, END)
    passw_entry.delete(0, END)
    conf_passw_entry.delete(0, END)
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    sec_entry.delete(0, END)
    SEM_entry.delete(0, END)
my_tree=ttk.Treeview(frame)
my_tree['columns']=("ID","Name","Department","Subject")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Name",width=150)
my_tree.column("ID",anchor=CENTER,width=110)
my_tree.column("Department",width=100)
my_tree.column("Subject",width=90)

my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Subject",text="Course",anchor=W)
my_tree.heading("Department",text="Department",anchor=W)
my_tree['height'] = 20
details()
my_tree.pack()
def show_passw():
    if passw_entry['show'] == "●":
        passw_entry['show'] = ""
        B1_show['text'] = '●'
        B1_show.update()
    elif passw_entry['show'] == "":
        passw_entry['show'] = "●"
        B1_show['text'] = '○'
        B1_show.update()
    passw_entry.update()
fr=LabelFrame(root,text="Add/Update Details",font=("Arial",14),relief=GROOVE).place(x=40,y=120,width=420,height=450)
Label(fr,text='Faculty id:',font=('Consolas', 12)).place(x=50, y=160)
fid_entry = Entry(fr,font=('Consolas', 12),width=20)
fid_entry.place(x=200, y=160)
Label(fr,text='Password:',font=('Consolas', 12)).place(x=50, y=200)
passw_entry = Entry(fr,font=('Consolas', 12),width=20,show="●")
passw_entry.place(x=200, y=200)
B1_show = Button(fr,text='○',font=('Consolas', 8, 'bold'),command=show_passw,width=3)
B1_show.place(x=390,y=200)
Label(fr,text='Confirm Password:',font=('Consolas', 12)).place(x=50, y=250)
conf_passw_entry = Entry(fr,font=('Consolas', 12),width=20,show="●")
conf_passw_entry.place(x=200, y=250)
Label(fr,text='Faculty Name:',font=('Consolas', 12)).place(x=50, y=290)
name_entry = Entry(fr,font=('Consolas', 12),width=20,)
name_entry.place(x=200, y=290,relx=0)
Label(fr,text='Email:',font=('Consolas', 12)).place(x=50, y=330)
roll_entry = Entry( fr, font=('Consolas', 12), width=20,)
roll_entry.place(x=200, y=330)
Label(fr,text='Course:',font=('Consolas', 12)).place(x=50, y=370)
sec_entry = Entry(fr,font=('Consolas', 12),width=20)
sec_entry.place(x=200, y=370)

Label(fr,text='Current Sem:',font=('Consolas', 12)).place(x=50, y=410)
SEM_entry = Entry(fr,font=('Consolas', 12),width=5)
SEM_entry.place(x=200, y=410)
B1 = Button(fr,text='Add Faculty',font=('Consolas', 12),bg="teal",fg="white",command=add_data)
B1.place(x=80,y=470)
B2 = Button(fr,text='Update Faculty',font=('Consolas', 12),bg="teal",fg="white")
B2.place(x=240,y=470)
B3 = Button(fr,text='Delete Faculty(s)',font=('Consolas', 12),bg="teal",fg="white",command=exit)
B3.place(x=80,y=520)
Button(fr,text="Clear",font=('Consolas', 12),bg="teal",fg="white",command=clear,width=10).place(x=280,y=520)
mainloop()