from tkinter import *
import psycopg2
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

class ReportPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback Page")
        self.root.geometry("1090x500+173+185")
        self.s_images = Image.open('report.jpg')
        self.sized_image= self.s_images.resize((1500,800))
        new_image= ImageTk.PhotoImage(self.sized_image)
        photo= ImageTk.PhotoImage(self.sized_image)
        self.sized_image=Label(root,image=photo)
        self.sized_image.image=photo
        self.sized_image.place(x=0, y=0)


        self.name=StringVar()
        self.email=StringVar()
        self.mobile=StringVar()
        self.report1=StringVar()

        self.cust=Frame(self.root, bg="#1C86EE")
        self.cust.place(x=0, y=0, height=45, width=1250,)
        self.title2=Label(self.cust, text="REPORT", font=("Bell MT", 26,"bold"),fg="Black", bg="#1C86EE").place(x=450,y=5)


        self.name_label = Label(self.root, text="Name:", font=("Times New Roman", 20,"bold"))
        self.name_label.place(x=20, y=60)
        self.name_entry = Entry(self.root,textvariable=self.name,font=("Arial", 15))
        self.name_entry.place(x=120, y=65,width=180, height=30)

        self.email_label = Label(self.root, text="Email:", font=("Times New Roman", 20,"bold"))
        self.email_label.place(x=350, y=60)
        self.email_entry = Entry(self.root,textvariable=self.email,font=("Arial", 15))
        self.email_entry.place(x=450, y=65,width=180, height=30)

        self.contact_label = Label(self.root, text="Mobile no:", font=("Times New Roman", 20,"bold"))
        self.contact_label.place(x=680, y=60)
        self.contact_entry = Entry(self.root,textvariable=self.mobile,font=("Arial", 15))
        self.contact_entry.place(x=830, y=65,width=180, height=30)

        self.report_label = Label(self.root, text="REPORT:", font=("Times New Roman", 20, "bold"))
        self.report_label.place(x=20, y=150)
        self.report = Entry(self.root, textvariable=self.report1,font=("Arial", 15))
        self.report.place(x=20, y=200,height=150, width=800)

        self.submit_button = Button(self.root, text="Submit", bg="#1C86EE",font=("Times new roman", 20, "bold") ,command=self.submit_report)
        self.submit_button.place(x=500, y=400, width=100, height=35)

    def submit_report(self):
        if self.name.get()=="" and self.report1.get()=="" and self.mobile.get()=="":
            messagebox.showwarning("Warning", "Please anter all the Required Fields",parent=self.root)
        else:

            conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into report1 values(%s,%s,%s,%s)",(
                                                                                    self.name.get(),
                                                                                    self.email.get(),
                                                                                    self.mobile.get(),
                                                                                    self.report1.get(),
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Report Submitted", "Your Report has been submitted, {}!".format(self.name))
            self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, END)
        self.report.delete(0, END)
        self.email_entry.delete(0, END)
        self.contact_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    feedback_page = ReportPage(root)
    root.mainloop()
