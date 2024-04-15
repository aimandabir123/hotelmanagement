from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import psycopg2
from tkinter import messagebox


class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1090x500+173+185")

        self.detf=Frame(self.root, bg="#1C86EE")
        self.detf.place(x=0, y=0, height=45, width=1250,)
        self.title2=Label(self.detf, text="ROOM DETAILS", font=("Bell MT", 26,"bold"),fg="Black", bg="#1C86EE").place(x=390,y=5)        

        self.Room_Number=StringVar()
        self.Floor=StringVar()
        self.Room_Type=StringVar()

        # down frame
        down_frame=LabelFrame(self.root, bd=2,relief=RIDGE, text="Show Room Details",font=("Times new roman", 12,'bold'),padx=2)
        down_frame.place(x=210, y=230,width=850, height=255)

        search_bar=Label(down_frame, text="******=================******================******", font=("Times new roman", 20,"bold"),bg="#1C86EE", fg="black")
        search_bar.place(x=5,y=5,height=30, width=840)

        down_frame2=LabelFrame(down_frame, bd=2,relief=RIDGE)
        down_frame2.place(x=4, y=30,width=840, height=185)

        scroll_y=ttk.Scrollbar(down_frame2,orient=VERTICAL)

        self.c_detail=ttk.Treeview(down_frame2,column=("Room_Number","floor","RoomType"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.c_detail.yview)

        self.c_detail.heading("Room_Number",text="Room Number")
        self.c_detail.heading("floor",text="Floor")
        self.c_detail.heading("RoomType",text="Room Type")
        

        self.c_detail["show"]="headings"

        self.c_detail.column("Room_Number",width=100)
        self.c_detail.column("floor",width=100)
        self.c_detail.column("RoomType",width=100)
        
        self.c_detail.pack(fill=BOTH,expand=1)
        self.c_detail.bind("<ButtonRelease-1>",self.get_cursor)
        self.display_data()

        img11= Image.open('home.jpg')
        img11= img11.resize((180,140))
        self.photoimg12= ImageTk.PhotoImage(img11)
        
        lbel1=Label(self.root, image=self.photoimg12, bd=0,relief=RIDGE)
        lbel1.place(x=10, y= 55)

        img12= Image.open('slides.jpg')
        img12= img12.resize((180,140))
        self.photoimg13= ImageTk.PhotoImage(img12)
        
        lbel2=Label(self.root, image=self.photoimg13, bd=0,relief=RIDGE)
        lbel2.place(x=10, y= 205)

        img13= Image.open('slide2.jpg')
        img13= img13.resize((180,130))
        self.photoimg14= ImageTk.PhotoImage(img13)
        
        lbel3=Label(self.root, image=self.photoimg14, bd=0,relief=RIDGE)
        lbel3.place(x=10, y= 360)

        #up frame
        up_frame=LabelFrame(self.root, bd=2,relief=RIDGE, font=("Times new roman", 12,'bold'),padx=2)
        up_frame.place(x=210, y=50,width=600, height=170)

        #details
        lbl_11=Label(up_frame, text="Room Number:", font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_11.grid(row=0, column=0, sticky=W)
        ent11=ttk.Entry(up_frame,textvariable=self.Room_Number, width=25,font=("Times new roman", 11,"bold"))
        ent11.grid(row=0,column=1, sticky=W)

        lbl_12=Label(up_frame, text="Floor:",font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_12.place(x=0, y= 60)
        ent12=ttk.Entry(up_frame, width=25, textvariable=self.Floor, font=("Times new roman", 11,"bold"))
        ent12.place(x=110, y= 62)

        lbl_14=Label(up_frame, text="Room Type:",  font=("Times new roman", 11,"bold"),padx=2,pady=6)
        lbl_14.place(x=0, y= 120)
        gen11=ttk.Combobox(up_frame, textvariable=self.Room_Type, font=("Times new roman", 11,"bold"),width=23, state="readonly")
        gen11["value"]=("Single","Double","Suite")
        gen11.current(0)
        gen11.place(x=110, y=124)

        # button
        aadd_btn=Button(up_frame,text="Add",command=self.add_data_,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        aadd_btn.place(x=450, y= 5)
        aadd_btn1=Button(up_frame,text="Update", command=self.Update_data_,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        aadd_btn1.place(x=450, y= 45)
        aadd_btn2=Button(up_frame,text="Delete",command=self.delete_r, font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        aadd_btn2.place(x=450, y= 85)
        aadd_btn3=Button(up_frame,text="CLEAR", command=self._reset_,font=("Times new roman", 11,"bold"),fg="Black", bg="#1C86EE", width=8,height=1)
        aadd_btn3.place(x=450, y= 125)

        img1= Image.open('resort.jpg')
        img1= img1.resize((180,180))
        self.photoimg2= ImageTk.PhotoImage(img1)
        
        lbel=Label(self.root, image=self.photoimg2, bd=0,relief=RIDGE)
        lbel.place(x=880, y= 48)

    def add_data_(self):
        if self.Room_Number.get() == "" or self.Floor.get() == "":
            messagebox.showwarning("Warning", "Please enter all the Required Fields", parent=self.root)
        else:
            conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor = conn.cursor()
            try:
                my_cursor.execute("INSERT INTO public.\"roomdetailss\" VALUES (%s, %s, %s)", (
                    self.Room_Number.get(),
                    self.Floor.get(),
                    self.Room_Type.get()
                ))
                conn.commit()
                self.display_data()
                messagebox.showinfo("Success", "Room has been added successfully")
            except psycopg2.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error occurred: {e}", parent=self.root)
            finally:
                conn.close()

    # display data again in left frame

    def display_data(self):
        conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM public."roomdetailss"')  # Remove the extra space at the end of "roomdetailss"
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.c_detail.delete(*self.c_detail.get_children())
            for i in rows:
                self.c_detail.insert("", END, values=i)
            conn.commit()  # Move commit outside the loop
        conn.close()

    def get_cursor(self,event=""):
        c_row=self.c_detail.focus()
        content=self.c_detail.item(c_row)
        row=content["values"]

        self.Room_Number.set(row[0]),
        self.Floor.set(row[1]),
        self.Room_Type.set(row[2]),


    # delete
    def delete_r(self):
        delete_r = messagebox.askyesno("Hotel Management System", "Do you want to delete this Room", parent=self.root)

        if delete_r:
            conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor = conn.cursor()
            query = "DELETE FROM public.\"roomdetailss\" WHERE \"roomdetailss\".\"Room_Number\" = %s"  # Corrected column name to "room_number"
            value = (self.Room_Number.get(),)
            try:
                my_cursor.execute(query, value)
                conn.commit()
                self.display_data()
                messagebox.showinfo("Success", "Room deleted successfully")
            except psycopg2.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error occurred: {e}", parent=self.root)
            finally:
                conn.close()

    # Update
    def Update_data_(self):
        if self.Room_Type.get() == "" or self.Floor.get() == "":
            messagebox.showerror("ERROR", "Please fill all the required fields!!", parent=self.root)
        else:
            conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
            my_cursor = conn.cursor()
            try:
                my_cursor.execute(
                    "UPDATE public.\"roomdetailss\" SET \"Floor\" = %s, \"Room_Type\" = %s WHERE \"Room_Number\" = %s",
                    (
                        self.Floor.get(),
                        self.Room_Type.get(),
                        self.Room_Number.get()
                    ))
                conn.commit()
                self.display_data()
                messagebox.showinfo("Success", "Data updated successfully")
            except psycopg2.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error occurred: {e}", parent=self.root)
            finally:
                conn.close()

    # clear
    def _reset_(self):
        self.Room_Number.set(""),
        self.Room_Type.set(""),
        self.Floor.set("")


if __name__== "__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()