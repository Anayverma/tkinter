import tkinter as tk
from tkinter import messagebox

root=tk.Tk()

messagebox.showerror("Error_title","you have definelty errored")
messagebox.showwarning("warning_title","you have definelty warned")
messagebox.showinfo("info_title","you have definelty informed")


tk.mainloop()
