from tkinter import *
from PIL import ImageTk, Image
from time import strftime
from customer import Customer_w
from room import roombooking
from details import Details
from report import ReportPage


class hotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Resort Management System")
        self.root.geometry("1550x800+0+0")
        self.s_images = Image.open('report.jpg')
        self.sized_image = self.s_images.resize((1265, 690))
        new_image = ImageTk.PhotoImage(self.sized_image)
        photo = ImageTk.PhotoImage(self.sized_image)
        self.sized_image = Label(root, image=photo)
        self.sized_image.image = photo
        self.sized_image.place(x=5, y=5)

        # frame
        self.hotel = Frame(self.root, bg="#87CEFA")
        self.hotel.place(x=15, y=15, height=40, width=1250, )
        self.hotel2 = Frame(self.root, bg="white")
        self.hotel2.place(x=15, y=60, height=40, width=500, )
        self.title1 = Label(self.hotel2, text="RESORT MANAGEMENT SYSTEM", font=("Bell MT", 20, "bold"), fg="Black",
                            bg="white").place(x=15, y=3)
        self.hotel3 = Frame(self.root, bg="#87CEFA")
        self.hotel3.place(x=15, y=110, height=40, width=250, )

        # buttons
        self.home_bt1 = Button(self.hotel, text="HOME", cursor="hand2", bg="#87CEFA", fg="black", bd=0,
                               font=("Times New Roman", 12, 'bold')).place(x=10, y=5)
        self.hom2_bt2 = Button(self.hotel, text="CUSTOMER", command=self.customer_detail, cursor="hand2", bg="#87CEFA",
                               fg="black", bd=0, font=("Times New Roman", 12, 'bold')).place(x=80, y=5)
        self.home_bt3 = Button(self.hotel, text="BOOKING", command=self.room_booking, cursor="hand2", bg="#87CEFA",
                               fg="black", bd=0, font=("Times New Roman", 12, 'bold')).place(x=190, y=5)
        self.home_bt4 = Button(self.hotel, text="DETAILS", command=self.detail_, cursor="hand2", bg="#87CEFA",
                               fg="black", bd=0, font=("Times New Roman", 12, 'bold')).place(x=290, y=5)
        self.home_bt4 = Button(self.hotel, text="REPORT", command=self.report_, cursor="hand2", bg="#87CEFA",
                               fg="black", bd=0, font=("Times New Roman", 12, 'bold')).place(x=390, y=5)
        self.home_bt5 = Button(self.hotel, text="LOGOUT", command=self.logout, cursor="hand2", bg="#87CEFA",
                               fg="#CD2626", bd=0, font=("Times New Roman", 12, 'bold')).place(x=1150, y=5)

        # images
        self.img1 = Image.open('resort.jpg')
        self.r1 = self.img1.resize((160, 160))
        new_image = ImageTk.PhotoImage(self.r1)
        photo = ImageTk.PhotoImage(self.r1)
        self.r1 = Label(root, image=photo, bg="black")
        self.r1.image = photo
        self.r1.place(x=10, y=170)

        self.img2 = Image.open('home.jpg')
        self.r2 = self.img2.resize((160, 160))
        new_image = ImageTk.PhotoImage(self.r2)
        photo = ImageTk.PhotoImage(self.r2)
        self.r2 = Label(root, image=photo, bg="white")
        self.r2.image = photo
        self.r2.place(x=10, y=345)

        self.img3 = Image.open('resort2.jpg')
        self.r3 = self.img3.resize((160, 160))
        new_image = ImageTk.PhotoImage(self.r3)
        photo = ImageTk.PhotoImage(self.r3)
        self.r3 = Label(root, image=photo, bg="black")
        self.r3.image = photo
        self.r3.place(x=10, y=520)

        self.img4 = Image.open('slides.jpg')
        self.r4 = self.img4.resize((180, 160))
        new_image = ImageTk.PhotoImage(self.r4)
        photo = ImageTk.PhotoImage(self.r4)
        self.r4 = Label(root, image=photo, bg="white")
        self.r4.image = photo
        self.r4.place(x=180, y=520)

        self.img5 = Image.open('slide2.jpg')
        self.r5 = self.img5.resize((180, 160))
        new_image = ImageTk.PhotoImage(self.r5)
        photo = ImageTk.PhotoImage(self.r5)
        self.r5 = Label(root, image=photo, bg="black")
        self.r5.image = photo
        self.r5.place(x=370, y=520)

        self.img6 = Image.open('resort3.jpg')
        self.r6 = self.img6.resize((180, 160))
        new_image = ImageTk.PhotoImage(self.r6)
        photo = ImageTk.PhotoImage(self.r6)
        self.r6 = Label(root, image=photo, bg="black")
        self.r6.image = photo
        self.r6.place(x=180, y=345)

        # clock
        self.label = Label(self.hotel3, font=('Times new roman', 20, 'bold'), background='#87CEFA', foreground='black')
        self.label.place(x=10, y=3)
        self.update_time()

    def update_time(self):
        string_time = strftime('%H:%M:%S %p')
        self.label.config(text=string_time)
        self.label.after(1000, self.update_time)  # Update every 1000 milliseconds (1 second)

    def customer_detail(self):
        self.new_window = Toplevel(self.root)
        self.hms = Customer_w(self.new_window)

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.hms = roombooking(self.new_window)

    def detail_(self):
        self.new_window = Toplevel(self.root)
        self.hms = Details(self.new_window)

    def report_(self):
        self.new_window = Toplevel(self.root)
        self.hms = ReportPage(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    Obj = hotelManagement(root)
    root.mainloop()
