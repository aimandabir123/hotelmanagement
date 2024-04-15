from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class PaymentPage:
    def __init__(self, root, total_cost):
        self.root = root
        self.root.title("Payment Page")
        self.root.geometry("600x300+605+262")
        

        # Convert total_cost to float if it's a string
        self.total_cost = float(total_cost) if isinstance(total_cost, str) else total_cost

        self.amount_label = Label(self.root, text="Amount:", font=("Arial", 12))
        self.amount_label.place(x=20, y=30)

        self.amount_var = StringVar()
        self.amount_var.set("{:.2f}".format(self.total_cost))  # Set the amount variable
        self.amount_entry = Entry(self.root, textvariable=self.amount_var, font=("Arial", 12), state="readonly")
        self.amount_entry.place(x=20, y=60)

        self.payment_successful = False

        self.payment_method_label = Label(self.root, text="Payment Method:", font=("Arial", 12))
        self.payment_method_label.place(x=20, y=120)

        self.payment_method_var = StringVar()
        self.payment_method_combobox = ttk.Combobox(self.root, textvariable=self.payment_method_var, values=["Credit/Debit Card", "UPI"], font=("Arial", 12), state="readonly")
        self.payment_method_combobox.place(x=20, y=170)
        self.payment_method_combobox.bind("<<ComboboxSelected>>", self.on_payment_method_selected)

        self.pay_button = Button(self.root, text="Pay", command=self.process_payment, font=("Arial", 12), bg="green", fg="white")
        self.pay_button.place(x=80, y=220, width=70)


    def on_payment_method_selected(self, event):
        selected_method = self.payment_method_var.get()

        if selected_method == "Credit/Debit Card":
            self.display_credit_card_details()
        elif selected_method == "UPI":
            self.display_upi_image()
        else:
            self.clear_right_panel()

    def display_credit_card_details(self):
        self.clear_right_panel()
        self.card_number_label = Label(self.root, text="Card/Debit Card:", font=("Arial", 12))
        self.card_number_label.place(x=300, y=30)

        self.card_number_var = StringVar()
        self.card_number_entry = Entry(self.root, textvariable=self.card_number_var, font=("Arial", 12))
        self.card_number_entry.place(x=300, y=60)

        self.expiry_label = Label(self.root, text="Expiry Date:", font=("Arial", 12))
        self.expiry_label.place(x=300, y=120)

        self.expiry_var = StringVar()
        self.expiry_combobox = ttk.Combobox(self.root, textvariable=self.expiry_var, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12","13","14","15","16","17","18","19","20", "21", "22","23","24","25","26","27","28","29","30","31"], font=("Arial", 12), state="readonly")
        self.expiry_combobox.current(0)
        self.expiry_combobox.place(x=300, y=170,width=70)

        self.year_label = Label(self.root, text="Year:", font=("Arial", 12))
        self.year_label.place(x=400, y=120)

        self.year_var = StringVar()
        self.year_combobox = ttk.Combobox(self.root, textvariable=self.year_var, values=["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038","2039","2040"], font=("Arial", 12), state="readonly")
        self.year_combobox.current(0)
        self.year_combobox.place(x=400, y=170, width=70)

        

    def display_upi_image(self):
        self.clear_right_panel()  # Clear existing widgets

        self.upi_image = Image.open(r"pic.jpg")
        self.upi_image = self.upi_image.resize((200, 200))
        self.upi_image = ImageTk.PhotoImage(self.upi_image)

        self.upi_label = Label(self.root, image=self.upi_image)
        self.upi_label.place(x=300, y=30)   

    def clear_right_panel(self):
    # Clear existing widgets in the right panel, excluding amount and payment entry widgets
        for widget in self.root.winfo_children():
            if widget.winfo_class() == "Label" or widget.winfo_class() == "Entry" or widget.winfo_class() == "Combobox":
                if widget not in [self.amount_label, self.amount_entry, self.payment_method_label, self.payment_method_combobox, self.pay_button]:
                    widget.destroy()
            elif widget.winfo_class() == "TLabel" and widget not in [self.amount_label, self.payment_method_label]:
                widget.destroy()




    def process_payment(self):
        amount = self.amount_var.get()
        payment_method = self.payment_method_var.get()

        if not amount or not payment_method:
            messagebox.showerror("Error", "Please enter amount and select payment method." ,parent=self.root)
        else:
            if payment_method == "Credit/Debit Card":
                card_number = self.card_number_var.get()
                expiry_date = self.expiry_var.get()
                year = self.year_var.get()
                if not card_number or not expiry_date or not year:
                    messagebox.showerror("Error", "Please enter all credit card details.", parent=self.root)
                    return

            messagebox.showinfo("Payment Successful", f"Payment of {amount} via {payment_method} successful.", parent=self.root)
            self.payment_successful = True
            self.root.destroy()




if __name__ == "__main__":
    root = Tk()
    total_cost_var = StringVar()
    payment_page = PaymentPage(root, total_cost_var)
    root.mainloop()