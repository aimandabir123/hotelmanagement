from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import psycopg2
from time import strftime
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from payment import PaymentPage
from availableroom import AvailableRoomPage


class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Resort Management System")
        self.root.geometry("1090x500+173+185")
        
        self.total_cost_var = StringVar()
        self.total_cost_var.set("0.00") 

        self.cust=Frame(self.root, bg="#1C86EE")
        self.cust.place(x=0, y=0, height=45, width=1250,)
        self.title2=Label(self.cust, text="CUSTOMER ROOM BOOKING ", font=("Bell MT", 26,"bold"),fg="Black", bg="#1C86EE").place(x=390,y=5)        

        left_frame=LabelFrame(self.root, bd=2,relief=RIDGE, text="Booking details",font=("Times new roman", 12,'bold'),padx=2)
        left_frame.place(x=5, y=45,width=380, height=450)

        self.Contact=StringVar()
        self.checkin=StringVar()
        self.checkout=StringVar()
        self.roomtype=StringVar()
        self.availableroom=StringVar()
        self.mealtype=StringVar()
        self.noofdays=StringVar()
        self.totaltax=StringVar()
        self.actualcost=StringVar()
        self.totalcost=StringVar()

        #details
        lbl_1=Label(left_frame, text="Customer Contact:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_1.grid(row=0, column=0, sticky=W)
        ent1=ttk.Entry(left_frame, width=18, textvariable=self.Contact,font=("Times new roman", 11,"bold"))
        ent1.grid(row=0,column=1, sticky=W)

        fetch_btn=Button(left_frame,text="FETCH",command=self.fetch_contact,font=("Times new roman", 8,"bold"),fg="Black", bg="#1C86EE", width=6,height=1)
        fetch_btn.place(x=290, y=6)

        lbl_2=Label(left_frame, text="Check in:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_2.grid(row=1, column=0, sticky=W)
        ent2=ttk.Entry(left_frame, width=26, textvariable=self.checkin, font=("Times new roman", 11,"bold"))
        ent2.grid(row=1,column=1)

        lbl_3=Label(left_frame, text="Check out:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_3.grid(row=2, column=0, sticky=W)
        ent3=ttk.Entry(left_frame, width=26, textvariable=self.checkout, font=("Times new roman", 11,"bold"))
        ent3.grid(row=2,column=1)

        lbl_4=Label(left_frame, text="Room Type:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_4.grid(row=3, column=0,sticky=W)
        gen1=ttk.Combobox(left_frame,textvariable=self.roomtype, font=("Times new roman", 11,"bold"),width=24, state="readonly")
        gen1["value"]=("Single","Double", "Suite")
        gen1.current(0)
        gen1.grid(row=3,column=1)

        lbl_5=Button(left_frame, text="Available Room:",command=self.avail_,fg="Black", bg="#1C86EE",font=("Times new roman", 11,"bold"),padx=2,pady=4)
        lbl_5.grid(row=4, column=0, sticky=W)
        ent5=ttk.Entry(left_frame, width=26,textvariable=self.availableroom,font=("Times new roman", 11,"bold"))
        ent5.grid(row=4,column=1)

        lbl_6=Label(left_frame, text="No of Days:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_6.grid(row=6, column=0, sticky=W)
        ent6=ttk.Entry(left_frame, width=26,textvariable=self.noofdays,font=("Times new roman", 11,"bold"))
        ent6.grid(row=6,column=1)

        lbl_7=Label(left_frame, text="Total Tax:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_7.grid(row=7, column=0, sticky=W)
        ent7=ttk.Entry(left_frame, width=26, textvariable=self.totaltax,font=("Times new roman", 11,"bold"))
        ent7.grid(row=7,column=1)

        lbl_8=Label(left_frame, text="Meal Type:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_8.grid(row=5, column=0, sticky=W)
        gen2=ttk.Combobox(left_frame,textvariable=self.mealtype, font=("Times new roman", 11,"bold"),width=24, state="readonly")
        gen2["value"]=("Veg","Non-Veg")
        gen2.current(0)
        gen2.grid(row=5,column=1)
    
        lbl_10=Label(left_frame, text="Actual Cost:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_10.grid(row=8, column=0, sticky=W)
        ent10=ttk.Entry(left_frame, width=26, textvariable=self.actualcost, font=("Times new roman", 11,"bold"))
        ent10.grid(row=8,column=1)

        lbl_11=Label(left_frame, text="Total Cost:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_11.grid(row=9, column=0, sticky=W)
        ent11=ttk.Entry(left_frame, width=26,textvariable=self.totalcost, font=("Times new roman", 11,"bold"))
        ent11.grid(row=9,column=1)

        add_btn=Button(left_frame,text="Bill",command=self.total,font=("Times new roman", 12,"bold"),fg="Black", bg="#1C86EE", width=6,height=1)
        add_btn.place(x=5, y=350)
        

        bt_frame=Frame(left_frame, bd=2, relief=RIDGE)
        bt_frame.place(x=0,y=390,width=340,height=38)

        #buttons
        add_btn=Button(bt_frame,text="Book",command=self.add_data,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn.grid(row=0, column=0, padx=1)
        add_btn1=Button(bt_frame,text="Update",command=self.Update_data,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn1.grid(row=0, column=1, padx=1)
        add_btn2=Button(bt_frame,text="Delete",command=self.delete_r,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn2.grid(row=0, column=2, padx=1)
        add_btn3=Button(bt_frame,text="Reset",command=self.reset_,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn3.grid(row=0, column=3, padx=1)
        print_btn = Button(self.root, text="Print Bill", command=self.print_bill, font=("Times new roman", 11, "bold"), fg="Black", bg="#1C86EE", width=8, height=1)
        print_btn.place(x=265, y=415)
        payment = Button(self.root, text="Payment",command=self.payment, font=("Times new roman", 11, "bold"), fg="Black", bg="#1C86EE", width=8, height=1)
        payment.place(x=135, y=415)

        # right frame
        right_frame=LabelFrame(self.root, bd=2,relief=RIDGE, text="View and Search Details",font=("Times new roman", 12,'bold'),padx=2)
        right_frame.place(x=390, y=200,width=680, height=300)

        # search bar
        search_bar=Label(right_frame, text="*****===============*****==============*****", font=("Times new roman", 20,"bold"),bg="#1C86EE", fg="black")
        search_bar.place(x=5,y=5,height=30, width=660)

        right_frame2=LabelFrame(right_frame, bd=2,relief=RIDGE)
        right_frame2.place(x=4, y=40,width=665, height=240)

        scroll_x=ttk.Scrollbar(right_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame2,orient=VERTICAL)

        self.c_detail = ttk.Treeview(right_frame2, column=("Contact", "checkin", "checkout", "roomtype", "availableroom", "mealtype", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.c_detail.xview)
        scroll_y.config(command=self.c_detail.yview)

        self.c_detail.heading("Contact",text="Contact no")
        self.c_detail.heading("checkin",text="Check In")
        self.c_detail.heading("checkout",text="Check Out")
        self.c_detail.heading("roomtype",text="Room Type")
        self.c_detail.heading("availableroom",text="Availabe Room")
        self.c_detail.heading("mealtype",text="Meal type")
        self.c_detail.heading("noofdays",text="Total Days")
        

        self.c_detail["show"]="headings"

        self.c_detail.column("Contact",width=100)
        self.c_detail.column("checkin",width=100)
        self.c_detail.column("checkout",width=100)
        self.c_detail.column("roomtype",width=100)
        self.c_detail.column("availableroom",width=100)
        self.c_detail.column("mealtype",width=100)
        self.c_detail.column("noofdays",width=100)
        
        self.c_detail.pack(fill=BOTH,expand=1)
        self.c_detail.bind("<ButtonRelease-1>",self.get_cursor)
        self.display_data()

        img1= Image.open('home.jpg')
        img1= img1.resize((160,160))
        self.photoimg2= ImageTk.PhotoImage(img1)
        
        lbel=Label(self.root, image=self.photoimg2, bd=0,relief=RIDGE)
        lbel.place(x=910, y= 48)

    def fetch_contact(self):
        if self.Contact.get()=="":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:
            conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor=conn.cursor()
            query=("select \"Customer1\".\"Name\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
            value=(self.Contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                show_data=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                show_data.place(x=390, y=55, width=450, height=145 )

                lblname=Label(show_data, text="Name: ",font=("Times new roman", 11,"bold"))
                lblname.place(x=0,y=0)
                lbl1=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl1.place(x=50,y=0)

                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                query=("select \"Customer1\".\"Gender\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
                value=(self.Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgen=Label(show_data, text="Gender: ",font=("Times new roman", 11,"bold"))
                lblgen.place(x=0,y=50)
                lbl2=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl2.place(x=70,y=50)

                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                query=("select \"Customer1\".\"Email\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
                value=(self.Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblmail=Label(show_data, text="Email: ",font=("Times new roman", 11,"bold"))
                lblmail.place(x=0,y=100)
                lbl3=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl3.place(x=50,y=100)

                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                query=("select \"Customer1\".\"Ref\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
                value=(self.Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblc=Label(show_data, text="Ref No: ",font=("Times new roman", 11,"bold"))
                lblc.place(x=250,y=0)
                lbl4=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl4.place(x=310,y=0)

                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                query=("select \"Customer1\".\"Country\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
                value=(self.Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblco=Label(show_data, text="Country: ",font=("Times new roman", 11,"bold"))
                lblco.place(x=250,y=50)
                lbl5=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl5.place(x=310,y=50)

                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                query=("select \"Customer1\".\"Address\" from public.\"Customer1\" where \"Customer1\".\"Mobile\"=%s")
                value=(self.Contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblc=Label(show_data, text="Address: ",font=("Times new roman", 11,"bold"))
                lblc.place(x=250,y=100)
                lbl4=Label(show_data, text=row,font=("Times new roman", 11,"bold"))
                lbl4.place(x=310,y=100)

    # add detail
    def add_data(self):
        if self.Contact.get() == "" or self.checkin.get() == "":
            messagebox.showerror("ERROR", "Please fill all the required fields!!", parent=self.root)
        else:
            try:
                conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into public.\"booking12\" values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.Contact.get(),
                    self.checkin.get(),
                    self.checkout.get(),
                    self.roomtype.get(),
                    self.availableroom.get(),
                    self.mealtype.get(),
                    self.noofdays.get(),
                ))
                
                conn.commit()
                self.display_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("ERROR", f"Error adding data to database: {e}", parent=self.root)


    

    
    def display_data(self):
        try:
            if self.root.winfo_exists() and hasattr(self, 'c_detail') and self.c_detail.winfo_exists():
                self.c_detail.delete(*self.c_detail.get_children())
    
            conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from public.\"booking12\"")
            rows = my_cursor.fetchall()
    
            if len(rows) != 0:
                for i in rows:
                    self.c_detail.insert("", END, values=i)
    
            conn.commit()
            conn.close()
    
        except Exception as e:
            if self.root.winfo_exists():
                messagebox.showerror("ERROR", f"Error displaying data: {e}", parent=self.root)
    
                    
    # display data again in left frame
    def get_cursor(self,event=""):
        c_row=self.c_detail.focus()
        content=self.c_detail.item(c_row)
        row=content["values"]
        if row:
            self.Contact.set(row[0]),
            self.checkin.set(row[1]),
            self.checkout.set(row[2]),
            self.roomtype.set(row[3]),
            self.availableroom.set(row[4]),
            self.mealtype.set(row[5]),
            self.noofdays.set(row[6]),

    def Update_data(self):
        if self.Contact.get() == "" or self.checkin.get() == "":
            messagebox.showerror("ERROR", "Please fill all the required fields!!", parent=self.root)
        else:
            try:
                conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "update public.\"booking12\" set \"Contact\"=%s, \"check_in\"=%s, \"check_out\"=%s, \"room_type\"=%s, \"meal\"=%s, \"no_of_days\"=%s where booking12.\"available_room\"=%s ",
                    (
                        self.Contact.get(),
                        self.checkin.get(),
                        self.checkout.get(),
                        self.roomtype.get(),
                        self.mealtype.get(),
                        self.noofdays.get(),
                        self.availableroom.get()
                    ))
                conn.commit()
                self.display_data()  # Display data again after update
                conn.close()
                messagebox.showinfo("Update", "Details have been updated successfully ", parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Went Wrong:{str(e)}", parent=self.root)

    def delete_r(self):
        delete_r = messagebox.askyesno("Hotel Management System", "Do you want to delete this Booking detail",
                                       parent=self.root)
        if delete_r > 0:
            conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor = conn.cursor()
            query = "delete from public.\"booking12\" where available_room=%s"
            value = (self.availableroom.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_r:
                return
        conn.commit()
        self.display_data()  # Display data again after deletion
        conn.close()

    def reset_(self):
        self.Contact.set(""),
        self.checkin.set(""),
        self.checkout.set(""),
        self.availableroom.set(""),
        self.roomtype.set(""),
        self.mealtype.set(""),    
        self.noofdays.set(""),
        self.totaltax.set(""),
        self.actualcost.set(""),
        self.totalcost.set("")

    def print_bill(self):

        conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
        my_cursor = conn.cursor()
        query = "SELECT \"Ref\", \"Name\", \"Email\" FROM public.\"Customer1\" WHERE \"Customer1\".\"Mobile\"=%s"
        value = (self.Contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        if row:
            ref, name, email = row
        else:
            ref, name, email = "Details not found"
        


        # Customize this based on your data structure
        bill_data = f"BILL\n"\
                    f"{'-'*20}\n"\
                    f"Reference No: {ref}\n" \
                    f"Name: {name}\n" \
                    f"Email: {email}\n" \
                    f"Contact: {self.Contact.get()}\n" \
                    f"Check-in: {self.checkin.get()}\n" \
                    f"Check-out: {self.checkout.get()}\n" \
                    f"Room Type: {self.roomtype.get()}\n" \
                    f"Available Room: {self.availableroom.get()}\n" \
                    f"Meal Type: {self.mealtype.get()}\n" \
                    f"No of Days: {self.noofdays.get()}\n" \
                    f"Actual Cost: {self.actualcost.get()}\n" \
                    f"Total Tax: {self.totaltax.get()}\n" \
                    f"{'-'*20}\n"\
                    f"Total Cost: {self.totalcost.get()}\n"

        # Ask the user for the file location
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],parent=self.root)

        # Check if the user canceled the dialog
        if not file_path:
            return

        # Save the bill to the chosen file
        with open(file_path, 'a') as file:
            file.write(bill_data)

        # Inform the user about the saved file
        messagebox.showinfo("Success", "Bill Saved", parent=self.root)

    def payment(self):
        if self.totalcost.get()=="":
            messagebox.showerror("Error","Please click on Bill before doing payment", parent=self.root)
        else:
            self.total()
            total_cost = self.total_cost_var.get()
            payment_window = Toplevel(self.root)
            payment_page = PaymentPage(payment_window, total_cost)
            payment_window.mainloop()

    def total(self):
        indate=self.checkin.get()
        outdate=self.checkout.get()
        indate=datetime.strptime(indate, "%d/%m/%Y")
        outdate=datetime.strptime(outdate, "%d/%m/%Y")
        self.noofdays.set(abs(outdate-indate).days)

        if self.mealtype.get() == "Veg" and self.roomtype.get() == "Double":
            q1 = 500
            q2 = 1500
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + (q5 * 0.2))))

        if self.mealtype.get() == "Veg" and self.roomtype.get() == "Single":
            q1 = 500
            q2 = 1000
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + ( q5 * 0.2))))

        if self.mealtype.get() == "Veg" and self.roomtype.get() == "Suite":
            q1 = 500
            q2 = 2500
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + (q5 * 0.2))))

        if self.mealtype.get() == "Non-Veg" and self.roomtype.get() == "Double":
            q1 = 800
            q2 = 1500
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + (q5 * 0.2))))

        if self.mealtype.get() == "Non-Veg" and self.roomtype.get() == "Single":
            q1 = 800
            q2 = 1000
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + (q5 * 0.2))))

        if self.mealtype.get() == "Non-Veg" and self.roomtype.get() == "Suite":
            q1 = 900
            q2 = 2500
            q3 = float(self.noofdays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            Taxx = "Rs. {:.2f}".format(q5 * 0.2)
            subtax = "Rs. {:.2f}".format(q5)
            totaltax = "Rs. {:.2f}".format(q5 + (q5 * 0.2))

            self.totaltax.set(Taxx)
            self.actualcost.set(subtax)
            self.totalcost.set(totaltax)
            self.total_cost_var.set("{:.2f}".format(float(q5 + (q5 * 0.2))))

    def avail_(self):
        self.new_window=Toplevel(self.root)
        self.hms=AvailableRoomPage(self.new_window)








if __name__== "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()