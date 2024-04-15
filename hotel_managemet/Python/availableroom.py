from tkinter import Tk, ttk
import psycopg2
from tkinter import messagebox

class AvailableRoomPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Rooms")
        self.root.geometry("250x330+310+265")

        self.tree = ttk.Treeview(self.root, columns=("Room Number", "Room Type"), show="headings")

        # Set column headings
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Room Type", text="Room Type")

        # Set column widths
        self.tree.column("Room Number", width=100)
        self.tree.column("Room Type", width=100)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Bind double-click event to a callback function
        self.tree.bind("<Double-1>", self.on_double_click)

        # Pack the Treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.display_data()

    def display_data(self):
        conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM "public"."roomdetailss"')
        rows = my_cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

        conn.close()

    def on_double_click(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, 'values')
            self.delete_room(values[0])
            self.tree.delete(item)
        self.root.destroy()

    def delete_room(self, room_number):
        # Implement the deletion logic from the database based on the room number
        conn = psycopg2.connect(host="localhost", user="postgres", password="aiman", database="hotelManagement")
        my_cursor = conn.cursor()
        query = "DELETE FROM roomdetailss WHERE Room_no = %s"
        value = (room_number,)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = AvailableRoomPage(root)
    root.mainloop()
