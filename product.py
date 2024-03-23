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
        self.product_id_var = StringVar()
        self.product_name_var = StringVar()
        self.product_price_var = StringVar()
        self.product_qty_var = StringVar()

        #==============Title
        title = Label(self.root, text="Inventory Management System", font=("times new roman", 30, "bold"), bg="white", fg="black").place(x=0, y=0, relwidth=1)

        # Manage Frame
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        manage_frame.place(x=20, y=80, width=450, height=400)

        # productClass ID
        lbl_product_id = Label(manage_frame, text="productClass ID", bg="white", fg="black",
                               font=("times new roman", 20, "bold"))
        lbl_product_id.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        txt_product_id = Entry(manage_frame, textvariable=self.product_id_var, font=("times new roman", 15, "bold"),
                               bd=5, relief=GROOVE)
        txt_product_id.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # productClass Name
        lbl_product_name = Label(manage_frame, text="productClass Name", bg="white", fg="black",
                                 font=("times new roman", 20, "bold"))
        lbl_product_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_product_name = Entry(manage_frame, textvariable=self.product_name_var, font=("times new roman", 15, "bold"),
                                 bd=5, relief=GROOVE)
        txt_product_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        # productClass Price
        lbl_product_price = Label(manage_frame, text="productClass Price", bg="white", fg="black",
                                  font=("times new roman", 20, "bold"))
        lbl_product_price.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_product_price = Entry(manage_frame, textvariable=self.product_price_var, font=("times new roman", 15, "bold"),
                                  bd=5, relief=GROOVE)
        txt_product_price.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # productClass Quantity
        lbl_product_qty = Label(manage_frame, text="productClass Quantity", bg="white", fg="black",
                                font=("times new roman", 20, "bold"))
        lbl_product_qty.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_product_qty = Entry(manage_frame, textvariable=self.product_qty_var, font=("times new roman", 15, "bold"),
                                bd=5, relief=GROOVE)
        txt_product_qty.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # Buttons Frame
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=320, width=430, height=70)

        # Add Button
        add_btn = Button(btn_frame, text="Add", width=10, command=self.add_product).grid(row=0, column=0, padx=10, pady=10)

        # Update Button
        update_btn = Button(btn_frame, text="Update", width=10, command=self.update_product).grid(row=0, column=1, padx=10, pady=10)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", width=10, command=self.delete_product).grid(row=0, column=2, padx=10, pady=10)

        # Clear Button
        clear_btn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # Detail Frame
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        detail_frame.place(x=500, y=80, width=750, height=400)

        # Search By
        lbl_search = Label(detail_frame, text="Search By", bg="white", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("productClass ID", "productClass Name", "productClass Price", "productClass Quantity")
        combo_search.grid(row=0, column=1, pady=10, padx=10)

        txt_search = Entry(detail_frame, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        # Search Button
        search_btn = Button(detail_frame, text="Search", width=10, command=self.search_product).grid(row=0, column=3, padx=10, pady=10)

        # Show All Button
        show_all_btn = Button(detail_frame, text="Show All", width=10, command=self.show_all).grid(row=0, column=4, padx=10, pady=10)

        # Table Frame
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=70, width=720, height=300)

        # Scrollbar
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(table_frame, columns=("product_id", "product_name", "product_price", "product_qty"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("product_id", text="productClass ID")
        self.product_table.heading("product_name", text="productClass Name")
        self.product_table.heading("product_price", text="productClass Price")
        self.product_table.heading("product_qty", text="productClass Quantity")

        self.product_table['show'] = 'headings'

        self.product_table.column("product_id", width=100)
        self.product_table.column("product_name", width=200)
        self.product_table.column("product_price", width=100)
        self.product_table.column("product_qty", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.show_all()

    def add_product(self):
        pass

    def update_product(self):
        pass

    def delete_product(self):
        pass

    def clear(self):
        pass

    def search_product(self):
        pass

    def show_all(self):
        pass

    def get_cursor(self, ev):
        pass


root = Tk()
obj = productClass(root)
root.mainloop()
