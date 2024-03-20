from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

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
        
        
        
        #  search
        search_frame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12), bd=2, relief=RIDGE, bg="white")
        search_frame.place(x=250, y=20, width=600, height=70)
        
        # option
        cmb_search = ttk.Combobox(search_frame, values=("Select", "Email", "Name", "Contact"), state="readonly", justify=CENTER, font=("time new roman", 15), width=15)
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        
        txt_search = Entry(search_frame, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10, width=180)
        btn_search = Button(search_frame, text="Search", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=400, y=9, width=150, height=30)
        
        # tittle
        tittle = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)
        
        
        # content
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()

