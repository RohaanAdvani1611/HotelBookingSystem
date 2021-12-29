from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Amenities_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Variables
        self.var_amen_name = StringVar()
        self.var_RoomNo = StringVar()
        self.var_amen_cost = StringVar()

        # Title
        lbl1 = Label(self.root, text="BOOK AMENITIES", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Amenity Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=230)

        img1i = Image.open("pic33.jpg")
        img1i = img1i.resize((425, 230), Image.ANTIALIAS)
        self.photoimg1i = ImageTk.PhotoImage(img1i)
        lbl2i = Label(self.root, image=self.photoimg1i, bd=0, relief=RIDGE)
        lbl2i.place(x=5, y=290, width=425, height=230)

        img1j = Image.open("pic34.jpg")
        img1j = img1j.resize((280, 230), Image.ANTIALIAS)
        self.photoimg1j = ImageTk.PhotoImage(img1j)
        lbl2j = Label(self.root, image=self.photoimg1j, bd=0, relief=RIDGE,padx=2)
        lbl2j.place(x=435, y=50, width=280, height=220)

        img1k = Image.open("pic35.jpg")
        img1k = img1k.resize((280, 230), Image.ANTIALIAS)
        self.photoimg1k = ImageTk.PhotoImage(img1k)
        lbl2k = Label(self.root, image=self.photoimg1k, bd=0, relief=RIDGE,padx=2)
        lbl2k.place(x=715, y=50, width=280, height=220)

        img1m = Image.open("pic36.jpg")
        img1m = img1m.resize((280, 230), Image.ANTIALIAS)
        self.photoimg1m = ImageTk.PhotoImage(img1m)
        lbl2m = Label(self.root, image=self.photoimg1m, bd=0, relief=RIDGE,padx=2)
        lbl2m.place(x=995, y=50, width=280, height=220)

        # Amenity details
        # amen_name
        lbl_amen_name = Label(lableframeleft, text="Amenity Name : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_amen_name.grid(row=0, column=0, sticky=W)
        combo_amen_name = ttk.Combobox(lableframeleft, textvariable=self.var_amen_name,
                                      font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_amen_name["value"] = ("Swimming pool", "Gym", "Spa", "Sauna", "Indoor Games")
        combo_amen_name.current(0)
        combo_amen_name.grid(row=0, column=1)

        # RoomNo
        lbl_RoomNo = Label(lableframeleft, text="Room No : ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from roomdetails")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(lableframeleft, textvariable=self.var_RoomNo,
                                    font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_RoomNo["value"] = rows
        # combo_RoomNo.current(0)
        combo_RoomNo.grid(row=1, column=1)

        # Amenity Cost
        lbl_amen_cost = Label(lableframeleft, text="Amenity Cost : ", font=("times new roman", 12, "bold"), padx=2,
                       pady=6)
        lbl_amen_cost.grid(row=2, column=0, sticky=W)
        entry_amen_cost = ttk.Entry(lableframeleft, textvariable=self.var_amen_cost, width=29,
                             font=("times new roman", 13, "bold"), state="readonly")
        entry_amen_cost.grid(row=2, column=1)

        # Bill Button
        btnBill = Button(lableframeleft, text="Bill", command=self.total, font=("times new roman", 12, "bold"),
                         bg="black", fg="gold", width=10, padx=1)
        btnBill.grid(row=3, column=0, padx=1, sticky=W)

        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=412, height=40)

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
            "amen_name", "RoomNo", "amen_cost"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("amen_name", text="Amenity Name")
        self.room_table.heading("RoomNo", text="Room No")
        self.room_table.heading("amen_cost", text="Amenity Cost")

        self.room_table["show"] = "headings"
        self.room_table.column("amen_name", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("amen_cost", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_RoomNo.get() == "" :
            messagebox.showerror("Error", "All details are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into amenities values(%s,%s,%s)", (
                    self.var_amen_name.get(),
                    self.var_RoomNo.get(),
                    self.var_amen_cost.get()
                ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Amenity booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from amenities")
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

        self.var_amen_name.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_amen_cost.set(row[2])

    # UPDATE ROOM
    def update(self):
        if self.var_RoomNo.get() == "":
            messagebox.showerror("Error", "please enter the room no", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update amenities set amen_name = %s, amen_cost = %s where RoomNo =(%s)",
                (
                    self.var_amen_name.get(),
                    self.var_amen_cost.get(),
                    self.var_RoomNo.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Amenity booking details have been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this amenity booking",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()
            query = "delete from amenities where RoomNo=%s;"
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_amen_name.set("")
        self.var_RoomNo.set("")
        self.var_amen_cost.set("")

    def total(self):
        Amenity = self.var_amen_name.get()

        if (Amenity == "Swimming pool"):
            q1 = float(100)
            Total = "Rs." + str("%.2f" % (+ q1))
            self.var_amen_cost.set(Total)

        elif (Amenity == "Gym"):
            q1 = float(200)
            Total = "Rs." + str("%.2f" % (+ q1))
            self.var_amen_cost.set(Total)

        elif (Amenity == "Spa"):
            q1 = float(1000)
            Total = "Rs." + str("%.2f" % (+ q1))
            self.var_amen_cost.set(Total)

        elif (Amenity == "Sauna"):
            q1 = float(500)
            Total = "Rs." + str("%.2f" % (+ q1))
            self.var_amen_cost.set(Total)

        elif (Amenity == "Indoor Games"):
            q1 = float(200)
            Total = "Rs." + str("%.2f" % (+ q1))
            self.var_amen_cost.set(Total)

        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Amenities_Window(root)
    root.mainloop()