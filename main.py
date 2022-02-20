import tkinter as tk
from tkinter import messagebox

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import *
from sqlalchemy.exc import *

from datetime import datetime

from dbTable import *
# ------ Database Function ------ #
db_user = "root"
db_password = "123456"
schema_name = "bt2102_as_1"

# Database Connection Initialization
engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'.format(db_user, db_password, schema_name),
echo = True)
DBSession = sessionmaker(bind = engine)
session = DBSession()


# ---------- UI ----------- #
win_w = 1000
win_h = 1000

# UI Initialization
root = tk.Tk()
root.title('ALS')
root.geometry("{}x{}".format(str(win_w), str(win_h)))
root.option_add("*font", "SF\ Pro 14")

# Frame Definition
Root_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_frame = tk.Frame(root)
Book_frame = tk.Frame(root)
Loan_frame = tk.Frame(root)
Res_frame = tk.Frame(root, height = win_h, width = win_w)
Fine_frame = tk.Frame(root)
Rep_frame = tk.Frame(root)

# Frame Control Function
def change_frame(from_frame, to_frame):
    from_frame.pack_forget()
    to_frame.pack()

# Query Function
class QueryError(Exception):
    pass

def get_member(member_id):
    """
    get the member with the unique member id.
    * Returns None if no valid LibMember is found.
    """

    try: # Check if the member ID is valid
        mem = session.query(LibMember).filter_by(memberid = member_id).one()
    except NoResultFound:
        messagebox.showerror(title = "Error", message = "\"{}\" is not a valid member id.".format(member_id))
        raise QueryError
    else:
        return mem

def get_book(acc_number):
    """
    get the book with the unique acc number.
    * Returns None if no valid LibBook is found.
    """

    try: # Check if the member ID is valid
        book = session.query(LibBooks).filter_by(Accession_Number = acc_number).one()
    except NoResultFound:
        messagebox.showerror(title = "Error", message = "\"{}\" is not a valid accession number.".format(acc_number))
        raise QueryError
    else:
        return book

def get_date_object(date_string):
    try:
        return datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        messagebox.showerror(title = "Error", message = "\"{}\" is not a valid date or a valid date format.".format(date_string))
        raise QueryError

#TODO:
# def is_book_on_loan(acc_number):
    

# Root frame object
Welcome_label = tk.Label(Root_frame, text = "Welcome to Another Library System (ALS)!", fg = 'black')
Welcome_label.place(x = 50, y = 50, anchor = "nw")
Mem_button = tk.Button(Root_frame, text = "Memberships", fg = 'black', command = lambda: change_frame(Root_frame, Mem_frame))
Mem_button.place(x = 50, y = 100, anchor = "nw")
Book_button = tk.Button(Root_frame, text = "Books", fg = 'black', command = lambda: change_frame(Root_frame, Book_frame))
Book_button.place(x = 50, y = 150, anchor = "nw")
Loan_button = tk.Button(Root_frame, text = "Loans", fg = 'black', command = lambda: change_frame(Root_frame, Loan_frame))
Loan_button.place(x = 50, y = 200, anchor = "nw")
Res_button = tk.Button(Root_frame, text = "Reservations", fg = 'black', command = lambda: change_frame(Root_frame, Res_frame))
Res_button.place(x = 50, y = 250, anchor = "nw")
Fine_button = tk.Button(Root_frame, text = "Fines", fg = 'black', command = lambda: change_frame(Root_frame, Fine_frame))
Fine_button.place(x = 50, y = 300, anchor = "nw")
Rep_button = tk.Button(Root_frame, text = "Reports", fg = 'black', command = lambda: change_frame(Root_frame, Rep_frame))
Rep_button.place(x = 50, y = 350, anchor = "nw")

# Qingyang begins
# Reservation frame object
Res_book_frame = tk.Frame(root, height = win_h, width = win_w)
Res_cancel_frame = tk.Frame(root, height = win_h, width = win_w)

Res_book_label = tk.Label(Res_frame, text = "Book Reservation", fg = 'black')
Res_book_label.place(x = 50, y = 50, anchor = "nw")
Res_book_button = tk.Button(Res_frame, text = "Reserve a Book", fg = 'black', command = lambda: change_frame(Res_frame, Res_book_frame))
Res_book_button.place(x = 300, y = 50, anchor = "nw")
Res_cancel_label = tk.Label(Res_frame, text = "Reservation Cancellation", fg = 'black')
Res_cancel_label.place(x = 50, y = 100, anchor = "nw")
Res_cancel_button = tk.Button(Res_frame, text = "Cancel Reservation", fg = 'black', command = lambda: change_frame(Res_frame, Res_cancel_frame))
Res_cancel_button.place(x = 300, y = 100, anchor = "nw")

Res_book_title_label = tk.Label(Res_book_frame, text = "To reserve a book, please enter information below:", fg = 'black')
Res_book_title_label.place(x = 50, y = 0, anchor = "nw")
Res_book_Acc_number_label = tk.Label(Res_book_frame, text = "Accession Number", fg = 'black')
Res_book_Acc_number_label.place(x = 50, y = 50, anchor = "nw")
Res_book_Acc_number_entry = tk.Entry(Res_book_frame, fg = 'black', bg = 'white', width = 60)
# Res_book_Acc_number_entry.insert(0, "Used to identify an instance of book")
Res_book_Acc_number_entry.place(x = 300, y = 50, anchor = "nw")
Res_book_Mem_ID_label = tk.Label(Res_book_frame, text = "Membership ID", fg = 'black')
Res_book_Mem_ID_label.place(x = 50, y = 100, anchor = "nw")
Res_book_Mem_ID_entry = tk.Entry(Res_book_frame, fg = 'black', bg = 'white', width = 60)
# Res_book_Mem_ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
Res_book_Mem_ID_entry.place(x = 300, y = 100, anchor = "nw")
Res_book_Res_date_label = tk.Label(Res_book_frame, text = "Reserve date (MM/DD/YYYY)", fg = 'black')
Res_book_Res_date_label.place(x = 50, y = 150, anchor = "nw")
Res_book_Res_date_entry = tk.Entry(Res_book_frame, fg = 'black', bg = 'white', width = 60)
Res_book_Res_date_entry.insert(0, "02/20/2022")
Res_book_Res_date_entry.place(x = 300, y = 150, anchor = "nw")

def confirm_book_reservation():
    mem_id = Res_book_Mem_ID_entry.get()
    acc_number = Res_book_Acc_number_entry.get()

    try:
        res_date = get_date_object(Res_book_Res_date_entry.get())
        mem = get_member(mem_id)
        book = get_book(acc_number)
        

    except QueryError:
        print("[confirm_book_reservation] QueryError.")
        return



        

Res_book_Res_button = tk.Button(Res_book_frame, text = "Reserve Book", fg = 'black', command = confirm_book_reservation)
Res_book_Res_button.place(x = 50, y = 200, anchor = "nw")
Res_book_Back_button = tk.Button(Res_book_frame, text = "Back to Reservation Menu", fg = 'black', command = lambda: change_frame(Res_book_frame, Res_frame))
Res_book_Back_button.place(x = 700, y = 200, anchor = "nw")

Res_cancel_title_label = tk.Label(Res_cancel_frame, text = "To cancel a reservation, please enter information below:", fg = 'black')
Res_cancel_title_label.place(x = 50, y = 0, anchor = "nw")
Res_cancel_Acc_number_label = tk.Label(Res_cancel_frame, text = "Accession Number", fg = 'black')
Res_cancel_Acc_number_label.place(x = 50, y = 50, anchor = "nw")
Res_cancel_Acc_number_entry = tk.Entry(Res_cancel_frame, fg = 'black', width = 60)
Res_cancel_Acc_number_entry.insert(0, "Used to identify an instance of book")
Res_cancel_Acc_number_entry.place(x = 300, y = 50, anchor = "nw")
Res_cancel_Mem_ID_label = tk.Label(Res_cancel_frame, text = "Membership ID", fg = 'black')
Res_cancel_Mem_ID_label.place(x = 50, y = 100, anchor = "nw")
Res_cancel_Mem_ID_entry = tk.Entry(Res_cancel_frame, fg = 'black', width = 60)
Res_cancel_Mem_ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
Res_cancel_Mem_ID_entry.place(x = 300, y = 100, anchor = "nw")
Res_cancel_Cancel_date_label = tk.Label(Res_cancel_frame, text = "Cancel date", fg = 'black')
Res_cancel_Cancel_date_label.place(x = 50, y = 150, anchor = "nw")
Res_cancel_Cancel_date_entry = tk.Entry(Res_cancel_frame, fg = 'black', width = 60)
Res_cancel_Cancel_date_entry.insert(0, "Date of reservation cancellation")
Res_cancel_Cancel_date_entry.place(x = 300, y = 150, anchor = "nw")

Res_cancel_Res_button = tk.Button(Res_cancel_frame, text = "Cancel Reservation", fg = 'black')
Res_cancel_Res_button.place(x = 50, y = 200, anchor = "nw")
Res_cancel_Back_button = tk.Button(Res_cancel_frame, text = "Back to Reservation Menu", fg = 'black', command = lambda: change_frame(Res_cancel_frame, Res_frame))
Res_cancel_Back_button.place(x = 700, y = 200, anchor = "nw")
# Qingyang ends

# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()

session.close()