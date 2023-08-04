from tkinter import *
import sqlite3

root = Tk()
root.title('Icons in tkinter.')
root.geometry("400x400")

# Database

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

c.execute("""CREATE TABLE addresses(
            first_name text,
            number int);
""")

conn.commit()

conn.close()

root.mainloop()