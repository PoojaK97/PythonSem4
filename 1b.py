from tkinter import *
def up():
    v.set(v.get()+1)
def down():
    v.set(v.get()-1)
root=Tk()
v=IntVar()
v.set(0)
b1=Button(root,text='UP',command=up).pack()
b2=Button(root,text='DOWN',command=down).pack()
l=Label(root,textvariable=v).pack(side=BOTTOM)
root.mainloop()
