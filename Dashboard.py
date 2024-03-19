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
        title = Label(self.root, text="Inventory Management System", image=self.icon_tittle, compound=LEFT, font=("times new roman", 20, "bold"),bg="#010c48", anchor="w", padx=20 , fg="white").place(x=0, y=0, relwidth=1, height=70)

        # btn logout
        btn_logout = Button(title, text="Logout", font=("times new roman", 10, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=15, width=140, height=35)
        #command=self.logout,
        
        # clock
        self.lbl_clock = Label(self.root, text="Welcom To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 10), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=25)
        
        # left menu
        self.menu_logo = Image.open("images/menu2.png")
        self.menu_logo.thumbnail((120, 150))  
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)     
        
        leftmenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftmenu.place(x=0, y=95, width=200, height=565)
        
        lbl_menu_logo = Label(leftmenu, image=self.menu_logo)
        lbl_menu_logo.pack(side=TOP, fill=X)
        
        self.icon_side = PhotoImage(file="images/side.png")
        lbl_menu = Label(leftmenu, text="Menu", font=("times new roman", 15), bg="#009688").pack(side=TOP, fill=X)
        
        btn_employee = Button(leftmenu, text="Employee", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(leftmenu, text="Supplier", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(leftmenu, text="Category", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(leftmenu, text="Sales", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(leftmenu, text="Exit", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # content
        self.lbl_employee = Label(self.root, text="Total Employees\n[0]", bd=4, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=250, y=100, width=250, height=150)
        
        self.lbl_supplier = Label(self.root, text="Total Suppliers\n[0]", bg="#33bbf9", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_supplier.place(x=520, y=100, width=250, height=150)
        
        # Footer
        lbl_footer = Label(self.root, text="IMS - Inventory Management System | Developed by KevCare \nContact: +27735266552", font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        













root = Tk()
obj = IMS(root)
root.mainloop()
