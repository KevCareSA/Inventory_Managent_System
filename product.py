from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force() 
        
        #===========================

        #=============Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_pid = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_category_supplier()
        
        
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        
        #====================================================
        #==============Product Frame
        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=10, width=450, height=480)
        
        #==============Title==============
        title = Label(product_frame, text="Manage Product Details", font=("goudy old style", 18), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)
      
        lbl_category = Label(product_frame, text="Category", font=("goudy old style", 15), bg="white").place(x=30, y=60)
        lbl_supplier = Label(product_frame, text="Supplier", font=("goudy old style", 15), bg="white").place(x=30, y=110)
        lbl_product_name = Label(product_frame, text="Name", font=("goudy old style", 15), bg="white").place(x=30, y=160)
        lbl_price = Label(product_frame, text="Price", font=("goudy old style", 15), bg="white").place(x=30, y=210)
        lbl_qty = Label(product_frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30, y=260)
        lbl_status = Label(product_frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30, y=310)
        
        
        #=================Column Fields 2============
        #txt_category = Label(product_frame, text="Select Category", font=("goudy old style", 15), bg="white")
        cmb_category = ttk.Combobox(product_frame, textvariable=self.var_category, values=self.cat_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_category.place(x=150, y=60, width=180)
        cmb_category.current(0)
        
        cmb_supplier = ttk.Combobox(product_frame, textvariable=self.var_supplier, values=self.sup_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_supplier.place(x=150, y=110, width=180)
        cmb_supplier.current(0)
        
        txt_product_name = Entry(product_frame, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=160, width=180)
        txt_price = Entry(product_frame, textvariable=self.var_price, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=210, width=180)
        txt_qty = Entry(product_frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=260, width=180)
        
        cmb_status = ttk.Combobox(product_frame, textvariable=self.var_status, values=("Active", "Inactive"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=180)
        cmb_status.current(0)
        
        #=================Buttons============
        
        btn_add = Button(product_frame, text="Add", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=400, width=100, height=30)
        btn_update = Button(product_frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=100, height=30)
        btn_delete = Button(product_frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=230, y=400, width=100, height=30)
        btn_clear = Button(product_frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=400, width=100, height=30)
        
         #======search
        search_frame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=480, y=10, width=600, height=80)
        
        #======option
        cmb_search = ttk.Combobox(search_frame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        
        txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10, width=180)
        btn_search = Button(search_frame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=400, y=9, width=150, height=30)
        
        #============Product Detals======================
        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame.place(x=480, y=100, width=600, height=390)
        
        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)
        
        
        self.productTable = ttk.Treeview(product_frame, columns=("pid", "supplier", "category", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        
        
        scrolly.config(command=self.productTable.yview)
        scrollx.config(command=self.productTable.xview)
        
        self.productTable.heading("pid", text="P ID")
        self.productTable.heading("category", text="Category")
        self.productTable.heading("supplier", text="Supplier")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("qty", text="Quantity")
        self.productTable.heading("status", text="Status")
        
        self.productTable["show"] = "headings"
        
        self.productTable.column("pid", width=90)
        self.productTable.column("category", width=100)
        self.productTable.column("supplier", width=100)
        self.productTable.column("name", width=100)
        self.productTable.column("price", width=100)
        self.productTable.column("qty", width=100)
        self.productTable.column("status", width=100)
        
        self.productTable.pack(fill=BOTH, expand=1)
        
        self.productTable.bind("<ButtonRelease-1>", self.fetch_data)
        self.show()
        
        #================================================================

    def fetch_category_supplier(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
                    
            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])         
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
            
            
    
    def add(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier.get()=="Select" or self.var_name.get()=="" or self.var_price.get()=="" or self.var_qty.get()=="" or self.var_status.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM products WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Product already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO products (Category, Supplier, name, price, qty, status) values(?,?,?,?,?,?)", (
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        
    def show(self):
            con=sqlite3.connect(database=r'inventory.db')
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM products")
                rows = cur.fetchall()
                self.productTable.delete(*self.productTable.get_children())
                for row in rows:
                    self.productTable.insert("", END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                
                
    def fetch_data(self, ev):
        f=self.productTable.focus()
        content = self.productTable.item(f)
        row = content["values"]
        self.var_pid.set(row[0])
        self.var_category.set(row[2])
        self.var_supplier.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        
        
        
    def update(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Product ID field is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM products WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute("UPDATE products SET Category=?, Supplier=?, name=?, price=?, qty=?, status=? WHERE pid=?", (
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Product ID field is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM products WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM products WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Product deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
            
    def clear(self):
        self.var_pid.set("")
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
    
        self.var_status.set("Active")
      
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchby.get()=="Category":
                cur.execute("SELECT * FROM products WHERE Category LIKE ?", ('%'+self.var_searchtxt.get()+'%',))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
            elif self.var_searchby.get()=="Supplier":
                cur.execute("SELECT * FROM products WHERE Supplier LIKE ?", ('%'+self.var_searchtxt.get()+'%',))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
            elif self.var_searchby.get()=="Name":
                cur.execute("SELECT * FROM products WHERE name LIKE ?", ('%'+self.var_searchtxt.get()+'%',))
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
