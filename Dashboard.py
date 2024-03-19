from tkinter import *
from PIL import Image, ImageTk

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="white")

        # title
        self.icon_tittle = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_tittle, compound=LEFT, bd=10, relief=GROOVE,  font=("times new roman", 20, "bold")).place(x=0, y=0, relwidth=1, height=70)

        # btn logout
        btn_logout = Button(title, text="Logout", font=("times new roman", 10, "bold"), bg="yellow").place(x=1150, y=15, width=140, height=35)
        #command=self.logout,

root = Tk()
obj = IMS(root)
root.mainloop()
