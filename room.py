from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Room_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_RoomNo = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_totalcost = StringVar()

        # Title
        lbl1 = Label(self.root, text="BOOK ROOM", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=490)

        img1a = Image.open("pic21.jpg")
        img1a = img1a.resize((430, 225), Image.ANTIALIAS)
        self.photoimg1a = ImageTk.PhotoImage(img1a)
        lbl2a = Label(self.root, image=self.photoimg1a, bd=0, relief=RIDGE)
        lbl2a.place(x=430, y=50, width=430, height=225)

        img1b = Image.open("pic22.jpg")
        img1b = img1b.resize((430, 225), Image.ANTIALIAS)
        self.photoimg1b = ImageTk.PhotoImage(img1b)
        lbl2b = Label(self.root, image=self.photoimg1b, bd=0, relief=RIDGE)
        lbl2b.place(x=865, y=50, width=430, height=225)

        # Room details
        # custContact
        lbl_contact = Label(lableframeleft, text="Customer Contact : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_contact.grid(row=0, column=0, sticky=W)
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select Contact from customer")
        rows=my_cursor.fetchall()
        combo_Contact = ttk.Combobox(lableframeleft,textvariable = self.var_contact, font=("times new roman", 12, "bold"), width=15, state="readonly")
        combo_Contact["value"] = rows
        combo_Contact.grid(row=0, column=1)
        btnFetch = Button(lableframeleft, command=self.fetch_contact, text="Fetch", font=("times new roman", 9, "bold"), bg="black", fg="gold", width=8,
                        padx=1)
        btnFetch.place(x=347, y=4)

        # custCheckin
        lbl_checkin = Label(lableframeleft, text="Check In Date : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_checkin.grid(row=1, column=0, sticky=W)
        entry_checkin = ttk.Entry(lableframeleft,textvariable = self.var_checkin, width=29, font=("times new roman", 13, "bold"))
        entry_checkin.grid(row=1, column=1)

        # custCheckout
        lbl_checkout = Label(lableframeleft, text="Check Out Date : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_checkout.grid(row=2, column=0, sticky=W)
        entry_checkout = ttk.Entry(lableframeleft,textvariable = self.var_checkout, width=29, font=("times new roman", 13, "bold"))
        entry_checkout.grid(row=2, column=1)

        #Room Type
        lbl_roomtype = Label(lableframeleft, text="Room Type : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from roomdetails")
        ide=my_cursor.fetchall()

        combo_roomtype = ttk.Combobox(lableframeleft,textvariable = self.var_roomtype, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_roomtype["value"] = ide
        combo_roomtype.grid(row=3, column=1)

        # Available room
        lbl_availableroom = Label(lableframeleft, text="Available Room : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_availableroom.grid(row=4, column=0, sticky=W)
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from roomdetails")
        rows=my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(lableframeleft,textvariable = self.var_RoomNo, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(lableframeleft, text="Inclusive Meal : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        combo_meal = ttk.Combobox(lableframeleft, textvariable=self.var_meal, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_meal["value"] = ("Breakfast", "Lunch","Dinner")
        combo_meal.grid(row=5, column=1)

        # No of days
        lbl_days = Label(lableframeleft, text="Number of Days : ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_days.grid(row=6, column=0, sticky=W)
        entry_days = ttk.Entry(lableframeleft,textvariable = self.var_noofdays, width=29, font=("times new roman", 13, "bold"))
        entry_days.grid(row=6, column=1)

        # Paid Tax
        lbl_tax = Label(lableframeleft, text="Paid Tax : ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_tax.grid(row=7, column=0, sticky=W)
        entry_tax = ttk.Entry(lableframeleft,textvariable = self.var_paidtax, width=29, font=("times new roman", 13, "bold"))
        entry_tax.grid(row=7, column=1)

        # Sub Total
        lbl_st = Label(lableframeleft, text="Sub Total : ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_st.grid(row=8, column=0, sticky=W)
        entry_st = ttk.Entry(lableframeleft,textvariable = self.var_subtotal, width=29, font=("times new roman", 13, "bold"))
        entry_st.grid(row=8, column=1)

        # Total Cost
        lbl_tc = Label(lableframeleft, text="Total Cost : ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_tc.grid(row=9, column=0, sticky=W)
        entry_tc = ttk.Entry(lableframeleft,textvariable = self.var_totalcost, width=29, font=("times new roman", 13, "bold"))
        entry_tc.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(lableframeleft, text="Bill",command=self.total, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10,
                        padx=1)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=430, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10,
                        padx=1)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("times new roman", 12, "bold"), bg="black", fg="gold",
                           width=10,
                           padx=1)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="Delete",command= self.mDelete,font=("times new roman", 12, "bold"), bg="black", fg="gold",
                           width=10,
                           padx=1)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("times new roman", 12, "bold"), bg="black", fg="gold",
                          width=10,
                          padx=1)
        btnReset.grid(row=0, column=3)

        # Table Frame
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", padx=2,
                                font=("times new roman", 12, "bold"))
        TableFrame.place(x=435, y=280, width=860, height=260)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("times new roman", 12, "bold"), bg="red",
                             fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)
        self.search_var=StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)
        self.txt_search=StringVar()
        entry_cust_search = ttk.Entry(TableFrame, width=24,textvariable=self.txt_search, font=("times new roman", 13, "bold"))
        entry_cust_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="Search",command = self.search,font=("times new roman", 12, "bold"), bg="black", fg="gold",
                           width=10, padx=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="Show All",command=self.fetch_data, font=("times new roman", 12, "bold"), bg="black", fg="gold",
                            width=10, padx=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=180)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.room_table = ttk.Treeview(DetailsFrame, column=("Contact", "CheckIn", "CheckOut", "RoomType", "RoomNo", "Meal", "Days"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact num")
        self.room_table.heading("CheckIn", text="Check In")
        self.room_table.heading("CheckOut", text="Check Out")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomNo", text="RoomNo")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("Days", text="Number Of Days")

        self.room_table["show"] = "headings"
        self.room_table.column("Contact", width=100)
        self.room_table.column("CheckIn", width=100)
        self.room_table.column("CheckOut", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("Days", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_RoomNo.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get()
                                                                        ))
                                                                                                                                                                                                          
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows :
                    self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_RoomNo.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    #UPDATE ROOM
    def update (self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter the number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
            my_cursor=conn.cursor()
            
            my_cursor.execute("update room set check_in = %s, check_out = %s, RoomType = %s, RoomNo = %s, meal =%s, days = %s  where Contact =(%s)",(
                                                                                                                             
                                                                                                                        self.var_checkin.get(),
                                                                                                                        self.var_checkout.get(),
                                                                                                                        self.var_roomtype.get(),
                                                                                                                        self.var_RoomNo.get(),
                                                                                                                        self.var_meal.get(),
                                                                                                                        self.var_noofdays.get(),
                                                                                                                        self.var_contact.get()        
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details have been updated successfully",parent=self.root)
 
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
            my_cursor=conn.cursor()
            query ="delete from room where Contact=%s;"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_RoomNo.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_totalcost.set("")

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Valid Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor=conn.cursor()
            query = ("select CustName from customer where Contact = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblname = Label(showDataframe, text="Name:", font=("times new roman", 12, "bold"))
                lblname.place(x=0, y=0)

                lbla = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbla.place(x=90, y=0)

                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Contact =%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("times new roman", 12, "bold"))
                lblgender.place(x=0, y=30)

                lblb = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lblb.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Contact =%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblem = Label(showDataframe, text="Email ID:", font=("times new roman", 12, "bold"))
                lblem.place(x=0, y=60)

                lblc = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lblc.place(x=90, y=60)

                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Contact =%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladd = Label(showDataframe, text="Address:", font=("times new roman", 12, "bold"))
                lbladd.place(x=0, y=90)

                lbld = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbld.place(x=90, y=90)


                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                query = ("select CustomerID from customer where Contact =%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblID = Label(showDataframe, text="CustomerID:", font=("times new roman", 12, "bold"))
                lblID.place(x=0, y=120)

                lble = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lble.place(x=90, y=120)
    # SEARCH
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
        my_cursor=conn.cursor()
       
        p = str(self.search_var.get())
        if p == "Contact":
            my_cursor.execute("select * from room where "+str(self.search_var.get())+" like '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()  
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(100)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Family"):
            q1=float(100)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Family"):
            q1=float(200)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Family"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            subTotal="Rs."+str("%.2f"%((q5)))
            Total="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(subTotal)
            self.var_totalcost.set(Total)
        else :
             return

if __name__ == "__main__":
    root = Tk()
    obj = Room_Window(root)
    root.mainloop()