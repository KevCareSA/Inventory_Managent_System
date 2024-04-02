import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.configure(bg="white")
        self.root.focus_force()
        
        #==== Variables ====
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_searchtype = StringVar()   
        
        
        self.var_emp_id = StringVar()
        self.var_designation = StringVar()
        self.var_department = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_gender = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        
        
        
        #======search
        search_frame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=250, y=20, width=600, height=70)
        
        #======option
        cmb_search = ttk.Combobox(search_frame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state="readonly", justify=CENTER, font=("time new roman", 15), width=15)
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        
        txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10, width=180)
        btn_search = Button(search_frame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=400, y=9, width=150, height=30)
        
        #=======tittle
        tittle = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)
        
        
        #========Content===========================
 
        #=======Row1==========
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 15), bg="white",).place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white",).place(x=350, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white",).place(x=740, y=150)
        
        
        txt_empid = Entry(self.root,textvariable=self.var_emp_id, font=("goudy old style", 15), bg="lightyellow",).place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER, font=("time new roman", 15), width=15)
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow",).place(x=850, y=150, width=180)
        

        #=======Row2==========
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white",).place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15), bg="white",).place(x=350, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("goudy old style", 15), bg="white",).place(x=740, y=190)
        
        
        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow",).place(x=150, y=190, width=180)
        txt_dob = Entry(self.root,textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow",).place(x=500, y=190, width=180)
        txt_doj = Entry(self.root,textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow",).place(x=850, y=190, width=180)
        
        #=======Row3==========
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white",).place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=("goudy old style", 15), bg="white",).place(x=350, y=230)
        lbl_utype = Label(self.root, text="User Type", font=("goudy old style", 15), bg="white",).place(x=740, y=230)
        
        
        txt_email = Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow",).place(x=150, y=230, width=180)
        txt_pass = Entry(self.root,textvariable=self.var_pass, font=("goudy old style", 15), bg="lightyellow",).place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state="readonly", justify=CENTER, font=("time new roman", 15), width=15)
        cmb_utype.place(x=850, y=230, width=180)
        #cmb_utype.current(0)
        
        
        #=======Row4==========
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white",).place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white",).place(x=500, y=270)
        
        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root,textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow",).place(x=600, y=270, width=180)
        
         
        #=======buttons==========
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)
        

        #=======Employee Details==========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)
        
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        
        self.employeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)
        
        self.employeeTable.heading("eid", text="Emp ID")
        self.employeeTable.heading("name", text="Name")
        self.employeeTable.heading("email", text="Email")
        self.employeeTable.heading("gender", text="Gender")
        self.employeeTable.heading("contact", text="Contact")
        self.employeeTable.heading("dob", text="D.O.B")
        self.employeeTable.heading("doj", text="D.O.J")
        self.employeeTable.heading("pass", text="Password")
        self.employeeTable.heading("utype", text="User Type")
        self.employeeTable.heading("address", text="Address")
        self.employeeTable.heading("salary", text="Salary")
        
        self.employeeTable["show"] = "headings"
        
        self.employeeTable.column("eid", width=90)
        self.employeeTable.column("name", width=100)
        self.employeeTable.column("email", width=100)
        self.employeeTable.column("gender", width=100)
        self.employeeTable.column("contact", width=100)
        self.employeeTable.column("dob", width=100)
        self.employeeTable.column("doj", width=100)
        self.employeeTable.column("pass", width=100)
        self.employeeTable.column("utype", width=100)
        self.employeeTable.column("address", width=100)
        self.employeeTable.column("salary", width=100)
        
        
        
        self.employeeTable.pack(fill=BOTH, expand=1)
        self.employeeTable.bind("<ButtonRelease-1>", self.fetch_data)
        
        self.show()
        
#================================================================

    def add(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
                messagebox.showerror("Error", "Employee ID, Name and Email fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Employee ID already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, address, salary) values(?,?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.txt_address.get("1.0", END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        
    def show(self):
            con=sqlite3.connect(database=r'inventory.db')
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM employee")
                rows = cur.fetchall()
                self.employeeTable.delete(*self.employeeTable.get_children())
                for row in rows:
                    self.employeeTable.insert("", END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
                
                
    def fetch_data(self, ev):
        f=self.employeeTable.focus()
        content = self.employeeTable.item(f)
        row = content["values"]
        
        self.txt_address.delete("1.0", END)
        self.var_emp_id.set(self.employeeTable.item(self.employeeTable.selection())["values"][0])
        self.var_name.set(self.employeeTable.item(self.employeeTable.selection())["values"][1])
        self.var_email.set(self.employeeTable.item(self.employeeTable.selection())["values"][2])
        self.var_gender.set(self.employeeTable.item(self.employeeTable.selection())["values"][3])
        self.var_contact.set(self.employeeTable.item(self.employeeTable.selection())["values"][4])
        self.var_dob.set(self.employeeTable.item(self.employeeTable.selection())["values"][5])
        self.var_doj.set(self.employeeTable.item(self.employeeTable.selection())["values"][6])
        self.var_pass.set(self.employeeTable.item(self.employeeTable.selection())["values"][7])
        self.txt_address.insert(END, self.employeeTable.item(self.employeeTable.selection())["values"][8])
        self.var_salary.set(self.employeeTable.item(self.employeeTable.selection())["values"][9])
        
        
    def update(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_name.get()=="" or self.var_email.get()=="":
                messagebox.showerror("Error", "Employee ID, Name and Email fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=?,gender=?,contact=?,dob=?,doj=?,pass=?,address=?,salary=? WHERE eid=?", (
                        self.var_name.get(), 
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.txt_address.get("1.0", END),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def delete(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID field is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Employee deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
            
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.txt_address.delete("1.0", END) 
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.var_searchtype.set("")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database=r'inventory.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search field is required", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE '%{self.var_searchtxt.get()}%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.employeeTable.delete(*self.employeeTable.get_children())
                    for row in rows:
                        self.employeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()

