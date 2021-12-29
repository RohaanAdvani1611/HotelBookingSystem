from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class About_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("400x400+0+0")

        self.var_CustID=StringVar()
        self.var_CustName=StringVar()
        self.var_Feedback=StringVar()

        lbl1 = Label(self.root, text="About & Feedback", font=("times new roman", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=400, height=50)

        lableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="", padx=2, font=("times new roman", 12, "bold"))
        lableframe.place(x=5, y=55, width=390, height=340)

        lbl2 = Label(lableframe, text="Developers: ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl2.grid(row=0, column=0, sticky=W)

        lbl3 = Label(lableframe, text="Mohit Zanwar ", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl3.grid(row=0, column=1, sticky=W)

        lbl4 = Label(lableframe, text="Rohaan Advani", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl4.grid(row=1, column=1, sticky=W)

        lbl5 = Label(lableframe, text="CustName", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl5.grid(row=2, column=0, sticky=W)
        entry5= ttk.Entry(lableframe, width=24,textvariable=self.var_CustName, font=("times new roman", 13, "bold"))
        entry5.grid(row=2, column=1)

        lbl6 = Label(lableframe, text="CustID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl6.grid(row=3, column=0, sticky=W)
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select CustomerID from customer")
        rows=my_cursor.fetchall()

        combo_CustID = ttk.Combobox(lableframe,textvariable = self.var_CustID, font=("times new roman", 12, "bold"), width=15, state="readonly")
        combo_CustID["value"] = rows
        combo_CustID.grid(row=3, column=1)

        lbl7 = Label(lableframe, text="Feedback", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl7.grid(row=4, column=0, sticky=W)
        entry7= ttk.Entry(lableframe, width=24,textvariable=self.var_Feedback, font=("times new roman", 13, "bold"))
        entry7.grid(row=4, column=1)

        Submit = Button(lableframe, text="Submit",command= self.submit, font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10, padx=1)
        Submit.grid(row=7, column=1)

    def submit(self):
        if self.var_CustID.get()=="":
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hms") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into feedback values(%s,%s,%s)",(
                                                                        self.var_CustID.get(),
                                                                        self.var_CustName.get(),
                                                                        self.var_Feedback.get()
                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Feedback has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)    
              
if __name__ == "__main__":
    root = Tk()
    obj = About_Window(root)
    root.mainloop()

