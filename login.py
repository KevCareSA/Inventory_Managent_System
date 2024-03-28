from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
import time

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#fafafa")
        
        
        #==========Images==========
        self.pic_image = ImageTk.PhotoImage(file="images/login3.jpg")
        self.lbl_pic_image = Label(self.root, image=self.pic_image, bd=0).place(x=200, y=110)
        
        #==========Login Frame==========
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=600, y=50, width=350, height=500)
        
        tittle = Label(login_frame, text="Login System", font=("Elephant", 20, "bold"), bg="white").place(x=0, y=20, relwidth=1)
        
        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)
        
        txt_username = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15), bg="#ECF0F1").place(x=50, y=130, width=250)
        
        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=200)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="#ECF0F1").place(x=50, y=230, width=250)
        
        
        btn_login = Button(login_frame, text="Login", command=self.login, font=("times new roman", 15), bg="#009688", fg="white").place(x=50, y=300, width=250) #command=self.login,
        
        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15)).place(x=170, y=360)
        
        btn_forget = Button(login_frame, text="Forget Password?", command=self.forget_window, font=("times new roman", 15), bg="white", fg="#009688", bd=0).place(x=50, y=400, width=250)
        
        #==========Register Frame==========
        
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=600, y=550, width=350, height=100)
        
        lbl_reg = Label(register_frame, text="New User? Register Here", font=("times new roman", 15), bg="white").place(x=50, y=20)
        
        
        
    def login(self):
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT utype FROM users WHERE eid=? AND password=?", (self.employee_id.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    if row=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
            
            
    def forget_window(self):
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("SELECT email FROM users WHERE eid=?", (self.employee_id.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()
                    
                    self.forget_window = Toplevel(self.root)
                    self.forget_window.title("Reset Password")
                    self.forget_window.geometry("350x400+480+150")
                    self.forget_window.focus_force()
                    
                    tittle = Label(self.forget_window, text="Reset Password", font=("goudy old style", 15, "bold"), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                    
                    lbl_reset = Label(self.forget_window, tex="Enter OTP sent on Registered Email", font=("times new roman", 15)).place(x=20, y=60)
                    text_reset = Entry(self.forget_window, textvariable=self.var_otp, font=("times new roman", 15), bg="lightyellow").place(x=20, y=100, width=300)
        
        
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)            
                    
        
        #==========Images==========
        self.pic_image = ImageTk.PhotoImage(file="images/login3.jpg")
        self.lbl_pic_image = Label(self.root, image=self.pic_image, bd=0).place(x=200, y=110)
        
        #==========Login Frame==========
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=600, y=50, width=350, height=500)
        
        tittle = Label(login_frame, text="Forget Password", font=("Elephant", 20, "bold"), bg="white").place(x=0, y=20, relwidth=1)
        
        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)
        
        txt_username = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15), bg="#ECF0F1").place(x=50, y=130, width=250)
        
        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=200)
        txt_pass = Entry(login_frame, textvariable=self.password, font=("times new roman", 15), bg="#ECF0F1").place(x=50, y=230, width=250)
        
        
        btn_login = Button(login_frame, text="Login", command=self.login, font=("times new roman", 15), bg="#009688", fg="white").place(x=50, y=300, width=250)
        
           

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
