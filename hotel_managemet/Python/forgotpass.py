from tkinter import *
from tkinter import ttk, messagebox
import psycopg2

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("400x300+440+120")

        self.email = StringVar()
        self.new_password = StringVar()
        self.confirm_password = StringVar()

        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=400, height=300)

        email_label = Label(frame, text="Email Address:", font=("Calibri", 15), fg="indigo", bg="White")
        email_label.place(x=10, y=50)
        email_entry = ttk.Entry(frame, textvariable=self.email, font=("Calibri", 15))
        email_entry.place(x=10, y=80, width=280)

        new_password_label = Label(frame, text="New Password:", font=("Calibri", 15), fg="indigo", bg="White")
        new_password_label.place(x=10, y=120)
        new_password_entry = ttk.Entry(frame, textvariable=self.new_password, font=("Calibri", 15), show="*")
        new_password_entry.place(x=10, y=150, width=280)

        confirm_password_label = Label(frame, text="Confirm Password:", font=("Calibri", 15), fg="indigo", bg="White")
        confirm_password_label.place(x=10, y=190)
        confirm_password_entry = ttk.Entry(frame, textvariable=self.confirm_password, font=("Calibri", 15), show="*")
        confirm_password_entry.place(x=10, y=220, width=280)

        reset_button = Button(frame, text="Reset Password", command=self.reset_password,
                              font=("Calibri", 15, "bold"), bd=3, relief=RIDGE, fg="WHITE", bg="Green",
                              activeforeground="white", activebackground="black")
        reset_button.place(x=120, y=260, width=160, height=35)

    def reset_password(self):
        # Get user input
        email = self.email.get()
        new_password = self.new_password.get()
        confirm_password = self.confirm_password.get()

        # Check if the email exists in the database
        conn = psycopg2.connect(host="localhost", user="postgres", password="secomps", database="hotelManagement")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM register WHERE email = %s", (email,))
        user_data = my_cursor.fetchone()
        conn.close()

        if user_data is None:
            messagebox.showerror("Error", "Email not found. Please enter a valid email.", parent=self.root)
        else:
            # Email found, update the password
            if new_password == confirm_password:
                # Update password in the database
                conn = psycopg2.connect(host="localhost", user="postgres", password="secomps", database="hotelManagement")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE register SET passwords = %s WHERE email = %s", (new_password, email))
                conn.commit()
                conn.close()

                # Display a success message
                messagebox.showinfo("Success", "Password reset successful!", parent=self.root)
            else:
                # Passwords don't match
                messagebox.showerror("Error", "Passwords do not match. Please enter matching passwords.", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = ForgotPassword(root)
    root.mainloop()
