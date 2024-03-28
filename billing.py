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
import time
from datetime import datetime


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
        btn_logout=Button(self.root,text="logout", command=self.logout, font=("times new roman",10,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=15,width=140,height=35) #command=self.log_out,
        #=========Clock========
        self.lbl_clock=Label(self.root,text="Welcome to the Inventry Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("times new roman", 10), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
#==================================================================================================================================
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
        btn_Show_All=Button(product_frame2,text="Show All",command=self.show,font=("goudy old style",10,"bold"),bg="lightgray",cursor="hand2").place(x=285,y=5,width=100,height=25) #
        #btn_Get_Barcode=Button(product_frame2,text="Get BarCode",command=self.My_invoice,font=("goudy old style",10,"bold"),bg="lightgray",cursor="hand2").place(x=175,y=5,width=110,height=30)
        
        lbl_Product_Name=Label(product_frame2,text="Product Name.",font=("goudy old style",13,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(product_frame2,textvariable=self.var_search,font=("goudy old style",13),bg="lightyellow").place(x=145,y=46,width=130,height=22)
        btn_search=Button(product_frame2,text="Search",command=self.search, font=("goudy old style",13,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=46,width=100,height=22)  #command=self.search,
        
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
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
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
        self.cartTitle=Label(cart_frame,text="Cart\t Total Products: [0]",font=("goudy old style",12),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)
        
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        
        self.cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)
        
        self.cart_table.heading("pid",text="P ID")
        self.cart_table.heading("name",text="Name")
        self.cart_table.heading("price",text="Price")
        self.cart_table.heading("qty",text="QTY")
        self.cart_table.column("pid",width=10)
        self.cart_table.column("name",width=40)
        self.cart_table.column("price",width=40)
        self.cart_table.column("qty",width=40)
        self.cart_table["show"]="headings"
        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart)
        
        
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
        
        self.lbl_inStock = Label(add_cart_frame,text="In Stock ",font=("times new roman",13),bg="white")
        self.lbl_inStock.place(x=5,y=70)
       
        
        btn_clear_cart = Button(add_cart_frame,text="Clear",command=self.clear_cart, font=("times new roman",13),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=22)
        btn_add_cart = Button(add_cart_frame,text="Add | Update", command=self.add_update_cart, font=("times new roman",13),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=22)
        
        
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
        self.lbl_amnt.place(x=5,y=5,width=130,height=50)
        
        self.lbl_disc = Label(bill_menu_frame,text="Discount\n[5%]",font=("goody old style",13),bg="#8bc34a",fg="white")
        self.lbl_disc.place(x=142,y=5,width=130,height=50)
        
        self.lbl_net_pay = Label(bill_menu_frame,text="Net Pay\n[0]",font=("goody old style",13),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=280,y=5,width=130,height=50)
        
        #=================Button================
        btn_print = Button(bill_menu_frame,text="Print",font=("goody old style",13),bg="#2196f3",fg="white",cursor="hand2")
        btn_print.place(x=5,y=60,width=130,height=50)
        
        btn_clear = Button(bill_menu_frame,text="Clear", command=self.clear_all, font=("goody old style",13),bg="#f44336",fg="white",cursor="hand2")
        btn_clear.place(x=142,y=60,width=130,height=50)
        
        btn_generate = Button(bill_menu_frame,text="Generate Bill", command=self.generate_bill, font=("goody old style",13),bg="#4caf50",fg="white",cursor="hand2")
        btn_generate.place(x=280,y=60,width=130,height=50)
        
        
        #=================Footer================
        footer = Label(self.root,text="Developed By: @KgosiKevin",font=("times new roman",10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()
        self.bill_top()
        self.update_date_time()
        
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
            cur.execute("select pid,name,price,qty,status from products where status='Active'")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
            
            
    def search(self):
        con=sqlite3.connect(database="inventory.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search field should not be empty",parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status from products where name LIKE '%"+self.var_search.get()+"%'" and "status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Product Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
            
    def get_data(self,ev):
        r=self.product_table.focus()
        content=self.product_table.item(r)
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_prodname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set("1")
      
    def get_data_cart(self, ev):
        r = self.cart_table.focus()
        content = self.cart_table.item(r)
        row = content["values"]
        if row:
            self.var_pid.set(row[0])
            self.var_prodname.set(row[1])
            self.var_price.set(row[2])
            self.var_qty.set(row[3])
            if len(row) >= 5:
                self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
                self.var_stock.set(row[4])
            else:
                self.lbl_inStock.config(text="In Stock [N/A]")
                self.var_stock.set("N/A")
    
    # def get_data_cart(self,ev):
    #     r=self.cart_table.focus()
    #     content=self.cart_table.item(r)
    #     row=content["values"]
    #     self.var_pid.set(row[0])
    #     self.var_prodname.set(row[1])
    #     self.var_price.set(row[2])
    #     self.var_qty.set(row[3])
    #     self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
    #     self.var_stock.set(row[4])
        
                
    def add_update_cart(self):
        if self.var_pid.get()=="": 
            messagebox.showerror("Error","Please select product from list",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Please enter product quantity",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
        #     price_cal=float(self.var_price.get())*int(self.var_qty.get())
        #     price_cal=float(price_cal)
            price_cal=self.var_price.get()
            
            cart_data=[self.var_pid.get(),self.var_prodname.get(),self.var_price.get(),self.var_qty.get(),price_cal,self.var_stock.get()]
            
            #=============Update Cart=============
            present="no"
            index=-1
            for row in self.cart_list:
                index+=1
                if self.var_pid.get()==row[0]:
                    present="yes"
                    break
                
            if present=="yes":
                op = messagebox.askyesno("Confirm","Product already present in cart, Do you want to update it?",parent=self.root)
                if op == True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][2]=price_cal
                        self.cart_list[index][3]=self.var_qty.get()
             
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()             
                
    
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for i in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(i[2])*int(i[3]))
            
        self.discount = (self.bill_amnt*5)/100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f"R{str(self.bill_amnt)}")
        self.lbl_net_pay.config(text=f"Net Pay \n R{str(self.net_pay)}")
        self.cartTitle.config(text=f"Cart. Total Products: {str(len(self.cart_list))}")
        
    
    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    
    def generate_bill(self):
        if self.var_cust_name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Customer details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","No product in cart",parent=self.root)
        else: 
            #=============Bill Top=============
            self.bill_top()
            
            #=============Bill Middle=============
            self.bill_middle()
            
            #=============Bill Bottom=============
            self.bill_bottom()
            
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Success","Bill has been generated",parent=self.root)
           
            
        
        
    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
        \t\t KevCare Tech Warehouse
        \t Phone No. : 0123456789, Johannesburg
        {str("="*39)}
         Customer Name: {self.var_cust_name.get()}
          Phone No. : {self.var_contact.get()}
          Bill No.  : {str(self.invoice)}\t\t Date:{time.strftime("%d/%m/%Y")}
        {str("="*39)}
         Product Name\t\t\tQty\t\tPrice
        {str("="*39)}
        
            '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
        
    
    def bill_bottom(self):
        bill_bottom_temp = f'''
                {str("="*29)}
                Total Amount\t\t\t {self.lbl_amnt.cget("text")}
                Discount: 5% \t\t\t R{self.discount}
                Net Pay \t\t\t\t R{self.net_pay}
                {str("="*29)}
                \t Thanks for shopping with us
                '''
        self.txt_bill_area.insert(END, bill_bottom_temp)


    
    def bill_middle(self):   
        for i in self.cart_list:
            name = i[1]
            qty = i[3]
            price = float(i[2]*int(i[3]))
            price = str(price)
            self.txt_bill_area.insert(END,"\n " + name + "\t\t\t " + qty + "\t R" + price)
            
            
    def clear_cart(self):
        op = messagebox.askyesno("Confirm","Do you really want to clear?",parent=self.root)
        if op == True:
            self.cart_list.clear()
            self.show_cart()
            self.bill_updates()
            self.txt_bill_area.delete('1.0',END)
            self.var_cust_name.set("")
            self.var_contact.set("")
            self.var_cal_input.set("")
            self.var_search.set("")
            self.show()
            self.bill_top()
            
            
    def clear_all(self):
        del self.cart_list[:]
        self.var_cust_name.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text="Cart \t Total Products: [0]")
        self.var_search.set("")
        self.clear_cart()
        self.show()
        self.show_cart()
        
        
     
    

    def update_date_time(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%H:%M:%S')
        formatted_date = current_time.strftime('%Y-%m-%d')  # Format date as desired
        self.lbl_clock.config(text=f"Welcome to the Inventory Management System\t\t Date: {formatted_date} \t\t Time: {formatted_time}")
        self.lbl_clock.after(1000, self.update_date_time)
    
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    
        
            
                    
                
                
                
    
        
        
        
if __name__=="__main__":        
    root=Tk()
    obj=billingClass(root)
    root.mainloop()
