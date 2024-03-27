from tkinter import*
from PIL import Image,ImageTk # pip install pillow
from tkinter import ttk,messagebox
import pandas as pd
import sqlite3
import os
import tempfile
#import cv2
# from pyzbar.pyzbar import decode
# from barcode import Gs1_128
# from barcode.writer import ImageWriter
# from returnProduct1 import*
# import time


class billingClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.cart_list=[]
        self.sales_list=[]
        self.chk_print=0
        
        
        #=====title=====
        self.image = Image.open('images/logo1.png')
        resized_img = self.image.resize((70, 70), Image.BICUBIC)
        self.icon_title= ImageTk.PhotoImage(self.image)
        
        title=Label(self.root,text="Inventry Management System",image=self.icon_title,compound=LEFT,font=("times new roman",20,"bold"),bg="#010c48",fg="white",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)
        #========btn_logout
        btn_logout=Button(self.root,text="logout",font=("times new roman",10,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=15,width=140,height=35) #command=self.log_out,
        #=========Clock========
        self.lbl_clock=Label(self.root,text="Welcome to Inventry Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("times new roman", 10), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
#==================================================================================================================================
        #============= All Product frame
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview",
                        background='silver',
                        forground='black',
                        rowheight=45,
                        font=("goudy old style",20,'bold'),
                        fieldbackground='silver')
        style.map('Treeview',
                  background=[('selected','green')])

        #======Product Variables & Search=======
        self.var_search=StringVar()
        
        product_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        product_frame.place(x=6,y=110,width=400,height=550)
        title=Label(product_frame,text="All Products",font=("goudy old style",13),bg="lightgrey").pack(side=TOP,fill=X)
        
        Search_product_frame=Frame(product_frame,bd=2,relief=RIDGE,bg="white")
        Search_product_frame.place(x=2,y=42,width=395,height=90)
        
        product_frame2=Frame(Search_product_frame,bd=0,relief=RIDGE,bg="white")
        product_frame2.place(x=1,y=5,width=390,height=90)
        
        lbl_search=Label(product_frame2,text="Search Product | By Name",font=("goudy old style",13,"bold"),bg="white", fg="green").place(x=2,y=5)
        btn_Show_All=Button(product_frame2,text="Show All",font=("goudy old style",10,"bold"),bg="lightgray",cursor="hand2").place(x=285,y=5,width=100,height=25) #command=self.show,
        #btn_Get_Barcode=Button(product_frame2,text="Get BarCode",command=self.My_invoice,font=("goudy old style",10,"bold"),bg="lightgray",cursor="hand2").place(x=175,y=5,width=110,height=30)
        
        lbl_Product_Name=Label(product_frame2,text="Product Name.",font=("goudy old style",13,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(product_frame2,textvariable=self.var_search,font=("goudy old style",13),bg="lightyellow").place(x=145,y=46,width=130,height=22)
        btn_search=Button(product_frame2,text="Search",font=("goudy old style",13,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=46,width=100,height=22)  #command=self.search,
        
        #=================Product Details frame--====================
        
        product_frame3 = Frame(product_frame,bd=2,relief=RIDGE,bg="white")
        product_frame3.place(x=2,y=140,width=398,height=374)
        
        scrolly=Scrollbar(product_frame3,orient=VERTICAL)
        scrollx=Scrollbar(product_frame3,orient=HORIZONTAL)
        
        self.product_table=ttk.Treeview(product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="Status")
        
        self.product_table.column("pid",width=10)
        self.product_table.column("name",width=40)
        self.product_table.column("price",width=40)
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=40)
        self.product_table["show"]="headings"
        self.product_table.pack(fill=BOTH,expand=1)
        #self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        #lbl_note=Label(product_frame3,text="Note:'Enter 0 QTY to remove Product Cart'",font=("goudy old style",10),bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #=================Customer Details frame
        
        self.var_cust_name=StringVar()
        self.var_contact=StringVar()
        
        
        
        customer_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customer_frame.place(x=410,y=110,width=530,height=70)
        
        customer_tittle=Label(customer_frame,text="Customer Details",font=("goudy old style",13),bg="lightgrey").pack(side=TOP,fill=X)
        
        
        lbl_name = Label(customer_frame,text="Name", font=("times new roman",13), bg="white").place(x=5,y=35)
        txt_name = Entry(customer_frame,textvariable=self.var_cust_name, font=("goudy old style",15), bg="lightyellow").place(x=80,y=35,width=150,height=25)
        
        lbl_contact = Label(customer_frame,text="Contact", font=("times new roman",13), bg="white").place(x=270,y=35)
        lbl_contact = Entry(customer_frame,textvariable=self.var_contact, font=("times new roman",13), bg="lightyellow").place(x=360,y=35,width=150, height=25)
        
        
        #=================Calculater frame
        
        cal_cart = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_cart.place(x=410,y=190,width=530,height=360)
        
        
        self.var_cal_input = StringVar()
        
        cal_frame = Frame(cal_cart,bd=6,relief=RIDGE,bg="white")
        cal_frame.place(x=5,y=10,width=270,height=340)
        
        
        self.txt_cal_input = Entry(cal_frame,textvariable=self.var_cal_input,font=("arial", 13, "bold"), width=20, bd=6, relief=RIDGE, state="readonly", justify=RIGHT, bg="lightyellow")
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        
        btn_8 = Button(cal_frame,text="8",font=("arial",13, "bold"),command=lambda:self.get_input(8), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=1,column=1)
        btn_7 = Button(cal_frame,text="7",font=("arial",13, "bold"),command=lambda:self.get_input(7), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=1,column=0)
        btn_9 = Button(cal_frame,text="9",font=("arial",13, "bold"),command=lambda:self.get_input(9), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=1,column=2)
        btn_add = Button(cal_frame,text="+",font=("arial",13, "bold"),command=lambda:self.get_input('+'), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=1,column=3)
        
        btn_4 = Button(cal_frame,text="4",font=("arial",13, "bold"),command=lambda:self.get_input(4), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=2,column=0)
        btn_5 = Button(cal_frame,text="5",font=("arial",13, "bold"),command=lambda:self.get_input(5), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=2,column=1)
        btn_6 = Button(cal_frame,text="6",font=("arial",13, "bold"),command=lambda:self.get_input(6), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=2,column=2)
        btn_sub = Button(cal_frame,text="-",font=("arial",13, "bold"),command=lambda:self.get_input('-'), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=2,column=3)
        
        btn_1 = Button(cal_frame,text="1",font=("arial",13, "bold"),command=lambda:self.get_input(1), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=3,column=0)
        btn_2 = Button(cal_frame,text="2",font=("arial",13, "bold"),command=lambda:self.get_input(2), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=3,column=1)
        btn_3 = Button(cal_frame,text="3",font=("arial",13, "bold"),command=lambda:self.get_input(3), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=3,column=2)
        btn_mul = Button(cal_frame,text="*",font=("arial",13, "bold"),command=lambda:self.get_input('*'), bd=4, width=4, padx=2, pady=19, cursor="hand2").grid(row=3,column=3)
        
        btn_0 = Button(cal_frame,text="0",font=("arial",13, "bold"),command=lambda:self.get_input(0), bd=4, width=4, padx=2, pady=20, cursor="hand2").grid(row=4,column=0)
        btn_clear = Button(cal_frame,text="C",font=("arial",13, "bold"), command=self.clear_cal, bd=4, width=4, padx=2, pady=20, cursor="hand2").grid(row=4,column=1)
        btn_equal = Button(cal_frame,text="=",font=("arial",13, "bold"), command=self.perform_cal, bd=4, width=4, padx=2, pady=20, cursor="hand2").grid(row=4,column=2)
        btn_div = Button(cal_frame,text="/",font=("arial",13, "bold"),command=lambda:self.get_input('/'), bd=4, width=4, padx=2, pady=20, cursor="hand2").grid(row=4,column=3)
        
        
        
        
        
        
        #=================Cart Details frame
        
        cart_frame = Frame(cal_cart,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=250,height=342)
        cartTitle=Label(cart_frame,text="Cart\t Total Products: [0]",font=("goudy old style",12),bg="lightgray").pack(side=TOP,fill=X)
        
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        
        self.cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)
        
        self.cart_table.heading("pid",text="P ID")
        self.cart_table.heading("name",text="Name")
        self.cart_table.heading("price",text="Price")
        self.cart_table.heading("qty",text="QTY")
        self.cart_table.heading("status",text="Status")

        self.cart_table.column("pid",width=10)
        self.cart_table.column("name",width=40)
        self.cart_table.column("price",width=40)
        self.cart_table.column("qty",width=40)
        self.cart_table.column("status",width=40)
        self.cart_table["show"]="headings"
        self.cart_table.pack(fill=BOTH,expand=1)
        #self.cart_table.bind("<ButtonRelease-1>",self.get_data)
        
        
        #=================Add Cart Details frame
        self.var_pid=StringVar()
        self.var_prodname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_stock=StringVar()
        
        add_cart_frame = Frame(self.root, bd=2,relief=RIDGE,bg="white")
        add_cart_frame.place(x=410,y=550,width=530,height=110)
        
        lbl_prod_name = Label(add_cart_frame,text="Product Name",font=("times new roman",13),bg="white").place(x=5,y=5)
        text_prod_name = Entry(add_cart_frame,textvariable=self.var_prodname,font=("times new roman",13),bg="lightyellow", state="readonly").place(x=5,y=35,width=160,height=22)
        
        lbl_prod_price = Label(add_cart_frame,text="Price (Per Qty)",font=("times new roman",13),bg="white").place(x=230,y=5)
        text_prod_price = Entry(add_cart_frame,textvariable=self.var_price,font=("times new roman",13),bg="lightyellow", state="readonly").place(x=230,y=35,width=130,height=22)
        
        lbl_prod_qty = Label(add_cart_frame,text="Quantity",font=("times new roman",13),bg="white").place(x=390,y=5)
        text_prod_qty = Entry(add_cart_frame,textvariable=self.var_qty,font=("times new roman",13),bg="lightyellow").place(x=390,y=35,width=130,height=22)
        
        self.lbl_inStock = Label(add_cart_frame,text="In Stock [9999]",font=("times new roman",13),bg="white").place(x=5,y=70)
        
        btn_clear_cart = Button(add_cart_frame,text="Clear",font=("times new roman",13),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=22)
        btn_add_cart = Button(add_cart_frame,text="Add | Update",font=("times new roman",13),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=22)
        
        
        #=================Billing Details frame===============
        
        billframe = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billframe.place(x=943,y=110,width=410,height=430)
        
        Bil_tittle = Label(billframe,text="Customer Billing Area",font=("goudy old style",13),bg="lightgrey").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #=================Billing Button frame===============
        
        bill_menu_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=943,y=540,width=410,height=120)
        
        self.lbl_amnt = Label(bill_menu_frame,text="Bill Amount\n[0]",font=("goody old style",13),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=5,y=5,width=127,height=50)
        
        self.lbl_disc = Label(bill_menu_frame,text="Discount\n[5%]",font=("goody old style",13),bg="#8bc34a",fg="white")
        self.lbl_disc.place(x=142,y=5,width=127,height=50)
        
        self.lbl_net_pay = Label(bill_menu_frame,text="Net Pay\n[0]",font=("goody old style",13),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=280,y=5,width=127,height=50)
        
        #=================Button================
        btn_print = Button(bill_menu_frame,text="Print",font=("goody old style",13),bg="#2196f3",fg="white",cursor="hand2").place(x=5,y=60,width=127,height=50)
        btn_clear = Button(bill_menu_frame,text="Clear",font=("goody old style",13),bg="#f44336",fg="white",cursor="hand2").place(x=142,y=60,width=127,height=50)
        btn_generate = Button(bill_menu_frame,text="Generate Bill",font=("goody old style",13),bg="#4caf50",fg="white",cursor="hand2").place(x=280,y=60,width=127,height=50)
        
        
        #=================Footer================
        footer = Label(self.root,text="Developed By: @KgosiKevin",font=("times new roman",10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()
        
        #=================Functionality=======================
        
    def get_input(self,num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)
    
    
    def clear_cal(self):
        self.var_cal_input.set("")
        
        
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
        
    def show(self):
        con=sqlite3.connect(database="inventory.db")
        cur=con.cursor()
        try:
            cur.execute("select * from products")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
                
    
    
        
if __name__=="__main__":        
    root=Tk()
    obj=billingClass(root)
    root.mainloop()
