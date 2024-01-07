from tkinter import *

def prifac():
    l=list(map(int,e1.get("1.0", "end-1c").split(' ')))
    x=""
    for i in range(l[0],l[1]):
        c=0
        # print(i)
        for j in range(2,i):
            if i % j == 0:
                c+=1
                break
        if c==0:
            x=x+" , "+str(i)
            if len(x) == 5:
                r1.insert("end",x+"\n")
                x=""
    r1.insert("end",x+"\n")
    

def calc():
    s=e2.get("1.0","end-1c")
    r2.insert("end",str(eval(s))+"\n")

def calculator_disp(l):
    c=ec.get()
    if l=='c':
        ec.delete(0,'end')
    elif l=='d':
        ec.delete(len(c)-1,'end')
    else:
        ec.insert("end",l)
def evalcalc():
    expression = ec.get()
    try:
        result = eval(expression)
        ec.delete(0, 'end')
        ec.insert('end', str(result))
    except Exception as e:
        ec.delete(0, 'end')
        ec.insert('end', "Error")



root=Tk()
root.geometry("2000x700")
root.configure(bg="lightblue")
vl=IntVar()
l1=Label(root,text="Prime numbers",width=30,height=5)
l1.grid(row=0,column=0,padx=10,pady=10)

e1=Text(root,width=28,height=5)
e1.grid(row=0, column=1)

b1=Button(root,text="Find",command=prifac,width=10,height=5)
b1.grid(row=0,column=2,padx=10,pady=10)

r1=Listbox(root,width=50,height=5)
r1.grid(row=0,column=3,padx=10,pady=10)


l2=Label(root,text="Calculator",width=30,height=5)
l2.grid(row=1,column=0,padx=10,pady=10)

e2=Text(root,width=28,height=5)
e2.grid(row=1, column=1)

b2=Button(root,text="Find",command=calc,width=10,height=5)
b2.grid(row=1,column=2,padx=10,pady=10)

r2=Text(root,width=50,height=5)
r2.grid(row=1,column=3,padx=10,pady=10)




clcl=Label(root,text="CALCULATOR",width=80,height=5,bg="blue",fg="white",font=('Cooperblack'))
# clcl.place(x=10,y=10,anchor="s")
clcl.grid(row=3,padx=20,columnspan=4)
ec=Entry(root)
ec.grid(row=4,column=0,padx=5,pady=5)

mcb=Button(root,text="Calculate",fg="white",bg="black",command=evalcalc)
mcb.grid(row=4,column=3)

l=[["c","%","d","/"],["7","8","9","*"],["4","5","6","-"],["1","2","3","+"],["00","0","(",")"]]
for i in range(0,5):
    for j in range(0,4):
        lc=Button(root,text=l[i][j],width=5,height=2,command=lambda var=l[i][j]:calculator_disp(var))
        lc.grid(row=5+i,column=0+j,padx=1,pady=1)


root.title("Master Program")
root.mainloop()