from tkinter import *
import os
root=Tk()
root.geometry("700x540")
root.resizable(False,False)
Label(root,relief=SUNKEN).pack(side=BOTTOM,fill=X)
def run_fac():
     path='C:/Users/AdityaGarg/OneDrive/Desktop/teachers.py'
     os.system(f'python {path}')
def run_stud():
     path='C:/Users/AdityaGarg/OneDrive/Desktop/student_details.py'
     os.system(f'python {path}')
def run_sub():
     path='C:/Users/AdityaGarg/OneDrive/Desktop/subjects_details.py'
     os.system(f'python {path}')
Label(root,text="A D M I N I S T R A T O R",font=("Arial",40,"bold"),padx=15,pady=15,border=0,relief=GROOVE,bg="teal",foreground="white").pack(side=TOP,fill=X)
mframe = LabelFrame(text='Modify', font=('Consolas'), padx=20)
mframe.place(x=50, y=100)

b1=Button(mframe,text="Students",font=('arial',20),command=run_stud).grid(row=0,column=0,padx=30,pady=30)
b2=Button(mframe,text="Faculties",font=('arial',20),command=run_fac).grid(row=0,column=1,padx=30)
b3=Button(mframe,text="Subjects",font=('arial',20),command=run_sub).grid(row=0,column=2,padx=30)

ttframe = LabelFrame(text='TimeTable', font=('Consolas'), padx=20)
ttframe.place(x=50, y=280)

Button(ttframe,text="Courses",font=('arial',20)).grid(row=0,column=0,padx=20,pady=30)
Button(ttframe,text="Faculty",font=('arial',20)).grid(row=0,column=1,padx=20)
Button(ttframe,text="Schedule-periods",font=('arial',20)).grid(row=0,column=2,padx=20)

Button(root,text='Quit',font=('Consolas'),command=root.destroy,width=15,pady=10,bg="teal",fg="white").place(x=250, y=450)
root.mainloop()