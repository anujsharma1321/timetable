from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def clear():
    scode_entry.delete(0,END)
    sname_entry.delete(0,END)
    radio_var.set('L')
def update_treeview():
    for row in my_tree.get_children():
        my_tree.delete(row)
    db=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Anuj@1310", database="anujdb")
    cursor=db.cursor()
    cursor.execute("select SUBCODE, SUBNAME,SUBTYPE from SUBJECTS")
    result=cursor.fetchall()
    count=0
    for i in result:
        my_tree.insert(parent='',index='end',iid=count,text='',values=i)
        count+=1
    my_tree.place()
    db.commit()
    db.close()
def add():
    subcode = str(scode_entry.get()).upper()
    subname = str(sname_entry.get()).upper()
    subtype = str(radio_var.get()).upper()
    if subtype=='L':
        subtype="LECTURE"
    if subtype=='P':
        subtype="PRACTICAL"
    if subtype=='T':
        subtype="TUTORIAL"
    if subcode=="":
        subcode = None
    if subname=="":
        subname = None

    if subcode is None or subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        scode_entry.delete(0, END)
        sname_entry.delete(0, END)
        return
    db=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Anuj@1310", database="anujdb")
    cursor=db.cursor()
    cursor.execute(f"INSERT INTO SUBJECTS VALUES ('{subcode}','{subname}','{subtype}')")
    db.commit()
    update_treeview()
    scode_entry.delete(0, END)
    sname_entry.delete(0, END)

def details():
    db=pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="Anuj@1310", database="anujdb")
    cursor=db.cursor()
    cursor.execute("select SUBCODE, SUBNAME,SUBTYPE from SUBJECTS")
    result=cursor.fetchall()
    count=0
    for i in result:
        my_tree.insert(parent='',index='end',iid=count,text='',values=i)
        count+=1
    db.commit()
    db.close()
root=Tk()
root.geometry("900x510")
root.resizable(False,False)
Label(root,text="Subjects Details",font=("Arial",40,"bold"),padx=15,pady=15,border=0,relief=GROOVE,bg="teal",foreground="white").pack(side=TOP,fill=X)
Label(root,relief=SUNKEN).pack(side=BOTTOM,fill=X)
frame=LabelFrame(root,text="List of Subjects",font=("Arial",14),relief=GROOVE,width=400,height=500)
frame.place(x=470,y=120)
my_tree=ttk.Treeview(frame)
my_tree['columns']=("ID","Name","Batch")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Name",width=190)
my_tree.column("ID",anchor=CENTER,width=120)
my_tree.column("Batch",width=100)

my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Code",anchor=W)
my_tree.heading("ID",text="Name",anchor=CENTER)
my_tree.heading("Batch",text="Type",anchor=W)
my_tree['height'] = 15
details()
my_tree.pack()
fr=LabelFrame(root,text="Add/Update Details",font=("Arial",14),relief=GROOVE).place(x=40,y=120,width=420,height=352)
Label(fr,text='Subject Code:',font=('Consolas', 12),).place(x=50, y=160)
scode_entry = Entry(fr,font=('Consolas', 12),width=20)
scode_entry.place(x=200, y=160)
Label(fr,text='Subject Name:',font=('Consolas', 12)).place(x=50, y=210)
sname_entry = Entry(fr,font=('Consolas', 12),width=20)
sname_entry.place(x=200, y=210)
Label(fr,text='Subject Type:',font=('Consolas', 12)).place(x=50, y=260)
radio_var = StringVar()
R1 = Radiobutton(fr,text='Lecture',font=('Consolas', 12),variable=radio_var,value="L")
R1.place(x=190, y=260)
R1.select()
R2 = Radiobutton(fr,text='Practical',font=('Consolas', 12),variable=radio_var,value="P")
R2.place(x=190, y=290)
R2.select()
R3 = Radiobutton(fr,text='Tutorial',font=('Consolas', 12),variable=radio_var,value="T")
R3.place(x=190, y=320)
R3.select()
B1 = Button(fr,text='Add Subject',font=('Consolas', 12),bg="teal",fg="white",command=add)
B1.place(x=80,y=380)
B2 = Button(fr,text='Update Subject',font=('Consolas', 12),bg="teal",fg="white")
B2.place(x=240,y=380)
B3 = Button(fr,text='Delete Subject(s)',font=('Consolas', 12),bg="teal",fg="white",command=exit)
B3.place(x=80,y=430)
Button(fr,text="Clear",font=('Consolas', 12),bg="teal",fg="white",command=clear,width=10).place(x=280,y=430)
root.mainloop()