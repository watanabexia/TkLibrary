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
Mem_frame = tk.Frame(root, height = win_h, width = win_w)
Book_frame = tk.Frame(root, height = win_h, width = win_w)
Loan_frame = tk.Frame(root, height = win_h, width = win_w)
Res_frame = tk.Frame(root, height = win_h, width = win_w)
Fine_frame = tk.Frame(root, height = win_h, width = win_w)
Rep_frame = tk.Frame(root, height = win_h, width = win_w)

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
        
# Root frame object
Mem_button = tk.Button(Root_frame, text = "Memberships", fg = 'black', command = lambda: change_frame(Root_frame, Mem_frame))
Mem_button.pack()
Book_button = tk.Button(Root_frame, text = "Books", fg = 'black', command = lambda: change_frame(Root_frame, Book_frame))
Book_button.pack()
Loan_button = tk.Button(Root_frame, text = "Loans", fg = 'black', command = lambda: change_frame(Root_frame, Loan_frame))
Loan_button.pack()
Res_button = tk.Button(Root_frame, text = "Reservations", fg = 'black', command = lambda: change_frame(Root_frame, Res_frame))
Res_button.pack()
Fine_button = tk.Button(Root_frame, text = "Fines", fg = 'black', command = lambda: change_frame(Root_frame, Fine_frame))
Fine_button.pack()
Rep_button = tk.Button(Root_frame, text = "Reports", fg = 'black', command = lambda: change_frame(Root_frame, Rep_frame))
Rep_button.pack()


#Book frame object
Acq_frame = tk.Frame(root, height = win_h, width = win_w)
Withd_frame = tk.Frame(root, height = win_h, width = win_w)

top_text = tk.Label(Book_frame, text='Select One Of The Options Below', bg='cyan')
top_text.place(x = 150, y = 0, anchor = "nw")

Acq_label = tk.Label(Book_frame, text = "Book Acquisition", fg = 'black')
Acq_label.place(x = 50, y = 50, anchor = "nw")
Acq_button = tk.Button(Book_frame, text = "Acquire A Book", fg = 'black', command = lambda: change_frame(Book_frame, Acq_frame))
Acq_button.place(x = 300, y = 50, anchor = "nw")

Withd_label = tk.Label(Book_frame, text = "Book Withdrawal", fg = 'black')
Withd_label.place(x = 50, y = 100, anchor = "nw")
Withd_button = tk.Button(Book_frame, text = "Withdraw A Book", fg = 'black', command = lambda: change_frame(Book_frame, Withd_frame))
Withd_button.place(x = 300, y = 100, anchor = "nw")

Back_button = tk.Button(Book_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Book_frame, Root_frame))
Back_button.place(x = 175, y = 150, anchor = "nw")


#Book Acquisition object
def add_new_book():
    messagebox.showinfo(title='Success!', message='New Book Added In Library!')
    # messagebox.showinfo(title='Error!', message='Book Already Added; Duplicate, Missing or Incomplete fields')

top_text = tk.Label(Acq_frame, text='For New Book Acquisition, Please Enter Information Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

AN_label = tk.Label(Acq_frame, text='Accession Number', fg = 'black')
AN_label.place(x = 50, y = 50, anchor = "nw")
AN_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
AN_entry.insert(0, "Used to identify an instance of book")
AN_entry.place(x = 300, y = 50, anchor = "nw")

Title_label = tk.Label(Acq_frame, text='Title', fg = 'black')
Title_label.place(x = 50, y = 100, anchor = "nw")
Title_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
Title_entry.insert(0, "Title of the book")
Title_entry.place(x = 300, y = 100, anchor = "nw")

Author_label = tk.Label(Acq_frame, text='Author', fg = 'black')
Author_label.place(x = 50, y = 150, anchor = "nw")
Author_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
Author_entry.insert(0, "Author of the book")
Author_entry.place(x = 300, y = 150, anchor = "nw")

ISBN_label = tk.Label(Acq_frame, text='ISBN', fg = 'black')
ISBN_label.place(x = 50, y = 200, anchor = "nw")
ISBN_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
ISBN_entry.insert(0, "ISBN of the book")
ISBN_entry.place(x = 300, y = 200, anchor = "nw")

Publisher_label = tk.Label(Acq_frame, text='Publisher', fg = 'black')
Publisher_label.place(x = 50, y = 250, anchor = "nw")
Publisher_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
Publisher_entry.insert(0, "Publisher of the book")
Publisher_entry.place(x = 300, y = 250, anchor = "nw")

Year_label = tk.Label(Acq_frame, text='Year', fg = 'black')
Year_label.place(x = 50, y = 300, anchor = "nw")
Year_entry = tk.Entry(Acq_frame, fg = 'black', width = 60)
Year_entry.insert(0, "Year of publishing of the book")
Year_entry.place(x = 300, y = 300, anchor = "nw")

Add_new_book_button = tk.Button(Acq_frame, text = "Add New Book", fg = 'black', command = add_new_book)
Add_new_book_button.place(x = 50, y = 350, anchor = "nw")
Back_to_book_button = tk.Button(Acq_frame, text = "Back To Book", fg = 'black', command = lambda: change_frame(Acq_frame, Book_frame))
Back_to_book_button.place(x = 700, y = 350, anchor = "nw")


#Book Withdrawal object
def withdraw_book():
    messagebox.askyesno(title='Please Confirm The Details Are Correct', message='New Book Added In Library!')
    # messagebox.showinfo(title='Error!', message='Book Is Currently On Loan.')
    # messagebox.showinfo(title='Error!', message='Book Is Currently Reserved.')

top_text = tk.Label(Withd_frame, text='To Remove Outdated Books From System, Please Enter Information Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

AN_label = tk.Label(Withd_frame, text='Accession Number')
AN_label.place(x = 50, y = 200, anchor = "nw")
AN_entry = tk.Entry(Withd_frame, fg = 'black', width = 60)
AN_entry.insert(0, "Used to identify an instance of book")
AN_entry.place(x = 300, y = 200, anchor = "nw")

Withdraw_book_button = tk.Button(Withd_frame, text = "Withdraw Book", fg = 'black', command = withdraw_book)
Withdraw_book_button.place(x = 50, y = 350, anchor = "nw")
Back_to_book_button = tk.Button(Withd_frame, text = "Back To Book", fg = 'black', command = lambda: change_frame(Withd_frame, Book_frame))
Back_to_book_button.place(x = 700, y = 350, anchor = "nw")

#Loan frame object
Borrow_frame = tk.Frame(root, height = win_h, width = win_w)
Return_frame = tk.Frame(root, height = win_h, width = win_w)

top_text = tk.Label(Loan_frame, text='Select One Of The Options Below', bg='cyan')
top_text.place(x = 150, y = 0, anchor = "nw")

Borrow_label = tk.Label(Loan_frame, text = "Book Borrow", fg = 'black')
Borrow_label.place(x = 50, y = 50, anchor = "nw")
Borrow_button = tk.Button(Loan_frame, text = "Borrow A Book", fg = 'black', command = lambda: change_frame(Loan_frame, Borrow_frame))
Borrow_button.place(x = 300, y = 50, anchor = "nw")

Return_label = tk.Label(Loan_frame, text = "Book Return", fg = 'black')
Return_label.place(x = 50, y = 100, anchor = "nw")
Return_button = tk.Button(Loan_frame, text = "Return A Book", fg = 'black', command = lambda: change_frame(Loan_frame, Return_frame))
Return_button.place(x = 300, y = 100, anchor = "nw")

Back_button = tk.Button(Loan_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Loan_frame, Root_frame))
Back_button.place(x = 175, y = 150, anchor = "nw")



#Borrow object
def borrow_book():
    messagebox.askyesno(title='Please Confirm The Loan Details To Be Correct', message='New Book Added In Library!')
    # messagebox.showinfo(title='Error!', message='Book Currently On Loan Until.')
    # messagebox.showinfo(title='Error!', message='Member Loan Quota Exceeded.')
    # messagebox.showinfo(title='Error!', message='Member Has Outstanding Fines.')

top_text = tk.Label(Borrow_frame, text='To Borrow A Book , Please Enter Information Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

AN_label = tk.Label(Borrow_frame, text='Accession Number')
AN_label.place(x = 50, y = 100, anchor = "nw")
AN_entry = tk.Entry(Borrow_frame, fg = 'black', width = 60)
AN_entry.insert(0, "Used to identify an instance of book")
AN_entry.place(x = 300, y = 100, anchor = "nw")

ID_label = tk.Label(Borrow_frame, text='Membership ID')
ID_label.place(x = 50, y = 200, anchor = "nw")
ID_entry = tk.Entry(Borrow_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID_entry.place(x = 300, y = 200, anchor = "nw")

Borrow_book_button = tk.Button(Borrow_frame, text = "Borrow Book", fg = 'black', command = withdraw_book)
Borrow_book_button.place(x = 50, y = 300, anchor = "nw")
Back_to_loan_button = tk.Button(Borrow_frame, text = "Back To Loan", fg = 'black', command = lambda: change_frame(Borrow_frame, Loan_frame))
Back_to_loan_button.place(x = 700, y = 300, anchor = "nw")

#Return object
def return_book():
    messagebox.askyesno(title='Please Confirm The Return Details To Be Correct', message='New Book Added In Library!')
    # messagebox.showinfo(title='Success!', message='Book Returned Successfully.')
    # messagebox.showinfo(title='Error!', message='Book Returned Successfully. But Has Fines')

top_text = tk.Label(Return_frame, text='To Return A Book , Please Enter Information Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

AN_label = tk.Label(Return_frame, text='Accession Number')
AN_label.place(x = 50, y = 100, anchor = "nw")
AN_entry = tk.Entry(Return_frame, fg = 'black', width = 60)
AN_entry.insert(0, "Used to identify an instance of book")
AN_entry.place(x = 300, y = 100, anchor = "nw")

ID_label = tk.Label(Return_frame, text='Membership ID')
ID_label.place(x = 50, y = 200, anchor = "nw")
ID_entry = tk.Entry(Return_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID_entry.place(x = 300, y = 200, anchor = "nw")

Return_book_button = tk.Button(Return_frame, text = "Return Book", fg = 'black', command = return_book)
Return_book_button.place(x = 50, y = 300, anchor = "nw")
Back_to_loan_button = tk.Button(Return_frame, text = "Back To Loan", fg = 'black', command = lambda: change_frame(Return_frame, Loan_frame))
Back_to_loan_button.place(x = 700, y = 300, anchor = "nw")

#Changyang Code
# Membership Frame Object
Mem_create_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_delete_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_update1_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_update2_frame = tk.Frame(root, height = win_h, width = win_w)


# Membership menu labels and buttons
Mem_create_label = tk.Label(Mem_frame, text = "Membership Creation", fg = 'black')
Mem_create_label.place(x = 50, y = 50, anchor = "nw")
Mem_create_button = tk.Button(Mem_frame, text = "Create A Member", fg = 'black', command = lambda: change_frame(Mem_frame, Mem_create_frame))
Mem_create_button.place(x = 300, y = 50, anchor = "nw")

Mem_delete_label = tk.Label(Mem_frame, text = "Membership Deletion", fg = 'black')
Mem_delete_label.place(x = 50, y = 100, anchor = "nw")
Mem_delete_button = tk.Button(Mem_frame, text = "Delete A Member", fg = 'black', command = lambda: change_frame(Mem_frame, Mem_delete_frame))
Mem_delete_button.place(x = 300, y = 100, anchor = "nw")

Mem_update_label = tk.Label(Mem_frame, text = "Membership Update", fg = 'black')
Mem_update_label.place(x = 50, y = 150, anchor = "nw")
Mem_update_button = tk.Button(Mem_frame, text = "Update A Member", fg = 'black', command = lambda: change_frame(Mem_frame, Mem_update1_frame))
Mem_update_button.place(x = 300, y = 150, anchor = "nw")

Back_button = tk.Button(Mem_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Mem_frame, Root_frame))
Back_button.place(x = 175, y = 200, anchor = "nw")



# Deletion Object
def delete_mem():
    None

top_text = tk.Label(Mem_delete_frame, text='To Delete A Member, Please Membership ID Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

ID_label = tk.Label(Mem_delete_frame, text='Membership ID')
ID_label.place(x = 50, y = 200, anchor = "nw")
ID_entry = tk.Entry(Mem_delete_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID_entry.place(x = 300, y = 200, anchor = "nw")


Mem_delete_button = tk.Button(Mem_delete_frame, text = "Delete Member", fg = 'black', command = delete_mem)
Mem_delete_button.place(x = 50, y = 300, anchor = "nw")
Back_to_mem_button = tk.Button(Mem_delete_frame, text = "Back To Membership Menu", fg = 'black', command = lambda: change_frame(Mem_delete_frame, Mem_frame))
Back_to_mem_button.place(x = 700, y = 300, anchor = "nw")

#Update1 Object 

top_text = tk.Label(Mem_update1_frame, text='To Update A Member, Please Membership ID Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

ID_label = tk.Label(Mem_update1_frame, text='Membership ID')
ID_label.place(x = 50, y = 200, anchor = "nw")
ID_entry = tk.Entry(Mem_update1_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID = ID_entry.get()
ID_entry.place(x = 300, y = 200, anchor = "nw")


Mem_update1_button = tk.Button(Mem_update1_frame, text = "Update Member", fg = 'black', command = lambda: change_frame(Mem_update1_frame, Mem_update2_frame))
Mem_update1_button.place(x = 50, y = 300, anchor = "nw")
Back_to_mem_button = tk.Button(Mem_update1_frame, text = "Back To Membership Menu", fg = 'black', command = lambda: change_frame(Mem_update1_frame, Mem_frame))
Back_to_mem_button.place(x = 700, y = 300, anchor = "nw")

#Update2 Object 
Mem_ID_label1 = tk.Label(Mem_update2_frame, text='Membership ID', fg = 'black')
Mem_ID_label1.place(x = 50, y = 50, anchor = "nw")
Mem_ID_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Mem_ID_entry.insert(0, ID)
Mem_ID_entry.place(x = 300, y = 50, anchor = "nw")

Name_label = tk.Label(Mem_update2_frame, text='Name', fg = 'black')
Name_label.place(x = 50, y = 100, anchor = "nw")
Name_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Name_entry.insert(0, "Update name")
Name_entry.place(x = 300, y = 100, anchor = "nw")

Faculty_label = tk.Label(Mem_update2_frame, text='Faculty', fg = 'black')
Faculty_label.place(x = 50, y = 150, anchor = "nw")
Faculty_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Faculty_entry.insert(0, "Update faculty")
Faculty_entry.place(x = 300, y = 150, anchor = "nw")

Phone_number_label = tk.Label(Mem_update2_frame, text='Phone Number', fg = 'black')
Phone_number_label.place(x = 50, y = 200, anchor = "nw")
Phone_number_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Phone_number_entry.insert(0, "Update phone number")
Phone_number_entry.place(x = 300, y = 200, anchor = "nw")

# Deletion Object
def Mem_update():
    None

Email_Address_label = tk.Label(Mem_update2_frame, text='Email Address', fg = 'black')
Email_Address_label.place(x = 50, y = 250, anchor = "nw")
Email_Address_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Email_Address_entry.insert(0, "Update Email")
Email_Address_entry.place(x = 300, y = 250, anchor = "nw")

Mem_update2_button = tk.Button(Mem_update2_frame, text = "Update Member", fg = 'black', command = Mem_update)
Mem_update2_button.place(x = 50, y = 300, anchor = "nw")
Back_to_mem_button = tk.Button(Mem_update2_frame, text = "Back To Membership Menu", fg = 'black', command = lambda: change_frame(Mem_update2_frame, Mem_frame))
Back_to_mem_button.place(x = 700, y = 300, anchor = "nw")

#Qingyang Code
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