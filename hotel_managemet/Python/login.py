from tkinter import*
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from hotel import hotelManagement
from Registerpage import Register
from forgotpass import ForgotPassword
import psycopg2


class Login:
        def __init__(self,root):
                self.root=root
                self.root.title("Login Page")
                self.root.geometry("15500x800+0+0")
                self.s_images = Image.open('resort2.jpg')
                self.sized_image= self.s_images.resize((1500,800))
                new_image= ImageTk.PhotoImage(self.sized_image)
                photo= ImageTk.PhotoImage(self.sized_image)
                self.sized_image=Label(root,image=photo)
                self.sized_image.image=photo
                self.sized_image.place(x=0,y=0)

                self.username = StringVar()
                self.password = StringVar()

                # login frame
                self.f_loginn=Frame(self.root, bg="#87CEFF")
                self.f_loginn.place(x=845, y=75, height=560, width=410,)
                self.f_login=Frame(self.root, bg="#EEE9E9")
                self.f_login.place(x=850, y=80, height=550, width=400,)

                title=Label(self.f_login, text="Login Here", font=("Bell MT", 30,"bold"),fg="Black", bg="#EEE9E9").place(x=90,y=40)
                self.s_img= Image.open('profile.png')
                self.resized_image= self.s_img.resize((70,70))
                new_image= ImageTk.PhotoImage(self.resized_image)
                photo= ImageTk.PhotoImage(self.resized_image)
                self.resized_image=Label(self.f_login,image=photo, bg="#EEE9E9")
                self.resized_image.image=photo
                self.resized_image.place(x=10,y=30)
                # Username Frame
                username=Label(self.f_login, text="Username", font=("Times New Roman", 15, "bold"),fg="black", bg="#EEE9E9")
                username.place(x=60,y=180)
                self.user= Image.open('username.jpg')
                self.resize_image= self.user.resize((40,40))
                new_image= ImageTk.PhotoImage(self.resize_image)
                photo= ImageTk.PhotoImage(self.resize_image)
                self.resize_image=Label(self.f_login,image=photo, bg="#EEE9E9")
                self.resize_image.image=photo
                self.resize_image.place(x=13,y=170)
                self.user_entry=Entry(self.f_login,textvariable=self.username, font=("Calibri Light", 12), bg="white")
                self.user_entry.place(x=13,y=220,height=30, width=300)
                # Password Frame
                password=Label(self.f_login, text="Password", font=("Times New Roman", 15, "bold"),fg="black", bg="#EEE9E9")
                password.place(x=60,y=300)
                self.lock_entry=Entry(self.f_login, textvariable=self.password,font=("Calibri Light", 12), show="*",bg="white")
                self.lock_entry.place(x=13,y=340,height=30, width=300)

                self.passwor = Image.open('password.jpg')
                self.resize_img= self.passwor.resize((40,40))
                new_img= ImageTk.PhotoImage(self.resize_img)
                photo= ImageTk.PhotoImage(self.resize_img)
                self.resize_img=Label(self.f_login,image=photo, bg="#EEE9E9")
                self.resize_img.image=photo
                self.resize_img.place(x=13,y=290)
                
                
                # forgot button
                F_button=Button(self.f_login,command=self.for_pass,text=" Forgot Password",cursor="hand2", bg="#EEE9E9", fg="#CD2626",bd=0,font=("Times New Roman",10)).place(x=215, y=380)
                QF_button=Button(self.f_login,command=self.Register_,text="Sign up",cursor="hand2", bg="#EEE9E9", fg="black",bd=0,font=("Times New Roman",15)).place(x=10, y=380)
                l_button=Button(self.f_login,text=" LOGIN", command=self.check_login,cursor="hand2",bg="#EED8AE", fg="Black",font=("Bell MT",18,"bold")).place(x=140, y=430)

        def check_login(self):
                if self.username.get() == "" or self.password.get() == "":
                       messagebox.showerror("Error", "Username and Password are required")
                else:
                    conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
                    my_cursor = conn.cursor()
                    query = "SELECT * FROM register WHERE username=%s AND passwords=%s"
                    value = (self.username.get(), self.password.get())
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()  
                    if row is not None:
                        messagebox.showinfo("Success", "Login Successful")
                        self.new_window=Toplevel(self.root)
                        self.hms=hotelManagement(self.new_window)
                    else:
                        messagebox.showerror("Error", "Invalid Username or Password")   
                    conn.close()


        def Register_(self):
                self.new_window=Toplevel(self.root)
                self.hms=Register(self.new_window)

        def for_pass(self):
                self.new_window=Toplevel(self.root)
                self.hms=ForgotPassword(self.new_window)





root=Tk()
obj=Login(root)
root.mainloop()
