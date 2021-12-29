from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Customer_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Variables
        self.var_ID= StringVar()
        x= random.randint(1000,9999)
        self.var_ID.set(str(x))
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobileNumber=StringVar()
        self.var_Email=StringVar()
        self.var_Address=StringVar()
        
        # Title
        lbl1 = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Image
        img2 = Image.open("pic8.jfif")
        img2 = img2.resize((425, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl3 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl3.place(x=5, y=330, width=425, height=200)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=320)

        # Customer details
        # custID
        lbl_cust_id = Label(lableframeleft, text="Customer ID : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)
        entry_cust_id = ttk.Entry(lableframeleft, width=29,textvariable=self.var_ID, font=("times new roman", 13, "bold"),state="readonly")
        entry_cust_id.grid(row=0, column=1)

        # Name
        lbl_cust_name = Label(lableframeleft, text="Customer Name : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_cust_name = ttk.Entry(lableframeleft, width=29,textvariable=self.var_name, font=("times new roman", 13, "bold"))
        entry_cust_name.grid(row=1, column=1)

        # Gender
        lbl_cust_gender = Label(lableframeleft, text="Gender : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_gender.grid(row=2, column=0, sticky=W)
        combo_gender = ttk.Combobox(lableframeleft,textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)

        # MobileNo:
        lbl_cust_mob = Label(lableframeleft, text="Contact : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_mob.grid(row=3, column=0, sticky=W)
        entry_cust_mob = ttk.Entry(lableframeleft, width=29,textvariable=self.var_mobileNumber,font=("times new roman", 13, "bold"))
        entry_cust_mob.grid(row=3, column=1)

        # Email
        lbl_cust_email = Label(lableframeleft, text="Email ID : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_email.grid(row=4, column=0, sticky=W)
        entry_cust_email = ttk.Entry(lableframeleft, width=29,textvariable=self.var_Email, font=("times new roman", 13, "bold"))
        entry_cust_email.grid(row=4, column=1)

        # Address
        lbl_cust_add = Label(lableframeleft, text="Address : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_add.grid(row=5, column=0, sticky=W)
        entry_cust_add = ttk.Entry(lableframeleft, width=29,textvariable=self.var_Address, font=("times new roman", 13, "bold"))
        entry_cust_add.grid(row=5, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command= self.add_data,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10,
                        padx=1)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10,
                        padx=1)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10,
                        padx=1)
        btnReset.grid(row=0, column=3)

        # Table Frame search system
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", padx=2,
                                    font=("times new roman", 12, "bold"))
        TableFrame.place(x=435, y=50, width=860, height=490)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("times new roman", 12, "bold"), bg="red", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var,font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact", "CustomerID")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        entry_cust_search = ttk.Entry(TableFrame,textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
        entry_cust_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="Search",command=self.search, font=("times new roman", 12, "bold"), bg="black", fg="gold",
                          width=10, padx=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="Show All",command=self.fetch_data, font=("times new roman", 12, "bold"), bg="black", fg="gold",
                          width=10, padx=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=350)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(DetailsFrame, column=("ID", "Name", "Gen", "Mob", "Em", "Add"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ID", text="CustomerID")
        self.Cust_Details_Table.heading("Name", text="CustName")
        self.Cust_Details_Table.heading("Gen", text="Gender")
        self.Cust_Details_Table.heading("Mob", text="Contact:")
        self.Cust_Details_Table.heading("Em", text="Email")
        self.Cust_Details_Table.heading("Add", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ID", width=100)
        self.Cust_Details_Table.column("Name", width=100)
        self.Cust_Details_Table.column("Gen", width=100)
        self.Cust_Details_Table.column("Mob", width=100)
        self.Cust_Details_Table.column("Em", width=100)
        self.Cust_Details_Table.column("Add", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobileNumber.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_ID.get(),
                                                                        self.var_name.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_mobileNumber.get(),
                                                                        self.var_Email.get(),
                                                                        self.var_Address.get()

                                                                    ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)    
              
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows :
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.var_ID.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobileNumber.set(row[3]),
        self.var_Email.set(row[4]),
        self.var_Address.set(row[5])
    
    def update (self):
        if self.var_mobileNumber.get()=="":
            messagebox.showerror("Error","please enter the number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
            my_cursor=conn.cursor()
            
            my_cursor.execute("update customer set Name= %s,Gender = %s, Contact = %s,`Email ID` = %s, Address = %s  where CustomerID =(%s)",(
                                                                                                                             
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_mobileNumber.get(),
                                                                                                                        self.var_Email.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_ID.get()        
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details have been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
            my_cursor=conn.cursor()
            query ="delete from customer where CustomerID=%s;"
            value=(self.var_ID.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_mobileNumber.set(""),
        self.var_Email.set(""),
        self.var_Address.set("")
        x= random.randint(1000,9999)
        self.var_ID.set(str(x))
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
        my_cursor=conn.cursor()
        p = str(self.search_var.get())
        if p == "ContactID":
            my_cursor.execute("select * from customer where "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")
        else:
            my_cursor.execute("select * from customer where `"+str(self.search_var.get())+"` like '%"+str(self.txt_search.get())+"%'")        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
if __name__ == "__main__":
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()