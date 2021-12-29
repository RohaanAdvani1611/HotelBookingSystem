from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class detailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1295x550+0+0")

        # Title
        lbl1 = Label(self.root, text="CONFIGURE ROOMS", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=1295, height=50)

        # Logo
        img1 = Image.open("pic7.jfif")
        img1 = img1.resize((100, 40), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=2, width=100, height=40)

        # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Rooms", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=425, height=220)

        img1c = Image.open("pic23.jpg")
        img1c = img1c.resize((425, 250), Image.ANTIALIAS)
        self.photoimg1c = ImageTk.PhotoImage(img1c)
        lbl2c = Label(self.root, image=self.photoimg1c, bd=0, relief=RIDGE)
        lbl2c.place(x=5, y=280, width=425, height=250)

        # floor
        lbl_floor = Label(lableframeleft, text="Floor : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(lableframeleft, textvariable=self.var_floor, width=20,
                                  font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        # roomno
        lbl_roomno = Label(lableframeleft, text="Room No : ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lbl_roomno.grid(row=1, column=0, sticky=W)

        self.var_roomno = StringVar()
        entry_roomno = ttk.Entry(lableframeleft, textvariable=self.var_roomno, width=20,
                                font=("times new roman", 13, "bold"))
        entry_roomno.grid(row=1, column=1, sticky=W)

        # roomtype
        lbl_roomtype = Label(lableframeleft, text="Room Type : ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)

        self.var_roomtype = StringVar()
        combo_roomtype = ttk.Combobox(lableframeleft, textvariable=self.var_roomtype, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_roomtype["value"] = ("Single", "Double","Family")
        combo_roomtype.grid(row=2, column=1)

        btn_fetch = Button(lableframeleft, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=10,
                        padx=1)
        btn_fetch.grid(row=3, column=1)
       
        # Buttons
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=155, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("times new roman", 12, "bold"), bg="black",
                        fg="gold", width=10,
                        padx=1)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 12, "bold"),
                           bg="black", fg="gold",
                           width=10,
                           padx=1)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("times new roman", 12, "bold"),
                           bg="black", fg="gold",
                           width=10,
                           padx=1)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 12, "bold"), bg="black",
                          fg="gold",
                          width=10,
                          padx=1)
        btnReset.grid(row=0, column=3)

        # Table Frame
        TableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", padx=2,
                                font=("times new roman", 12, "bold"))
        TableFrame.place(x=440, y=55, width=600, height=470)

        img1d = Image.open("pic24.jpg")
        img1d = img1d.resize((237, 240), Image.ANTIALIAS)
        self.photoimg1d = ImageTk.PhotoImage(img1d)
        lbl2d = Label(self.root, image=self.photoimg1d, bd=0, relief=RIDGE)
        lbl2d.place(x=1050, y=55, width=237, height=240)

        img1e = Image.open("pic25.jpg")
        img1e = img1e.resize((237, 230), Image.ANTIALIAS)
        self.photoimg1e = ImageTk.PhotoImage(img1e)
        lbl2e = Label(self.root, image=self.photoimg1e, bd=0, relief=RIDGE)
        lbl2e.place(x=1050, y=300, width=237, height=230)

        scroll_x = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.room_table = ttk.Treeview(TableFrame, column=(
        "floor", "RoomType", "Roomno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="floor")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("Roomno", text="Room Number")

        self.room_table["show"] = "headings"
        self.room_table.column("floor", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("Roomno", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All details are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into roomdetails values (%s,%s,%s)", (
                                                                    self.var_floor.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_roomno.get()
                                                                ))

                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "room added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong :{str(es)}", parent=self.root)

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from roomdetails")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows :
                    self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    # UPDATE ROOM
    def update(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "please enter the Room Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hms")
            my_cursor = conn.cursor()

            my_cursor.execute(
                "update roomdetails set floor = %s, RoomType = %s where RoomNo =(%s)",
                (
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
            my_cursor=conn.cursor()
            query ="delete from roomdetails where RoomNo=%s;"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data
        conn.close()

    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")

if __name__ == "__main__":
    root = Tk()
    obj = detailsRoom(root)
    root.mainloop()