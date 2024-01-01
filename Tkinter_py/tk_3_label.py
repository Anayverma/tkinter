# import tkinter as tk

# root=tk.Tk()
# root.geometry("500x500")
# root.configure(bg="yellow")
# root.title("GUI-2-grid")

# lb1=tk.Label(root,text="THIS IS LABEL 1 ONE" ,fg="red",bg="lightblue",width=20,height=10,anchor="w",relief="sunken")
# # lb1.pack(side="bottom",anchor="e")
# lb2=tk.Label(root,text="THIS IS LABEL 2 ONE" ,fg="red",bg="lightblue",width=20,height=10,anchor="w",relief="sunken")
# lb3=tk.Label(root,text="THIS IS LABEL 3 ONE" ,fg="red",bg="lightblue",width=20,height=10,anchor="w",relief="sunken")
# lb4=tk.Label(root,text="THIS IS LABEL 4 ONE" ,fg="red",bg="lightblue",width=20,height=10,anchor="w",relief="sunken")
# lb5=tk.Label(root,text="THIS IS LABEL 5 ONE" ,fg="red",bg="lightblue",width=20,height=10,anchor="w",relief="sunken")  
# lb1.grid(row=0,column=0)
# lb2.grid(row=0,column=1)
# lb3.grid(row=1,column=0)
# lb4.grid(row=1,column=1)
# lb5.grid(row=0,column=2)



# root.mainloop()
import tkinter as tk

root = tk.Tk()

# Creating three labels and placing them in different columns
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3")
label3.grid(row=0, column=2)

# Creating another label with columnspan
label4 = tk.Label(root, text="Label 4 (Columnspan)", bg="yellow")
label4.grid(row=1, column=0, columnspan=2)

en1=tk.Entry(root)
en2=tk.Entry(root)
en1.grid(row=0,column=4)
en2.grid(row=1,columnspan=5)


root.mainloop()
