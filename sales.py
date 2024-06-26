import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1100x500+220+130")
        self.root.configure(bg="white")
        self.root.focus_force()

        #========Variables=================
        self.var_invoice = StringVar()
        self.product_var = StringVar()
        self.quantity_var = IntVar()
        self.price_var = DoubleVar()
        self.total_var = DoubleVar()
        self.customer_name_var = StringVar()
        self.customer_contact_var = StringVar()
        
        self.bill_list = []

        #========Title=====================
        title = Label(self.root, text="View Customer Bills", font=("goudy old style", 20, "bold"), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15),bg="lightyellow").place(x=180, y=100, width=180, height=28)
        
        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=370, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=500, y=100, width=120, height=28)
        
        #========Sales Frame===============
        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)
        
        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_frame, font=("goudy old style", 13), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        
        
        #========Bill Frame================
        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=270, y=140, width=410, height=330)
        
        lbl_tittle2 = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 14), bg="orange", fg="white").pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.bill_area = Text(bill_frame, font=("goudy old style", 8), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)
        
        
        #========Image=====================
        #======img1=========
        self.bill_img = Image.open("images/bill4.png")
        resized_img = self.bill_img.resize((110, 110), Image.BICUBIC)

        self.bill_img = ImageTk.PhotoImage(self.bill_img)
        
        lbl_image = Label(self.root, image=self.bill_img)
        lbl_image.place(x=720, y=120)
        
        self.show()
    #============================================================
        #=======Functions========== 
        
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split(".")[-1] == "txt":
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split(".")[0])
                

    def get_data(self, ev):
        index = self.sales_list.curselection()
        file_name = self.sales_list.get(index)
        print(file_name)
        self.bill_area.delete('1.0', END)
        fp = open(f"bill/{file_name}", "r")
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()
        
        
    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice Number Required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f"bill/{self.var_invoice.get()}.txt", "r")
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice Number", parent=self.root)
        
        
    def clear(self):
        self.var_invoice.set("")
        self.bill_area.delete('1.0', END)
        self.show()

if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()

