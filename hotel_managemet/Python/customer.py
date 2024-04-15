from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import psycopg2
import random
from tkinter import messagebox


class Customer_w:
    def __init__(self,root):
        self.root=root
        self.root.title("Resort Management System")
        self.root.geometry("1090x500+173+185")

        self.ref1=StringVar()
        x=random.randint(1000,9999)
        self.ref1.set(str(x))

        self.c_name=StringVar()
        self.c_dob=StringVar()
        self.c_gender=StringVar()
        self.c_post=StringVar()
        self.c_mobile=StringVar()
        self.c_email=StringVar()
        self.c_country=StringVar()
        self.c_idproof=StringVar()
        self.c_idnumber=StringVar()
        self.c_address=StringVar()

        self.cust=Frame(self.root, bg="#1C86EE")
        self.cust.place(x=0, y=0, height=45, width=1250,)
        self.title2=Label(self.cust, text="ADD CUSTOMER DETAILS", font=("Bell MT", 26,"bold"),fg="Black", bg="#1C86EE").place(x=390,y=5)

        # frame
        left_frame=LabelFrame(self.root, bd=2,relief=RIDGE, text="Customer detail",font=("Times new roman", 12,'bold'),padx=2)
        left_frame.place(x=5, y=45,width=380, height=450)

        #details
        lbl_1=Label(left_frame, text="Customer Ref:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_1.grid(row=0, column=0, sticky=W)
        ent1=ttk.Entry(left_frame, width=26, textvariable=self.ref1,font=("Times new roman", 11,"bold"),state="readonly")
        ent1.grid(row=0,column=1)

        lbl_2=Label(left_frame, text="Customer Name:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_2.grid(row=1, column=0, sticky=W)
        ent2=ttk.Entry(left_frame, width=26, textvariable=self.c_name, font=("Times new roman", 11,"bold"))
        ent2.grid(row=1,column=1)

        lbl_3=Label(left_frame, text="Customer DOB:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_3.grid(row=2, column=0, sticky=W)
        ent3=ttk.Entry(left_frame, width=26, textvariable=self.c_dob,font=("Times new roman", 11,"bold"))
        ent3.grid(row=2,column=1)

        lbl_4=Label(left_frame, text="Gender:",  font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_4.grid(row=3, column=0,sticky=W)
        gen1=ttk.Combobox(left_frame,textvariable=self.c_gender, font=("Times new roman", 11,"bold"),width=24, state="readonly")
        gen1["value"]=("Male","Female","Others")
        gen1.current(0)
        gen1.grid(row=3,column=1)

        lbl_5=Label(left_frame, text="Postcode:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_5.grid(row=4, column=0, sticky=W)
        ent5=ttk.Entry(left_frame, width=26,  textvariable=self.c_post,font=("Times new roman", 11,"bold"))
        ent5.grid(row=4,column=1)

        lbl_6=Label(left_frame, text="Mobile no:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_6.grid(row=5, column=0, sticky=W)
        ent6=ttk.Entry(left_frame, width=26, textvariable=self.c_mobile,font=("Times new roman", 11,"bold"))
        ent6.grid(row=5,column=1)

        lbl_7=Label(left_frame, text="Email:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_7.grid(row=6, column=0, sticky=W)
        ent7=ttk.Entry(left_frame, width=26,textvariable=self.c_email, font=("Times new roman", 11,"bold"))
        ent7.grid(row=6,column=1)

        lbl_8=Label(left_frame, text="Country:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_8.grid(row=7, column=0, sticky=W)
        gen2=ttk.Combobox(left_frame,textvariable=self.c_country, font=("Times new roman", 11,"bold"),width=24, state="readonly")
        gen2["value"]=("India","UK","USA","France","Russia","Germany","Sri lanka","Pakistan","Afghanistan","Nepal")
        gen2.current(0)
        gen2.grid(row=7,column=1)

        lbl_9=Label(left_frame,text="ID Proof:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_9.grid(row=8, column=0, sticky=W)
        gen3=ttk.Combobox(left_frame, textvariable=self.c_idproof, font=("Times new roman", 11,"bold"),width=24, state="readonly")
        gen3["value"]=("Passport","Aadhaar Card","Pan Card","Driving Lisence","Voter ID","Bank Account","Post Office ID")
        gen3.current(0)
        gen3.grid(row=8,column=1)

        lbl_10=Label(left_frame, text="ID Number:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_10.grid(row=9, column=0, sticky=W)
        ent10=ttk.Entry(left_frame, width=26,  textvariable=self.c_idnumber,font=("Times new roman", 11,"bold"))
        ent10.grid(row=9,column=1)

        lbl_11=Label(left_frame, text="Address:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_11.grid(row=10, column=0, sticky=W)
        ent11=ttk.Entry(left_frame, width=26, textvariable=self.c_address,font=("Times new roman", 11,"bold"))
        ent11.grid(row=10,column=1)

        bt_frame=Frame(left_frame, bd=2, relief=RIDGE)
        bt_frame.place(x=0,y=370,width=340,height=38)

        #buttons
        add_btn=Button(bt_frame,text="Add",command=self.add_data,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn.grid(row=0, column=0, padx=1)
        add_btn1=Button(bt_frame,text="Update",command=self.update,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn1.grid(row=0, column=1, padx=1)
        add_btn2=Button(bt_frame,text="Delete",command=self.delete_r,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn2.grid(row=0, column=2, padx=1)
        add_btn3=Button(bt_frame,text="Reset",command=self.reset_,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        add_btn3.grid(row=0, column=3, padx=1)

        # frame
        right_frame=LabelFrame(self.root, bd=2,relief=RIDGE, text="View and Search Details",font=("Times new roman", 12,'bold'),padx=2)
        right_frame.place(x=390, y=45,width=680, height=450)

        # search bar
        # search_bar=Label(right_frame, text="Search By:", font=("Times new roman", 11,"bold"),bg="#1C86EE", fg="black")
        # search_bar.grid(row=0, column=0, sticky=W)
# 
        # self.search_var=StringVar()
        # s_box=ttk.Combobox(right_frame, textvariable=self.search_var,font=("Times new roman", 11,"bold"),width=15, state="readonly")
        # s_box["value"]=("Ref Number","Mobile no")
        # s_box.current(0)
        # s_box.grid(row=0,column=1,padx=2)
# 
        # self.txt_search=StringVar()
        # t_search=ttk.Entry(right_frame,textvariable=self.txt_search, width=24, font=("Times new roman", 12,"bold"))
        # t_search.grid(row=0,column=2,padx=2)

        # add_btn4=Button(right_frame,text="Search",font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8)
        # add_btn4.grid(row=0, column=3, padx=1)
        # add_btn5=Button(right_frame,text="Show All",command=self.display_data,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8)
        # add_btn5.grid(row=0, column=4, padx=1)

        # Show Table
        right_frame2=LabelFrame(right_frame, bd=2,relief=RIDGE)
        right_frame2.place(x=4, y=40,width=665, height=300)

        scroll_x=ttk.Scrollbar(right_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame2,orient=VERTICAL)

        self.c_detail=ttk.Treeview(right_frame2,column=("Ref","Name","DOB","Gender","Post","Mobile","Email","Country","Id Proof","Id Number","Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.c_detail.xview)
        scroll_y.config(command=self.c_detail.yview)

        self.c_detail.heading("Ref",text="Ref No")
        self.c_detail.heading("Name",text="Name")
        self.c_detail.heading("DOB",text="DOB")
        self.c_detail.heading("Gender",text="Gender")
        self.c_detail.heading("Post",text="Postcode")
        self.c_detail.heading("Mobile",text="Mobile No")
        self.c_detail.heading("Email",text="Email")
        self.c_detail.heading("Country",text="Country")
        self.c_detail.heading("Id Proof",text="ID Proof")
        self.c_detail.heading("Id Number",text="ID No")
        self.c_detail.heading("Address",text="Address")

        self.c_detail["show"]="headings"

        self.c_detail.column("Ref",width=100)
        self.c_detail.column("Name",width=100)
        self.c_detail.column("DOB",width=100)
        self.c_detail.column("Gender",width=100)
        self.c_detail.column("Post",width=100)
        self.c_detail.column("Mobile",width=100)
        self.c_detail.column("Email",width=100)
        self.c_detail.column("Country",width=100)
        self.c_detail.column("Id Proof",width=100)
        self.c_detail.column("Id Number",width=100)
        self.c_detail.column("Address",width=100)

        self.c_detail.pack(fill=BOTH,expand=1)
        self.c_detail.bind("<ButtonRelease-1>",self.get_cursor)
        self.display_data()

    def add_data(self):
        if self.c_mobile.get()=="" or self.c_dob.get()=="":
            messagebox.showerror("ERROR","Please fill all the required fields!!",parent=self.root)
        else:
            try:
                conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                my_cursor=conn.cursor()
                my_cursor.execute("""
                    INSERT INTO "public"."Customer1"
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                                  (
                                      self.ref1.get(),
                                      self.c_name.get(),
                                      self.c_dob.get(),
                                      self.c_gender.get(),
                                      self.c_post.get(),
                                      self.c_mobile.get(),
                                      self.c_email.get(),
                                      self.c_country.get(),
                                      self.c_idproof.get(),
                                      self.c_idnumber.get(),
                                      self.c_address.get()
                                  )
                                  )

                conn.commit()
                self.display_data()
                conn.close()
            except Exception as e:
                messagebox.showwarning("Warning", f"Went Wrong:{str(e)}",parent=self.root)   
    # display data in right frame
    def display_data(self):
        conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
        my_cursor=conn.cursor()
        my_cursor.execute('SELECT * FROM "public"."Customer1"')
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.c_detail.delete(*self.c_detail.get_children())
            for i in rows:
                self.c_detail.insert("", END,values=i)
                conn.commit()
            conn.close()

                    
    # display data again in left frame
    def get_cursor(self,event=""):
        c_row=self.c_detail.focus()
        content=self.c_detail.item(c_row)
        row=content["values"]

        self.ref1.set(row[0]),
        self.c_name.set(row[1]),
        self.c_dob.set(row[2]),
        self.c_gender.set(row[3]),
        self.c_post.set(row[4]),
        self.c_mobile.set(row[5]),
        self.c_email.set(row[6]),
        self.c_country.set(row[7]),
        self.c_idproof.set(row[8]),
        self.c_idnumber.set(row[9]),    
        self.c_address.set(row[10])

    def update(self):
        if self.c_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor=conn.cursor()
            my_cursor.execute("""
                UPDATE "public"."Customer1"
                SET "Name"=%s, "DOB"=%s, "Gender"=%s, "Postcode"=%s, "Mobile"=%s, "Email"=%s, "Country"=%s, "Id_Proof"=%s, "Id_Number"=%s, "Address"=%s
                WHERE "Customer1"."Ref" = %s
                """,
                              (
                                  self.c_name.get(),
                                  self.c_dob.get(),
                                  self.c_gender.get(),
                                  self.c_post.get(),
                                  self.c_mobile.get(),
                                  self.c_email.get(),
                                  self.c_country.get(),
                                  self.c_idproof.get(),
                                  self.c_idnumber.get(),
                                  self.c_address.get(),
                                  self.ref1.get()
                              )
                              )

            conn.commit()
            self.display_data()
            conn.close()
            messagebox.showinfo("Update","Details have been successfully Updated",parent=self.root) 


    def delete_r(self):
        delete_r=messagebox.askyesno("Resort Management System", "Do you want to delete this Customer Record",parent=self.root)
        if delete_r>0:
            conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor=conn.cursor()
            query = 'DELETE FROM public."Customer1" WHERE "Customer1"."Ref" = %s'

            value=(self.ref1.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_r:
                return
        
        conn.commit()
        self.display_data()
        conn.close()

    def reset_(self):
        # self.ref1.set(""),
        self.c_name.set(""),
        self.c_dob.set(""),
        # self.c_gender.set(""),
        self.c_post.set(""),
        self.c_mobile.set(""),
        self.c_email.set(""),
        # self.c_country.set(""),
        # self.c_idproof.set(""),
        self.c_idnumber.set(""),    
        self.c_address.set("")
        x=random.randint(1000,9999)
        self.ref1.set(str(x))



            




if __name__== "__main__":
    root=Tk()
    obj=Customer_w(root)
    root.mainloop()