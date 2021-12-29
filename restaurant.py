from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Restaurant_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Variables
        self.var_restname = StringVar()
        self.var_meal = StringVar()
        self.var_roomno = StringVar()
        self.var_mealcost = StringVar()

        # Title
        lbl1 = Label(self.root, text="BOOK TABLE AT RESTAURANT", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Restaurant Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=300)

        img1f = Image.open("pic31.jpg")
        img1f = img1f.resize((425, 170), Image.ANTIALIAS)
        self.photoimg1f = ImageTk.PhotoImage(img1f)
        lbl2f = Label(self.root, image=self.photoimg1f, bd=0, relief=RIDGE)
        lbl2f.place(x=5, y=360, width=425, height=170)

        img1g = Image.open("pic40.jpg")
        img1g = img1g.resize((425, 220), Image.ANTIALIAS)
        self.photoimg1g = ImageTk.PhotoImage(img1g)
        lbl2g = Label(self.root, image=self.photoimg1g, bd=0, relief=RIDGE)
        lbl2g.place(x=430, y=50, width=425, height=220)

        img1h = Image.open("pic30.jpg")
        img1h = img1h.resize((425, 220), Image.ANTIALIAS)
        self.photoimg1h = ImageTk.PhotoImage(img1h)
        lbl2h = Label(self.root, image=self.photoimg1h, bd=0, relief=RIDGE)
        lbl2h.place(x=860, y=50, width=425, height=220)

        # Restaurant details
        # rest_name
        lbl_restname = Label(lableframeleft, text="Restaurant Name : ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lbl_restname.grid(row=0, column=0, sticky=W)
        combo_restname = ttk.Combobox(lableframeleft, textvariable=self.var_restname, font=("times new roman", 12, "bold"),
                                    width=27, state="readonly")
        combo_restname["value"] = ("Golden Grill House", "Chinatown", "Spice Kitchen", "Little Bakery")
        combo_restname.current(0)
        combo_restname.grid(row=0, column=1)

        # Meal
        lbl_meal = Label(lableframeleft, text="Meal : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=1, column=0, sticky=W)
        combo_meal = ttk.Combobox(lableframeleft, textvariable=self.var_meal, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_meal["value"] = ("Lunch buffet", "Dinner buffet")
        combo_meal.current(0)
        combo_meal.grid(row=1, column=1)

        # roomno
        lbl_roomno = Label(lableframeleft, text="Room No : ", font=("times new roman", 12, "bold"),  padx=2, pady=6)
        lbl_roomno.grid(row=2, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from roomdetails")
        rows = my_cursor.fetchall()

        combo_roomno = ttk.Combobox(lableframeleft, textvariable=self.var_roomno,
                                    font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_roomno["value"] = rows
        # combo_roomno.current(0)
        combo_roomno.grid(row=2, column=1)

        # Meal Cost
        lbl_mealcost = Label(lableframeleft, text="Meal Cost : ", font=("times new roman", 12, "bold"), padx=2,
                       pady=6)
        lbl_mealcost.grid(row=3, column=0, sticky=W)
        entry_mealcost = ttk.Entry(lableframeleft, textvariable=self.var_mealcost, width=29,
                             font=("times new roman", 13, "bold"), state="readonly")
        entry_mealcost.grid(row=3, column=1)

        # Bill Button
        btnBill = Button(lableframeleft, text="Bill", command=self.total, font=("times new roman", 12, "bold"),
                         bg="black", fg="gold", width=10, padx=1)
        btnBill.grid(row=4, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=230, width=412, height=40)

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
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details", padx=2,
                                font=("times new roman", 12, "bold"))
        TableFrame.place(x=435, y=280, width=860, height=260)

        btnShowAll = Button(TableFrame, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"),
                            bg="black", fg="gold", width=10, padx=1)
        btnShowAll.grid(row=0, column=0, padx=2)

        # Show Data Table
        DetailsFrame = Frame(TableFrame, bd=2, relief=RIDGE)
        DetailsFrame.place(x=0, y=50, width=830, height=180)

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.room_table = ttk.Treeview(DetailsFrame, column=(
            "restname", "meal", "roomno", "mealcost"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("restname", text="Restaurant Name")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("mealcost", text="Meal Cost")

        self.room_table["show"] = "headings"
        self.room_table.column("restname", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("mealcost", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_roomno.get() == "" or self.var_meal.get() == "":
            messagebox.showerror("Error", "All details are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into restaurant values(%s,%s,%s,%s)", (
                    self.var_restname.get(),
                    self.var_meal.get(),
                    self.var_roomno.get(),
                    self.var_mealcost.get()
                ))

                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Table booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from restaurant")
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

        self.var_restname.set(row[0])
        self.var_meal.set(row[1])
        self.var_roomno.set(row[2])
        self.var_mealcost.set(row[3])

    # UPDATE ROOM
    def update(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "please enter the room no", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update restaurant set restname = %s, meal = %s, mealcost = %s where roomno =(%s)",
                (
                    self.var_restname.get(),
                    self.var_meal.get(),
                    self.var_mealcost.get(),
                    self.var_roomno.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Table booking details have been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System","Do you want to delete this table booking",parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()
            query = "delete from restaurant where roomno=%s;"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_restname.set("")
        self.var_meal.set("")
        self.var_roomno.set("")
        self.var_mealcost.set("")

    def total(self):
        Restname=self.var_restname.get()
        Mealtype=self.var_meal.get()  
        if(self.var_meal.get()=="Lunch buffet" and self.var_restname.get()=="Golden Grill House"):
            q1=float(600)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Dinner buffet" and self.var_restname.get()=="Golden Grill House"):
            q1=float(700)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Lunch buffet" and self.var_restname.get()=="Chinatown"):
            q1=float(400)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Dinner buffet" and self.var_restname.get()=="Chinatown"):
            q1=float(500)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Lunch buffet" and self.var_restname.get()=="Spice Kitchen"):
            q1=float(700)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Dinner buffet" and self.var_restname.get()=="Spice Kitchen"):
            q1=float(800)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Lunch buffet" and self.var_restname.get()=="Little Bakery"):
            q1=float(300)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        elif(self.var_meal.get()=="Dinner buffet" and self.var_restname.get()=="Little Bakery"):
            q1=float(400)
            Total="Rs."+str("%.2f"%(+ q1))
            self.var_mealcost.set(Total)

        else :
             return

if __name__ == "__main__":
    root = Tk()
    obj = Restaurant_Window(root)
    root.mainloop()


