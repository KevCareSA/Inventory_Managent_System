import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

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

        #========Title=====================
        title = Label(self.root, text="View Customer Bills", font=("goudy old style", 20, "bold"), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15),bg="lightyellow").place(x=180, y=100, width=180, height=28)
        
        btn_search = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=370, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=500, y=100, width=120, height=28)
        
        #========Sales Frame===============
        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)
        
        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        
        
        #========Bill Frame================
        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=270, y=140, width=410, height=330)
        
        lbl_tittle2 = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange", fg="white").pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.bill_area = Text(bill_frame, font=("goudy old style", 14), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)
        
        
        #========Image=====================
        #======img1=========
        self.bill_img = Image.open("images/bill4.png")
        resized_img = self.bill_img.resize((110, 110), Image.BICUBIC)
        #self.bill_img = self.bill_img.resize((500, 500), Image.ANTIALIAS)
        self.bill_img = ImageTk.PhotoImage(self.bill_img)
        
        lbl_image = Label(self.root, image=self.bill_img)
        lbl_image.place(x=720, y=120)
        
        

        # #========Manage Title===============
        # m_title = Label(manage_frame, text="Manage Sales", bg="white", fg="#6e8bc6", font=("times new roman", 20, "bold"))
        # m_title.grid(row=0, columnspan=2, pady=20)

        # #========Product Name==============
        # lbl_product = Label(manage_frame, text="Product Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_product.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # txt_product = Entry(manage_frame, textvariable=self.product_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_product.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # #========Quantity==================
        # lbl_quantity = Label(manage_frame, text="Quantity", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_quantity.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        # txt_quantity = Entry(manage_frame, textvariable=self.quantity_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_quantity.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # #========Price=====================
        # lbl_price = Label(manage_frame, text="Price", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_price.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        # txt_price = Entry(manage_frame, textvariable=self.price_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_price.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # #========Total=====================
        # lbl_total = Label(manage_frame, text="Total", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_total.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        # txt_total = Entry(manage_frame, textvariable=self.total_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_total.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # #========Customer Name==============
        # lbl_customer_name = Label(manage_frame, text="Customer Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_customer_name.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        # txt_customer_name = Entry(manage_frame, textvariable=self.customer_name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_customer_name.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # #========Customer Contact===========
        # lbl_customer_contact = Label(manage_frame, text="Customer Contact", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_customer_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # txt_customer_contact = Entry(manage_frame, textvariable=self.customer_contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # txt_customer_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # #========Button Frame===============
        # btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="white")
        # btn_frame.place(x=0, y=300, width=430, height=70)

        # #========Add Button=================
        # add_btn = Button(btn_frame, text="Add", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # add_btn.grid(row=0, column=0, padx=10, pady=10)
        # # command=self.add_sales,

        # #========Update Button==============
        # update_btn = Button(btn_frame, text="Update", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # update_btn.grid(row=0, column=1, padx=10, pady=10)
        # # command=self.update,

        # #========Delete Button==============
        # delete_btn = Button(btn_frame, text="Delete", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # delete_btn.grid(row=0, column=2, padx=10, pady=10)
        # # command=self.delete,

        # #========Clear Button===============
        # clear_btn = Button(btn_frame, text="Clear", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # clear_btn.grid(row=0, column=3, padx=10, pady=10)
        # # command=self.clear,

        # #========Detail Frame===============
        # detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        # detail_frame.place(x=500, y=100, width=570, height=380)

        # #========Search By==================
        # lbl_search = Label(detail_frame, text="Search By", bg="white", fg="black", font=("times new roman", 15, "bold"))
        # lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # combo_search = ttk.Combobox(detail_frame, font=("times new roman", 13, "bold"), state="readonly", width=10)
        # combo_search["values"] = ("Product", "Customer")
        # combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        # txt_search = Entry(detail_frame, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        # txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        # #========Search Button==============
        # search_btn = Button(detail_frame, text="Search", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # search_btn.grid(row=0, column=3, padx=10, pady=10)
        # # command=self.search,

        # #========Show All Button============
        # show_all_btn = Button(detail_frame, text="Show All", width=10, font=("times new roman", 12, "bold"), bg="#6e8bc6", fg="white")
        # show_all_btn.grid(row=0, column=4, padx=10, pady=10)
        #  #command=self.fetch_data,

        # #========Table Frame================
        # table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="white")
        # table_frame.place(x=10, y=70, width=540, height=290)

        # #========Scroll Bar=================
        # scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        # scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        # self.sales_table = ttk.Treeview(table_frame, columns=("product", "quantity", "price", "total", "customer_name", "customer_contact"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_y.pack(side=RIGHT, fill=Y)
        # scroll_x.config(command=self.sales_table.xview)
        # scroll_y.config(command=self.sales_table.yview)
        # self.sales_table.heading("product", text="Product")
        # self.sales_table.heading("quantity", text="Quantity")
        # self.sales_table.heading("price", text="Price")
        # self.sales_table.heading("total", text="Total")
        # self.sales_table.heading("customer_name", text="Customer Name")
        # self.sales_table.heading("customer_contact", text="Customer Contact")
        # self.sales_table["show"] = "headings"
        # self.sales_table.pack(fill=BOTH, expand=1)
        # #self.sales_table.bind("<ButtonRelease-1>", self.get_cursor)
        # #self.fetch_data()

        # # def add_sales(self):
        # #     pass

        # # def update(self):
        # #     pass

        # # def delete(self):
        # #     pass

        # # def clear(self):
        # #     pass

        # # def search(self):
        # #     pass

        # # def fetch_data(self):
        # #     pass

        # # def get_cursor(self, ev):
        # #     pass

        # # def update_data(self):
        # #     pass

        # # def delete_data(self):
        # #     pass

        # # def search_data(self):
        # #     pass


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()

