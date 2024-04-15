from tkinter import*
from tkinter import ttk
import psycopg2
from datetime import datetime
from tkinter import messagebox

class Register:
     def __init__(self,root):
          self.root=root
          self.root.title("Register")
          self.root.geometry("400x500+440+120")

          self.username=StringVar()
          self.email=StringVar()
          self.spass=StringVar()
          self.cpass=StringVar()

          frame=Frame(self.root,bg="white") 
          frame.place(x=0,y=0,width=400,height=550) 

          register_lb1=Label(frame,text="REGISTER HERE",font=("Calibri",25,"bold"),fg="White",bg="Indigo")
          register_lb1.place(x=10,y=20,width=380)

          phone=Label(frame,text="Username:",font=("Calibri",15,),fg="indigo",bg="White")
          phone.place(x=10,y=100)
          phone=ttk.Entry(frame,textvariable=self.username,font=("Calibri",15))
          phone.place(x=10,y=130,width=250)

          mail=Label(frame,text="Email Address:",font=("Calibri",15,),fg="indigo",bg="White")
          mail.place(x=10,y=170)
          mail=ttk.Entry(frame,textvariable=self.email,font=("Calibri",15))
          mail.place(x=10,y=200,width=280)

          spass=Label(frame,text="Set Your Password:",font=("Calibri",15,),fg="indigo",bg="White")
          spass.place(x=10,y=240)
          spass=ttk.Entry(frame,textvariable=self.spass,font=("Calibri",15))
          spass.place(x=10,y=270,width=250)

          cpass=Label(frame,text="Confirm Password:",font=("Calibri",15,),fg="indigo",bg="White")
          cpass.place(x=10,y=315)
          cpass=ttk.Entry(frame,textvariable=self.cpass,font=("Calibri",15))
          cpass.place(x=10,y=350,width=250)

          login_btn=Button(frame,text="Submit",command=self.add_data_,font=("Calibri",20,"bold"),bd=3,relief=RIDGE,fg="WHITE",bg="Green",activeforeground ="white",activebackground="black")
          login_btn.place(x=120,y=450,width=160,height=45)

          checkbtn=Checkbutton(frame,text="I Agree to the terms and Conditions",font=("times new roman",15),bg="white",fg="indigo")
          checkbtn.place(x=10,y=400)


     def add_data_(self):
          if  self.username.get()=="" or self.email.get()=="" or self.spass.get()=="" or self.cpass.get()=="":
               messagebox.showerror("Error","all fields required")
          else:
        
               conn=psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into register values(%s,%s,%s)",(
                                                                                       self.username.get(),
                                                                                       self.email.get(),
                                                                                       self.spass.get()
                                                                                       ))
               
               conn.commit()
               messagebox.showinfo("Success","Registeration Successful ",parent=self.root) 
               conn.close()



     

                    
            







if __name__ == "__main__":
     root=Tk()
     app=Register(root)
     root.mainloop()           