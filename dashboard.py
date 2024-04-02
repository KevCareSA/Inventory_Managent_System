from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import ttk, messagebox
import os
import time
from datetime import datetime   


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="white")

        # title
        self.icon_tittle = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_tittle, compound=LEFT, font=("times new roman", 20, "bold"),bg="#010c48", anchor="w", padx=20, fg="white").place(x=0, y=0, relwidth=1, height=70)

        # btn logout
        btn_logout = Button(title, text="Logout", command=self.logout, font=("times new roman", 10, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=15, width=140, height=35)
        #command=self.logout,
        
        # clock
        self.lbl_clock = Label(self.root, text="Welcom To The Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 10), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=25)
        
        # left menu
        self.menu_logo = Image.open("images/menu2.png")
        self.menu_logo.thumbnail((300, 150))  
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)     
        
        leftmenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftmenu.place(x=0, y=95, width=200, height=565)
        
        lbl_menu_logo = Label(leftmenu, image=self.menu_logo)
        lbl_menu_logo.pack(side=TOP, fill=X)
        
        self.icon_side = PhotoImage(file="images/side.png")
        lbl_menu = Label(leftmenu, text="Menu", font=("times new roman", 15), bg="#009688").pack(side=TOP, fill=X)
        
        btn_employee = Button(leftmenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(leftmenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(leftmenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_products = Button(leftmenu, text="Product", command=self.product, image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(leftmenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(leftmenu, text="Exit", image=self.icon_side, compound=LEFT, padx=10, anchor="w", font=("times new roman", 13, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # content
        
        self.lbl_employee = Label(self.root, text="Total Employees\n[0]", bd=4, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_employee.place(x=250, y=150, width=250, height=150)
        
        self.lbl_supplier = Label(self.root, text="Total Suppliers\n[0]", bd=4, relief=RIDGE, bg="#FF8E00", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_supplier.place(x=600, y=150, width=250, height=150)
        
        self.lbl_category = Label(self.root, text="Total Categorys\n[0]", bd=4, relief=RIDGE, bg="#FFE400", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_category.place(x=950, y=150, width=250, height=150)
        
        self.lbl_product = Label(self.root, text="Total Products\n[0]", bd=4, relief=RIDGE, bg="#06FF00", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_product.place(x=250, y=350, width=250, height=150)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=4, relief=RIDGE, bg="#FF1700", fg="white", font=("goudy old style", 15, "bold"))
        self.lbl_sales.place(x=600, y=350, width=250, height=150)
        
        # Footer
        lbl_footer = Label(self.root, text="IMS - Inventory Management System | Developed by KevCare \nContact: @CodingKevCare on twitter ", font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        self.update_content()
    #======================================
    
    def employee(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_window)
        
    def supplier(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_window)
        
    def category(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_window)
        
    def product(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = productClass(self.new_window)
        
    def sales(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = salesClass(self.new_window)
        
    def update_content(self):
        con = sqlite3.connect(database="inventory.db")
        cur = con.cursor()
        try:
            products = cur.fetchall()
            cur.execute("SELECT * FROM products")
            self.lbl_product.config(text=f"Total Products\n[{str(len(products))}]")
            
            cur.execute("SELECT * FROM supplier")
            suppliers = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[{str(len(suppliers))}]")
            
            cur.execute("SELECT * FROM category")
            categorys = cur.fetchall()
            self.lbl_category.config(text=f"Total Categorys\n[{str(len(categorys))}]")
            
            cur.execute("SELECT * FROM Employee")
            employees = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employees\n[{str(len(employees))}]")
            bill = len(os.listdir("bill/"))
            self.lbl_sales.config(text=f"Total Sales\n[{str(bill)}]")
            
            
            formatted_time = time.strftime("%H:%M:%S")
            formatted_date = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To The Inventory Management System\t\t Date: {formatted_date}\t\t Time: {formatted_time}")
            self.lbl_clock.after(200, self.update_content)
            
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
        


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
