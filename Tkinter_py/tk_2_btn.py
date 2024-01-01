import tkinter as tk
root=tk.Tk()
root.geometry("5000x5000")
root.title("GUI using tkinter")
root.configure(bg="lightblue")
def on_Click_Command():
    print("Button clicked")
    # flat, groove, raised, ridge, solid, or sunken
btn1=tk.Button(root,text="btn-1",command=on_Click_Command,font=('Arial'),anchor="n",fg="red",bg="yellow",relief="raised")
btn1.pack(fill="x")

root.mainloop()
