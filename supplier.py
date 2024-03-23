from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.configure(bg="white")
        self.root.focus_force()
        
#========================================================
#==============Variables==============

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        #self.var_supplier_id = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        
        
       
        

#============tittle============

        #======search
        
        #======option
        lbl_search = Label(self.root, text="Invoice No.", bg="white", font=("goudy old style", 15))
        lbl_search.place(x=700, y=80)
        
        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=830, y=80, width=150)
        btn_search = Button(self.root, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=980, y=79, width=100, height=30)
        
        #=======tittle
        tittle = Label(self.root, text="Supplier Details", font=("goudy old style", 15, "bold"), bg="#0f4d7d", fg="white").place(x=50, y=10, width=1030, height=40)
        
        
        #========CONTENT=========
        #=======Row1==========
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white",).place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow",).place(x=170, y=80, width=180)
        

        #=======Row2==========
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white",).place(x=50, y=120)
        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow",).place(x=170, y=120, width=180)
        
        
        #=======Row3==========
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white",).place(x=50, y=160)
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow",).place(x=170, y=160, width=180)
        
        
        
        #=======Row4==========
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white",).place(x=50, y=200)
        self.text_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.text_desc.place(x=170, y=200, width=470, height=90)
        
         
        #=======buttons==========
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=170, y=305, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=290, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=410, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=530, y=305, width=110, height=28)
        

        #=======Employee Details==========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700, y=120, width=380, height=350)
        
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        
        # self.supplierTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc", "date", "address"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable.heading("date", text="Date")
        self.supplierTable.heading("address", text="Address")
        
        
        self.supplierTable["show"] = "headings"
        
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
        
#================================================================

    def add(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error", "Invoice field is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Invoice No. already assigned", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) values(?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
                    
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        
    def show(self):
            con=sqlite3.connect(database=r'inventory.db')
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM supplier")
                rows = cur.fetchall()
                self.supplierTable.delete(*self.supplierTable.get_children())
                for row in rows:
                    self.supplierTable.insert("", END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                
                
    def get_data(self, ev):
        f=self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content["values"]
        
        
        self.var_sup_invoice.set(self.supplierTable.item(self.supplierTable.selection())["values"][0])
        self.var_name.set(self.supplierTable.item(self.supplierTable.selection())["values"][1])
        self.var_contact.set(self.supplierTable.item(self.supplierTable.selection())["values"][2])
        self.text_desc.delete("1.0", END)
        self.text_desc.insert(END, self.supplierTable.item(self.supplierTable.selection())["values"][3])
        
        
    def update(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
                messagebox.showerror("Error", "Invoice No. fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get("1.0", END),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice No. field is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.text_desc.delete("1.0", END)
        self.var_searchtxt.set("")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchone()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                    
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()


