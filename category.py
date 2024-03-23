from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.configure(bg="white")
        self.root.focus_force()
        
#========================================================

        #========Variables=================
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
    
        #========title=====================
    
        lbl_title = Label(self.root, text="Manage Category", font=("goudy old style", 25, "bold"), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X)
        
        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 20), bg="white").place(x=50, y=100)
        text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow").place(x=50, y=170, width=300)
        
        btn_add = Button(self.root, text="add",command=self.add, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=35)
        btn_delete = Button(self.root, text="delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=35)
        #

        #========Category Details=====================
        self.cat_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.cat_frame.place(x=700, y=100, width=380, height=105)
        
        scrolly = Scrollbar(self.cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.cat_frame, orient=HORIZONTAL)
        
        self.category_table = ttk.Treeview(self.cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.category_table.yview)
        scrollx.config(command=self.category_table.xview)
        
        
        self.category_table.heading("cid", text="Category ID")
        self.category_table.heading("name", text="Category Name")
        self.category_table["show"] = "headings"
        
        self.category_table.column("cid", width=90)
        self.category_table.column("name", width=100)
        
        self.category_table.pack(fill=BOTH, expand=1)
        
        self.category_table.bind("<ButtonRelease-1>", self.get_data)
        #self.show()

        #========Image=====================
        #======img1=========
        self.img = Image.open("images/cat2.jpg")
        resized_img = self.img.resize((390, 250), Image.BICUBIC)
        self.img = ImageTk.PhotoImage(resized_img)
        
        self.lbl_img = Label(self.root, image=self.img, bd=2, relief=RAISED)
        self.lbl_img.place(x=80, y=220)
        
        #======img2=========
        self.img2 = Image.open("images/cat1.jpg")
        resized_img2 = self.img2.resize((390, 250), Image.BICUBIC)
        self.img2 = ImageTk.PhotoImage(resized_img2)
        
        self.lbl_img2 = Label(self.root, image=self.img2, bd=2, relief=RAISED)
        self.lbl_img2.place(x=550, y=220)
        
        self.show()
        
        #=======Functions========
    def add(self):
            conn=sqlite3.connect(database="inventory.db")
            cur=conn.cursor()
            try:
                if self.var_name.get()=="":
                    messagebox.showerror("Error", "Category Name is required", parent=self.root)
                else:
                    cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error", "Category Name already exists", parent=self.root)
                    else:
                        cur.execute("INSERT INTO category (name) VALUES(?)", (self.var_name.get(),))
                        conn.commit()
                        messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                        self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                
                
    def show(self):
        conn=sqlite3.connect(database="inventory.db")
        cur=conn.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    
    
    def get_data(self, ev):
        f = self.category_table.focus()
        content = self.category_table.item(f)
        row = content["values"]
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
        
    def delete(self):
        con=sqlite3.connect(database="inventory.db")
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Category ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Category ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete this category?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        
        
                    
        

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
