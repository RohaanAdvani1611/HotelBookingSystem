from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Employee_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Variables
        self.var_EmpID = StringVar()
        x = random.randint(1000, 9999)
        self.var_EmpID.set(str(x))

        self.var_EmpName = StringVar()
        self.var_Contact = StringVar()
        self.var_Desig = StringVar()
        self.var_RoomNo = StringVar()

        # Title
        lbl1 = Label(self.root, text="ADD EMPLOYEE DETAILS", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Employee Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=270)

        img1n = Image.open("pic27.png")
        img1n = img1n.resize((425,190), Image.ANTIALIAS)
        self.photoimg1n = ImageTk.PhotoImage(img1n)
        lbl2n = Label(self.root, image=self.photoimg1n, bd=0, relief=RIDGE)
        lbl2n.place(x=5, y=330, width=425, height=190)

        img1o = Image.open("pic28.png")
        img1o = img1o.resize((850, 230), Image.ANTIALIAS)
        self.photoimg1o = ImageTk.PhotoImage(img1o)
        lbl2o = Label(self.root, image=self.photoimg1o, bd=0, relief=RIDGE)
        lbl2o.place(x=435, y=50, width=850, height=230)

        # Employee details
        # emp_id
        lbl_eid = Label(lableframeleft, text="Employee ID : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_eid.grid(row=0, column=0, sticky=W)
        entry_eid = ttk.Entry(lableframeleft, textvariable=self.var_EmpID, width=29,
                                  font=("times new roman", 13, "bold"), state="readonly")
        entry_eid.grid(row=0, column=1, sticky=W)

        # emp_name
        lbl_ename = Label(lableframeleft, text="Employee Name : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_ename.grid(row=1, column=0, sticky=W)
        entry_ename = ttk.Entry(lableframeleft, textvariable=self.var_EmpName, width=29,
                                  font=("times new roman", 13, "bold"))
        entry_ename.grid(row=1, column=1)

        # roomno
        lbl_roomno = Label(lableframeleft, text="Room No : ", font=("times new roman", 12, "bold"),  padx=2, pady=6)
        lbl_roomno.grid(row=2, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from roomdetails")
        rows = my_cursor.fetchall()

        combo_roomno = ttk.Combobox(lableframeleft, textvariable=self.var_RoomNo,
                                    font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_roomno["value"] = rows
        # combo_roomno.current(0)
        combo_roomno.grid(row=2, column=1)

        # emp_contact
        lbl_contact = Label(lableframeleft, text="Contact no : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_contact.grid(row=3, column=0, sticky=W)
        entry_contact = ttk.Entry(lableframeleft, textvariable=self.var_Contact, width=29,
                                   font=("times new roman", 13, "bold"))
        entry_contact.grid(row=3, column=1)

        # Desig
        lbl_desig = Label(lableframeleft, text="Desig : ", font=("times new roman", 12, "bold"),
                                  padx=2, pady=6)
        lbl_desig.grid(row=4, column=0, sticky=W)
        entry_desig = ttk.Entry(lableframeleft, textvariable=self.var_Desig, width=29,
                                  font=("times new roman", 13, "bold"))
        entry_desig.grid(row=4, column=1)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=190, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=10, padx=1)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=10, padx=1)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("times new roman", 12, "bold"),
                            bg="black", fg="gold", width=10, padx=1)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 12, "bold"), bg="black",
                          fg="gold", width=10, padx=1)
        btnReset.grid(row=0, column=3)

        # Table Frame
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", padx=2,
                                font=("times new roman", 12, "bold"))
        TableFrame.place(x=435, y=280, width=860, height=260)

        lbl_searchby = Label(TableFrame, text="Search By : ", font=("times new roman", 12, "bold"), bg="red",
                             fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(TableFrame,textvariable=self.search_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("EmpID")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_emp_search = ttk.Entry(TableFrame, width=24,textvariable=self.txt_search, font=("times new roman", 13, "bold"))
        entry_emp_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(TableFrame, text="Search", command=self.search, font=("times new roman", 12, "bold"),
                           bg="black", fg="gold", width=10, padx=1)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(TableFrame, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"),
                            bg="black", fg="gold", width=10, padx=1)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=180)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.room_table = ttk.Treeview(DetailsFrame, column=(
        "EmpID", "EmpName","RoomNo", "Contact", "Desig"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("EmpID", text="Employee ID")
        self.room_table.heading("EmpName", text="Employee Name")
        self.room_table.heading("RoomNo", text="Room Number")
        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Desig", text="Designation")

        self.room_table["show"] = "headings"
        self.room_table.column("EmpID", width=100)
        self.room_table.column("EmpName", width=100)
        self.room_table.column("RoomNo",width=100) 
        self.room_table.column("Contact", width=100)
        self.room_table.column("Desig", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_EmpID.get() == "" or self.var_EmpName.get() == "":
            messagebox.showerror("Error", "All details are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s)", (
                    self.var_EmpID.get(),
                    self.var_EmpName.get(),
                    self.var_RoomNo.get(),
                    self.var_Contact.get(),
                    self.var_Desig.get()
                ))

                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "employee added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong :{str(es)}", parent=self.root)

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from employee")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)
                conn.commit()
            conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_EmpID.set(row[0])
        self.var_EmpName.set(row[1])
        self.var_RoomNo.set(row[2])
        self.var_Contact.set(row[3])
        self.var_Desig.set(row[4])

    # UPDATE ROOM
    def update(self):
        if self.var_EmpName.get() == "":
            messagebox.showerror("Error", "please enter the employee name", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update employee set EmpName = %s,RoomNo= %s, Contact = %s, Desig = %s where EmpID =(%s)",
                (
                    self.var_EmpName.get(),
                    self.var_RoomNo.get(),
                    self.var_Contact.get(),
                    self.var_Desig.get(),
                    self.var_EmpID.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Employee details have been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this employee",parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()
            query = "delete from employee where EmpID=%s;"
            value = (self.var_EmpID.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_EmpName.set("")
        self.var_Contact.set("")
        self.var_Desig.set("")
        x = random.randint(1000, 9999)
        self.var_EmpID.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()

        p = str(self.search_var.get())
        if p == "EmpID":
            my_cursor.execute("select * from employee where " + str(self.search_var.get()) + " like '%" + str(
                self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Employee_Window(root)
    root.mainloop()






