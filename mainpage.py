from tkinter import *
from PIL import Image, ImageTk
from customer import Customer_Window
from room import Room_Window
from details import detailsRoom
from employee import Employee_Window
from restaurant import Restaurant_Window
from amenities import Amenities_Window
from About import About_Window
import sys

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("1550x800+0+0")

        # Header Images
        img1 = Image.open("pic9.jfif")
        img1 = img1.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl1.place(x=230, y=0, width=210, height=140)

        img1b = Image.open("pic6.png")
        img1b = img1b.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1b = ImageTk.PhotoImage(img1b)
        lbl1b = Label(self.root, image=self.photoimg1b, bd=4, relief=RIDGE)
        lbl1b.place(x=440, y=0, width=210, height=140)

        img1c = Image.open("pic10.jfif")
        img1c = img1c.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1c = ImageTk.PhotoImage(img1c)
        lbl1c = Label(self.root, image=self.photoimg1c, bd=4, relief=RIDGE)
        lbl1c.place(x=650, y=0, width=210, height=140)

        img1d = Image.open("pic11.jfif")
        img1d = img1d.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1d = ImageTk.PhotoImage(img1d)
        lbl1d = Label(self.root, image=self.photoimg1d, bd=4, relief=RIDGE)
        lbl1d.place(x=860, y=0, width=210, height=140)

        img1e = Image.open("pic12.jfif")
        img1e = img1e.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1e = ImageTk.PhotoImage(img1e)
        lbl1e = Label(self.root, image=self.photoimg1e, bd=4, relief=RIDGE)
        lbl1e.place(x=1070, y=0, width=210, height=140)

        img1f = Image.open("pic20.jpg")
        img1f = img1f.resize((210, 140), Image.ANTIALIAS)
        self.photoimg1f = ImageTk.PhotoImage(img1f)
        lbl1f = Label(self.root, image=self.photoimg1f, bd=4, relief=RIDGE)
        lbl1f.place(x=1280, y=0, width=210, height=140)

        # Logo
        img2 = Image.open("pic7.jfif")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl2.place(x=0, y=0, width=230, height=140)

        # Title
        lbl3 = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl3.place(x=0, y=140, width=1550, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # Menu
        lbl4 = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl4.place(x=0, y=0, width=230)

        # Menu Frame
        menu_frame = Frame(main_frame, bd=4, relief=RIDGE)
        menu_frame.place(x=0, y=35, width=230, height=335)

        customer_btn = Button(menu_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black",
                     fg="gold", bd=0, cursor="hand1")
        customer_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(menu_frame, text="ROOM",command=self.Room_details, width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(menu_frame, text="ROOM DETAILS", command=self.details, width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        employee_btn = Button(menu_frame, text="EMPLOYEE",command=self.Employee, width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        employee_btn.grid(row=3, column=0, pady=1)

        restaurant_btn = Button(menu_frame, text= "RESTAURANT",command=self.Restaurant, width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        restaurant_btn.grid(row=4, column=0, pady=1)

        amenities_btn = Button(menu_frame, text= "AMENITIES",command=self.Amenities,width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        amenities_btn.grid(row=5, column=0, pady=1)

        About_btn = Button(menu_frame, text= "FEEDBACK",width=22,command=self.About, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        About_btn.grid(row=6, column=0, pady=1)

        logout_btn = Button(menu_frame, text="LOGOUT",command=self.Logout, width=22, font=("times new roman", 14, "bold"), bg="black",
                              fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=7, column=0, pady=1)

        # Centre Image
        img3 = Image.open("pic3.png")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl5 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl5.place(x=230, y=0, width=1310, height=590)

        # Side Images
        img4 = Image.open("pic2.png")
        img4 = img4.resize((230, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl6 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl6.place(x=0, y=340, width=230, height=130)

        img5 = Image.open("pic4.jfif")
        img5 = img5.resize((230, 130), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl7 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbl7.place(x=0, y=470, width=230, height=130)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)
    
    def Room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Window(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = detailsRoom(self.new_window)

    def Employee(self):
        self.new_window = Toplevel(self.root)
        self.app = Employee_Window(self.new_window)

    def Restaurant(self):
        self.new_window = Toplevel(self.root)
        self.app = Restaurant_Window(self.new_window)

    def Amenities(self):
        self.new_window = Toplevel(self.root)
        self.app = Amenities_Window(self.new_window)

    def About(self):
        self.new_window = Toplevel(self.root)
        self.app = About_Window(self.new_window)
    
    def Logout(self):
        sys.exit(0)

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

