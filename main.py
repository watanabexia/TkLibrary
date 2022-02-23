from operator import and_
from sqlalchemy import Table, Column, String, create_engine, Integer, Date, MetaData
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import *
from sqlalchemy.exc import *
from sqlalchemy import and_

from datetime import datetime

from dbTable import *
# ------ Database Function ------ #
db_user = "root"
db_password = "201314"
schema_name = "bt2102_as_1"

# Database Connection Initialization
engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'.format(db_user, db_password, schema_name),
echo = True)
metadata = MetaData(engine)
DBSession = sessionmaker(bind = engine)
conn = engine.connect()
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

def change_frame_delete_infor(from_frame, to_frame, tree):
    for i in tree.get_children():
        tree.delete(i)
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
    return session.query(LibMember).filter_by(memberid = member_id).one()

def get_book(acc_number):
    """
    get the book with the unique acc number.
    * Returns None if no valid LibBook is found.
    """
    return session.query(LibBooks).filter_by(Accession_Number = acc_number).one()

def get_book_contains_author(author_one):
    if " " in author_one:
        messagebox.showinfo(title='Wrong!', message='Input cannot be more than one word')
    else:
        return session.query(Book_Author).filter(Book_Author.Author.contains(author_one)).all()

def get_book_contains(title_one, ISBN_one, publisher_one, publication_year_one):
    if " " in title_one  or " " in ISBN_one or " " in publisher_one or " " in publication_year_one:
        messagebox.showinfo(title='Wrong!', message='Input cannot be more than one word')
    else: 
        return session.query(LibBooks).filter(and_(
            LibBooks.Title.contains(title_one),
            LibBooks.ISBN.contains(ISBN_one),
            LibBooks.Publisher.contains(publisher_one),
            LibBooks.Year.contains(publication_year_one))).all()

def get_book_on_loan():
    return session.query(Borrow_And_Return_Record).order_by(Borrow_And_Return_Record.Accession_Number).all()
 
def get_borrow_record_by_memid(mem_id):
    return session.query(Borrow_And_Return_Record).filter_by(memberid = mem_id).all()

def get_book_on_reserve():
    return session.query(Reserve_Record).order_by(Reserve_Record.Accession_Number).all()

def get_mem_with_fines():
    return session.query(LibMember).filter(LibMember.outstanding_fee != 0).all()

def get_book_title_based_on_AN(acc_number):
    books = session.query(LibBooks).filter_by(Accession_Number = acc_number).all()
    res = ''
    for book in books:
        res += book.Title
    return res

def get_book_ISBN_based_on_AN(acc_number):
    books = session.query(LibBooks).filter_by(Accession_Number = acc_number).all()
    res = ''
    for book in books:
        res += book.ISBN
    return res

def get_book_publisher_based_on_AN(acc_number):
    books = session.query(LibBooks).filter_by(Accession_Number = acc_number).all()
    res = ''
    for book in books:
        res += book.Publisher
    return res

def get_book_year_based_on_AN(acc_number):
    books = session.query(LibBooks).filter_by(Accession_Number = acc_number).all()
    res = ''
    for book in books:
        res += str(book.Year)
    return res

def get_member_name_based_on_id(mem_id):
    books = session.query(LibMember).filter_by(memberid = mem_id).all()
    res = ''
    for book in books:
        res += book.name
    return res

def get_Authors_report_loan(acc_number):
    res = ''
    books = session.query(Book_Author).filter_by(Accession_Number = acc_number).all()
    for book in books:
        res += book.Author
    return res

def get_date_object(date_string):
    return datetime.strptime(date_string, '%m/%d/%Y')

def is_book_on_loan(acc_number):
    """
    check if a book is on loan.
    Returns True if is on loan. False if is not on loan.
    """
    book = get_book(acc_number)
    try:
        br_record = session.query(Borrow_And_Return_Record).filter_by(Accession_Number = acc_number, Return_Date = None).one()
    except NoResultFound:
        return False
    else:
        return True

# def has_outstanding_fine(member_id):

# Root frame object
top_text = tk.Label(Root_frame, text='ALS System', bg='cyan')
top_text.place(x = 250, y = 0, anchor = "nw")
Mem_button = tk.Button(Root_frame, text = "Memberships", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Mem_frame))
Mem_button.place(x = 200, y = 50, anchor = "nw")
Book_button = tk.Button(Root_frame, text = "Books", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Book_frame))
Book_button.place(x = 200, y = 100, anchor = "nw")
Loan_button = tk.Button(Root_frame, text = "Loans", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Loan_frame))
Loan_button.place(x = 200, y = 150, anchor = "nw")
Res_button = tk.Button(Root_frame, text = "Reservations", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Res_frame))
Res_button.place(x = 200, y = 200, anchor = "nw")
Fine_button = tk.Button(Root_frame, text = "Fines", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Fine_frame))
Fine_button.place(x = 200, y = 250, anchor = "nw")
Rep_button = tk.Button(Root_frame, text = "Reports", width=20, fg = 'black', command = lambda: change_frame(Root_frame, Rep_frame))
Rep_button.place(x = 200, y = 300, anchor = "nw")

#Membership Frame
# Membership Frame Object
Mem_create_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_delete_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_update1_frame = tk.Frame(root, height = win_h, width = win_w)
Mem_update2_frame = tk.Frame(root, height = win_h, width = win_w)

# Membership menu labels and buttons
top_text = tk.Label(Mem_frame, text='Select One Of The Options Below', bg='cyan')
top_text.place(x = 150, y = 0, anchor = "nw")

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


# Membership creation labels and buttons
def create_new_member():
    messagebox.showinfo(title='Success!', message='ALS Membership Created')

top_text = tk.Label(Mem_create_frame, text='To Create Member, Please Enter Requested Information Below:', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Mem_ID_label1 = tk.Label(Mem_create_frame, text='Membership ID', fg = 'black')
Mem_ID_label1.place(x = 50, y = 50, anchor = "nw")
Mem_ID_entry = tk.Entry(Mem_create_frame, fg = 'black', width = 60)
Mem_ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
Mem_ID_entry.place(x = 300, y = 50, anchor = "nw")

Name_label = tk.Label(Mem_create_frame, text='Name', fg = 'black')
Name_label.place(x = 50, y = 100, anchor = "nw")
Name_entry = tk.Entry(Mem_create_frame, fg = 'black', width = 60)
Name_entry.insert(0, "Enter member's name")
Name_entry.place(x = 300, y = 100, anchor = "nw")

Faculty_label = tk.Label(Mem_create_frame, text='Faculty', fg = 'black')
Faculty_label.place(x = 50, y = 150, anchor = "nw")
Faculty_entry = tk.Entry(Mem_create_frame, fg = 'black', width = 60)
Faculty_entry.insert(0, "e.g., Computing, Engineering, Science, etc.")
Faculty_entry.place(x = 300, y = 150, anchor = "nw")

Phone_number_label = tk.Label(Mem_create_frame, text='Phone Number', fg = 'black')
Phone_number_label.place(x = 50, y = 200, anchor = "nw")
Phone_number_entry = tk.Entry(Mem_create_frame, fg = 'black', width = 60)
Phone_number_entry.insert(0, "e.g., 91234567, 81093487, 92054981, etc.")
Phone_number_entry.place(x = 300, y = 200, anchor = "nw")

Email_Address_label = tk.Label(Mem_create_frame, text='Email Address', fg = 'black')
Email_Address_label.place(x = 50, y = 250, anchor = "nw")
Email_Address_entry = tk.Entry(Mem_create_frame, fg = 'black', width = 60)
Email_Address_entry.insert(0, "e.g., ALSuser@als.edu")
Email_Address_entry.place(x = 300, y = 250, anchor = "nw")

Add_new_member_button = tk.Button(Mem_create_frame, text = "Create Member", fg = 'black', command = create_new_member)
Add_new_member_button.place(x = 50, y = 300, anchor = "nw")
Back_to_membership_menu_button_C = tk.Button(Mem_create_frame, text = "Back To Membership Menu", fg = 'black', command = lambda: change_frame(Mem_create_frame, Mem_frame))
Back_to_membership_menu_button_C.place(x = 700, y = 300, anchor = "nw")


# Membership deletion labels and buttons
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


# Membership update menu labels and buttons
top_text = tk.Label(Mem_update1_frame, text='To Update A Member, Please Membership ID Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

ID_label = tk.Label(Mem_update1_frame, text='Membership ID')
ID_label.place(x = 50, y = 200, anchor = "nw")
ID_entry = tk.Entry(Mem_update1_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID_entry.place(x = 300, y = 200, anchor = "nw")


Mem_update1_button = tk.Button(Mem_update1_frame, text = "Update Member", fg = 'black', command = lambda: change_frame(Mem_update1_frame, Mem_update2_frame))
Mem_update1_button.place(x = 50, y = 300, anchor = "nw")
Back_to_mem_button = tk.Button(Mem_update1_frame, text = "Back To Membership Menu", fg = 'black', command = lambda: change_frame(Mem_update1_frame, Mem_frame))
Back_to_mem_button.place(x = 700, y = 300, anchor = "nw")

# Membership update information labels and buttons
def update_mem():
    None

Mem_ID_label1 = tk.Label(Mem_update2_frame, text='Membership ID', fg = 'red')
Mem_ID_label1.place(x = 50, y = 50, anchor = "nw")
Mem_ID_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Mem_ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
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

Email_Address_label = tk.Label(Mem_update2_frame, text='Email Address', fg = 'black')
Email_Address_label.place(x = 50, y = 250, anchor = "nw")
Email_Address_entry = tk.Entry(Mem_update2_frame, fg = 'black', width = 60)
Email_Address_entry.insert(0, "Update Email")
Email_Address_entry.place(x = 300, y = 250, anchor = "nw")

Mem_update2_button = tk.Button(Mem_update2_frame, text = "Update Member", fg = 'black', command = lambda: change_frame(Mem_update2_frame, update_mem))
Mem_update2_button.place(x = 50, y = 300, anchor = "nw")
Back_to_mem_button = tk.Button(Mem_update2_frame, text = "Back To Previous Membership Menu", fg = 'black', command = lambda: change_frame(Mem_update2_frame, Mem_update1_frame))
Back_to_mem_button.place(x = 700, y = 300, anchor = "nw")


#Book Frame
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
    # tkinter.messagebox.showinfo(title='Error!', message='Book Already Added; Duplicate, Missing or Incomplete fields')

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
    # tkinter.messagebox.showinfo(title='Error!', message='Book Is Currently On Loan.')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Is Currently Reserved.')

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

#Loan Frame
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
    # tkinter.messagebox.showinfo(title='Error!', message='Book Currently On Loan Until.')
    # tkinter.messagebox.showinfo(title='Error!', message='Member Loan Quota Exceeded.')
    # tkinter.messagebox.showinfo(title='Error!', message='Member Has Outstanding Fines.')

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
    # tkinter.messagebox.showinfo(title='Success!', message='Book Returned Successfully.')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Returned Successfully. But Has Fines')

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



# Reservation frame object
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

    # try:
    #     res_date = get_date_object(Res_book_Res_date_entry.get())
    # except:
    #     messagebox.showerror(title = "Error", message = "\"{}\" is not a valid date or a valid date format.".format(date_string))
    
    # try:
    #     mem = get_member(mem_id)
    # except:
    #     messagebox.showerror(title = "Error", message = "\"{}\" is not a valid member id.".format(member_id))
    
    try:
        book = get_book(acc_number)
    except:
        messagebox.showerror(title = "Error", message = "\"{}\" is not a valid accession number.".format(acc_number))
        if (is_book_on_loan(acc_number)):
            pass
        else:
            messagebox.showerror(title = "Error", message = "\"{}\" is available. You may go ahead and borrow it now.".format(book.name))

    # except QueryError:
    #     print("[confirm_book_reservation] QueryError.")
    #     return     

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

#Fine frame
# Fine menu labels and buttons
Fine_payment_frame = tk.Frame(root, height = win_h, width = win_w)

top_text = tk.Label(Fine_frame, text='Select The Option Below', bg='cyan')
top_text.place(x = 150, y = 0, anchor = "nw")

Fine_payment_label = tk.Label(Fine_frame, text = "Payment", fg = 'black')
Fine_payment_label.place(x = 50, y = 50, anchor = "nw")
Fine_payment_button = tk.Button(Fine_frame, text = "Fine Payment", fg = 'black', command = lambda: change_frame(Fine_frame, Fine_payment_frame))
Fine_payment_button.place(x = 150, y = 47, anchor = "nw")

Back_to_mem_button = tk.Button(Fine_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Fine_frame, Root_frame))
Back_to_mem_button.place(x = 300, y = 100, anchor = "nw")


# Fine payment labels and buttons
def pay_fine():
    None
top_text = tk.Label(Fine_payment_frame, text='To Pay a Fine, Please Enter Information Below:', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

ID_label = tk.Label(Fine_payment_frame, text='Membership ID')
ID_label.place(x = 50, y = 50, anchor = "nw")
ID_entry = tk.Entry(Fine_payment_frame, fg = 'black', width = 60)
ID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
ID_entry.place(x = 300, y = 50, anchor = "nw")

Payment_date_label = tk.Label(Fine_payment_frame, text='Payment Date')
Payment_date_label.place(x = 50, y = 100, anchor = "nw")
Payment_date_entry = tk.Entry(Fine_payment_frame, fg = 'black', width = 60)
Payment_date_entry.insert(0, "Date Payment Received")
Payment_date_entry.place(x = 300, y = 100, anchor = "nw")

Payment_amount_label = tk.Label(Fine_payment_frame, text='Payment Amount')
Payment_amount_label.place(x = 50, y = 150, anchor = "nw")
Payment_amount_entry = tk.Entry(Fine_payment_frame, fg = 'black', width = 60)
Payment_amount_entry.insert(0, "Total fine amount")
Payment_amount_entry.place(x = 300, y = 150, anchor = "nw")

Pay_fine_button = tk.Button(Fine_payment_frame, text = "Pay Fine", fg = 'black', command = pay_fine)
Pay_fine_button.place(x = 50, y = 200, anchor = "nw")
Back_to_fine_menu_button = tk.Button(Fine_payment_frame, text = "Back To Fines Menu", fg = 'black', command = lambda: change_frame(Fine_payment_frame, Fine_frame))
Back_to_fine_menu_button.place(x = 700, y = 200, anchor = "nw")

#xunuo start
#Report frame
#other frames in the report frame
Book_search_frame = tk.Frame(root, height = win_h, width = win_w)
Book_search_results_frame = tk.Frame(root, height = win_h, width = win_w)
Book_on_Loan_frame = tk.Frame(root, height = win_h, width = win_w)
Book_on_reservation_frame = tk.Frame(root, height = win_h, width = win_w)
Outstanding_Fines__frame = tk.Frame(root, height = win_h, width = win_w)
Books_on_Loan_to_Member__frame = tk.Frame(root, height = win_h, width = win_w)
Books_on_Loan_to_Member__results_frame = tk.Frame(root, height = win_h, width = win_w)

# report frame Main menu
top_text = tk.Label(Rep_frame, text='Select One Of The Options Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Book_Search_label = tk.Label(Rep_frame, text = "A member can perform a search \n on the collection of books.", fg = 'black')
Book_Search_label.place(x = 400, y = 50, anchor = "nw")
Book_Search_button = tk.Button(Rep_frame, text = "Book Search", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Book_search_frame))
Book_Search_button.place(x = 50, y = 50, anchor = "nw")

# display books on loan
game_scroll = Scrollbar(Book_on_Loan_frame)
game_scroll.pack(side=RIGHT, fill=Y)
game_scroll = Scrollbar(Book_on_Loan_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)
book_onloan_table = ttk.Treeview(Book_on_Loan_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
book_onloan_table.pack()
game_scroll.config(command=book_onloan_table.yview)
game_scroll.config(command=book_onloan_table.xview)
book_onloan_table['columns'] = ('book_AN', 'book_title', 'book_authors', 'book_ISBN', 'book_publisher','book_year')
book_onloan_table.column("#0", width=0,  stretch=YES)
book_onloan_table.column("book_AN",anchor=CENTER, width=150)
book_onloan_table.column("book_title",anchor=CENTER,width=150)
book_onloan_table.column("book_authors",anchor=CENTER,width=150)
book_onloan_table.column("book_ISBN",anchor=CENTER,width=150)
book_onloan_table.column("book_publisher",anchor=CENTER,width=150)
book_onloan_table.column("book_year",anchor=CENTER,width=150)
book_onloan_table.heading("#0",text="",anchor=CENTER)
book_onloan_table.heading("book_AN",text="Accession Number",anchor=CENTER)
book_onloan_table.heading("book_title",text="Title",anchor=CENTER)
book_onloan_table.heading("book_authors",text="Authors",anchor=CENTER)
book_onloan_table.heading("book_ISBN",text="ISBN",anchor=CENTER)
book_onloan_table.heading("book_publisher",text="Publisher",anchor=CENTER)
book_onloan_table.heading("book_year",text="Year",anchor=CENTER)

def return_book_onloan():
    book_list = get_book_on_loan()
    book_final=[]
    # for book_author in get_book_contains_author(Author_keyword):
    for book in book_list:
        author = get_Authors_report_loan(book.Accession_Number)
        title = get_book_title_based_on_AN(book.Accession_Number)
        ISBN = get_book_ISBN_based_on_AN(book.Accession_Number)
        publisher = get_book_publisher_based_on_AN(book.Accession_Number)
        year = get_book_year_based_on_AN(book.Accession_Number)
        book_infor = [book.Accession_Number, title,author, ISBN, publisher, year]
        book_final.append(book_infor)

    change_frame(Rep_frame, Book_on_Loan_frame)

    for book in book_final:
        book_onloan_table.insert(parent='',index='end',iid=0,text='', values=(book))
    book_onloan_table.pack()

Book_on_Loan_label = tk.Label(Rep_frame, text = "This function displays all the books \n currently on loan to members.", fg = 'black')
Book_on_Loan_label.place(x = 400, y = 120, anchor = "nw")
Book_on_Loan_button = tk.Button(Rep_frame, text = "Books on Loan", width=25, fg = 'black', command = return_book_onloan)
Book_on_Loan_button.place(x = 50, y = 120, anchor = "nw")

# display books on reservation
game_scroll = Scrollbar(Book_on_reservation_frame)
game_scroll.pack(side=RIGHT, fill=Y)
game_scroll = Scrollbar(Book_on_reservation_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)
book_onreserve_table = ttk.Treeview(Book_on_reservation_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
book_onreserve_table.pack()
game_scroll.config(command=book_onreserve_table.yview)
game_scroll.config(command=book_onreserve_table.xview)
book_onreserve_table['columns'] = ('book_AN', 'book_title', 'mem_id', 'mem_name')
book_onreserve_table.column("#0", width=0,  stretch=YES)
book_onreserve_table.column("book_AN",anchor=CENTER, width=150)
book_onreserve_table.column("book_title",anchor=CENTER,width=150)
book_onreserve_table.column("mem_id",anchor=CENTER,width=150)
book_onreserve_table.column("mem_name",anchor=CENTER,width=150)
book_onreserve_table.heading("#0",text="",anchor=CENTER)
book_onreserve_table.heading("book_AN",text="Accession Number",anchor=CENTER)
book_onreserve_table.heading("book_title",text="Title",anchor=CENTER)
book_onreserve_table.heading("mem_id",text="Membership ID",anchor=CENTER)
book_onreserve_table.heading("mem_name",text="Name",anchor=CENTER)

def return_book_onreservation():
    book_list = get_book_on_reserve()
    book_final=[]
    for book in book_list:
        title = get_book_title_based_on_AN(book.Accession_Number)
        member_id = book.memberid
        member_name = get_member_name_based_on_id(member_id)
        book_infor = [book.Accession_Number, title, member_id, member_name]
        book_final.append(book_infor)

    change_frame(Rep_frame, Book_on_reservation_frame)

    for book in book_final:
        book_onreserve_table.insert(parent='',index='end',iid=0,text='', values=(book))
    book_onreserve_table.pack()


Book_on_reservation_label = tk.Label(Rep_frame, text = "This function displays all the books \n that members have reserved.", fg = 'black')
Book_on_reservation_label.place(x = 400, y = 190, anchor = "nw")
Book_on_reservation_button = tk.Button(Rep_frame, text = "Books on Reservation", width=25, fg = 'black', command = return_book_onreservation)
Book_on_reservation_button.place(x = 50, y = 190, anchor = "nw")

# display members with outstanding fines
game_scroll = Scrollbar(Outstanding_Fines__frame)
game_scroll.pack(side=RIGHT, fill=Y)
game_scroll = Scrollbar(Outstanding_Fines__frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)
mem_with_fines_table = ttk.Treeview(Outstanding_Fines__frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
mem_with_fines_table.pack()
game_scroll.config(command=mem_with_fines_table.yview)
game_scroll.config(command=mem_with_fines_table.xview)
mem_with_fines_table['columns'] = ('mem_id', 'mem_name', 'mem_faculty', 'mem_ph', 'mem_email')
mem_with_fines_table.column("#0", width=0,  stretch=YES)
mem_with_fines_table.column("mem_id",anchor=CENTER, width=150)
mem_with_fines_table.column("mem_name",anchor=CENTER,width=150)
mem_with_fines_table.column("mem_faculty",anchor=CENTER,width=150)
mem_with_fines_table.column("mem_ph",anchor=CENTER,width=150)
mem_with_fines_table.column("mem_email",anchor=CENTER,width=150)
mem_with_fines_table.heading("#0",text="",anchor=CENTER)
mem_with_fines_table.heading("mem_id",text="Membership ID",anchor=CENTER)
mem_with_fines_table.heading("mem_name",text="Name",anchor=CENTER)
mem_with_fines_table.heading("mem_faculty",text="Faculty",anchor=CENTER)
mem_with_fines_table.heading("mem_ph",text="Phone Number",anchor=CENTER)
mem_with_fines_table.heading("mem_email",text="Email Address",anchor=CENTER)

def return_mem_with_fines():
    mem_list = get_mem_with_fines()
    mem_final=[]
    for mem in mem_list:
        mem_infor = [mem.memberid, mem.name, mem.faculty, mem.phone_number, mem.email_address]
        mem_final.append(mem_infor)

    change_frame(Rep_frame, Outstanding_Fines__frame)

    for mem in mem_final:
        mem_with_fines_table.insert(parent='',index='end',iid=0,text='', values=(mem))
    mem_with_fines_table.pack()

Outstanding_Fines__label = tk.Label(Rep_frame, text = "This function displays the \n outstanding fines for members.", fg = 'black')
Outstanding_Fines__label.place(x = 400, y = 260, anchor = "nw")
Outstanding_Fines__button = tk.Button(Rep_frame, text = "Outstanding Fines", width=25, fg = 'black', command = return_mem_with_fines)
Outstanding_Fines__button.place(x = 50, y = 260, anchor = "nw")

Books_on_Loan_to_Member__label = tk.Label(Rep_frame, text = "This function displays all the books a member \n identified by the membership ID has borrowed.", fg = 'black')
Books_on_Loan_to_Member__label.place(x = 400, y = 330, anchor = "nw")
Books_on_Loan_to_Member__button = tk.Button(Rep_frame, text = "Books on Loan to Member", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Books_on_Loan_to_Member__frame))
Books_on_Loan_to_Member__button.place(x = 50, y = 330, anchor = "nw")

Back_button = tk.Button(Rep_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Rep_frame, Root_frame))
Back_button.place(x = 300, y = 400, anchor = "nw")

# Book search frame
# display books on search
game_scroll = Scrollbar(Book_search_results_frame)
game_scroll.pack(side=RIGHT, fill=Y)
game_scroll = Scrollbar(Book_search_results_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)
book_search_table = ttk.Treeview(Book_search_results_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
book_search_table.pack()
game_scroll.config(command=book_search_table.yview)
game_scroll.config(command=book_search_table.xview)
book_search_table['columns'] = ('book_AN', 'book_title', 'book_authors', 'book_ISBN', 'book_publisher','book_year')
book_search_table.column("#0", width=0,  stretch=YES)
book_search_table.column("book_AN",anchor=CENTER, width=150)
book_search_table.column("book_title",anchor=CENTER,width=150)
book_search_table.column("book_authors",anchor=CENTER,width=150)
book_search_table.column("book_ISBN",anchor=CENTER,width=150)
book_search_table.column("book_publisher",anchor=CENTER,width=150)
book_search_table.column("book_year",anchor=CENTER,width=150)
book_search_table.heading("#0",text="",anchor=CENTER)
book_search_table.heading("book_AN",text="Accession Number",anchor=CENTER)
book_search_table.heading("book_title",text="Title",anchor=CENTER)
book_search_table.heading("book_authors",text="Authors",anchor=CENTER)
book_search_table.heading("book_ISBN",text="ISBN",anchor=CENTER)
book_search_table.heading("book_publisher",text="Publisher",anchor=CENTER)
book_search_table.heading("book_year",text="Year",anchor=CENTER)

def book_search_function():
    Title_keyword = Title_entry.get()
    Author_keyword = Author_entry.get()
    ISBN_keyword = ISBN_entry.get()
    Publisher_keyword = Publisher_entry.get()
    Year_keyword = Year_entry.get()
    book_final=[]
    book_list = get_book_contains(Title_keyword, ISBN_keyword, Publisher_keyword, Year_keyword)
    for book_author in get_book_contains_author(Author_keyword):
        for book in book_list:
            if book.Accession_Number == book_author.Accession_Number:
                book_infor = [book.Accession_Number, book.Title, book_author.Author, book.ISBN, book.Publisher, book.Year]
                book_final.append(book_infor)
    change_frame(Book_search_frame, Book_search_results_frame)
    for book in book_final:
        book_search_table.insert(parent='',index='end',iid=0,text='', values=(book))
    book_search_table.pack()
   
top_text = tk.Label(Book_search_frame, text='Select based on one of the categories below:', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Title_label = tk.Label(Book_search_frame, text='Title', fg = 'black')
Title_label.place(x = 50, y = 50, anchor = "nw")
Title_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
# Title_entry.insert(0, "Book Name")
Title_entry.place(x = 300, y = 50, anchor = "nw")

Author_label = tk.Label(Book_search_frame, text='Authors', fg = 'black')
Author_label.place(x = 50, y = 100, anchor = "nw")
Author_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
# Author_entry.insert(0, "There can be multiple authors for a book")
Author_entry.place(x = 300, y = 100, anchor = "nw")

ISBN_label = tk.Label(Book_search_frame, text='ISBN', fg = 'black')
ISBN_label.place(x = 50, y = 150, anchor = "nw")
ISBN_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
# ISBN_entry.insert(0, "ISBN Number")
ISBN_entry.place(x = 300, y = 150, anchor = "nw")

Publisher_label = tk.Label(Book_search_frame, text='Publisher', fg = 'black')
Publisher_label.place(x = 50, y = 200, anchor = "nw")
Publisher_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
# Publisher_entry.insert(0, "PRandom House, Penguin, Cengage, Springer, etc.")
Publisher_entry.place(x = 300, y = 200, anchor = "nw")

Year_label = tk.Label(Book_search_frame, text='Publication Year', fg = 'black')
Year_label.place(x = 50, y = 250, anchor = "nw")
Year_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
# Year_entry.insert(8, "Edition year")
Year_entry.place(x = 300, y = 250, anchor = "nw")

Search_book_buttom = tk.Button(Book_search_frame, text = "Search Book", width=20, height=1, command = book_search_function)
Search_book_buttom.place(x = 50, y = 300, anchor = "nw")

Back_to_Report_Main = tk.Button(Book_search_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Book_search_frame, Rep_frame))
Back_to_Report_Main.place(x = 700, y = 300, anchor = "nw")


#Book Search Results frame buttom
top_label = tk.Label(Book_search_results_frame, text='Book Search Results', bg='cyan')
top_label.pack(side=TOP)

Back_to_Search_Function = tk.Button(Book_search_results_frame, text = "Back To Search Function", width=20, height=1, command = lambda: change_frame_delete_infor(Book_search_results_frame, Book_search_frame, book_search_table))
# Back_to_Search_Function.place(x = 50, y = 400, anchor = "nw")
Back_to_Search_Function.pack(side=BOTTOM)

# Book on loan frame
top_text = tk.Label(Book_on_Loan_frame, text='Books on Loan Report', bg='cyan')
top_text.pack(side = TOP)

Back_to_Report_Main = tk.Button(Book_on_Loan_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame_delete_infor(Book_on_Loan_frame, Rep_frame, book_onloan_table))
Back_to_Report_Main.pack(side = BOTTOM)


# Book on reservation frame
top_text = tk.Label(Book_on_reservation_frame, text='Books on Reservation Report', bg='cyan')
top_text.pack(side = TOP)

Back_to_Report_Main = tk.Button(Book_on_reservation_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame_delete_infor(Book_on_reservation_frame, Rep_frame, book_onreserve_table))
Back_to_Report_Main.pack(side = BOTTOM)

# Outstanding Fines frame
top_text = tk.Label(Outstanding_Fines__frame, text='Members With Outstanding Fines', bg='cyan')
top_text.pack(side = TOP)

Back_to_Report_Main = tk.Button(Outstanding_Fines__frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame_delete_infor(Outstanding_Fines__frame, Rep_frame, mem_with_fines_table))
Back_to_Report_Main.pack(side = BOTTOM)

# Books on Loan to Member search frame
# books on loan to member table
# game_scroll = Scrollbar(Book_search_results_frame)
# game_scroll.pack(side=RIGHT, fill=Y)
# game_scroll = Scrollbar(Book_search_results_frame,orient='horizontal')
# game_scroll.pack(side= BOTTOM,fill=X)
book_loan_mem_table = ttk.Treeview(Books_on_Loan_to_Member__results_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)
book_loan_mem_table.pack()
# game_scroll.config(command=book_search_table.yview)
# game_scroll.config(command=book_search_table.xview)
book_loan_mem_table['columns'] = ('book_AN', 'book_title', 'book_authors', 'book_ISBN', 'book_publisher','book_year')
book_loan_mem_table.column("#0", width=0,  stretch=YES)
book_loan_mem_table.column("book_AN",anchor=CENTER, width=150)
book_loan_mem_table.column("book_title",anchor=CENTER,width=150)
book_loan_mem_table.column("book_authors",anchor=CENTER,width=150)
book_loan_mem_table.column("book_ISBN",anchor=CENTER,width=150)
book_loan_mem_table.column("book_publisher",anchor=CENTER,width=150)
book_loan_mem_table.column("book_year",anchor=CENTER,width=150)
book_loan_mem_table.heading("#0",text="",anchor=CENTER)
book_loan_mem_table.heading("book_AN",text="Accession Number",anchor=CENTER)
book_loan_mem_table.heading("book_title",text="Title",anchor=CENTER)
book_loan_mem_table.heading("book_authors",text="Authors",anchor=CENTER)
book_loan_mem_table.heading("book_ISBN",text="ISBN",anchor=CENTER)
book_loan_mem_table.heading("book_publisher",text="Publisher",anchor=CENTER)
book_loan_mem_table.heading("book_year",text="Year",anchor=CENTER)


top_text = tk.Label(Books_on_Loan_to_Member__frame, text='Books on Loan to Member', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

MemID_text = tk.Label(Books_on_Loan_to_Member__frame, text='Membership ID')
MemID_text.place(x = 50, y = 200, anchor = "nw")
MemID_entry = tk.Entry(Books_on_Loan_to_Member__frame, fg = 'black', width = 60)
# MemID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
MemID_entry.place(x = 300, y = 200, anchor = "nw")

def book_on_loan_mem_function():
    mem_id_keyword = MemID_entry.get()
    borrow_return_list_final=[]
    borrow_return_list = get_borrow_record_by_memid(mem_id_keyword)
    for infor in borrow_return_list:
        book = get_book(infor.Accession_Number)
        book_infor = [book.Accession_Number,  book.Title, get_Authors_report_loan(infor.Accession_Number), book.ISBN, book.Publisher, book.Year]
        borrow_return_list_final.append(book_infor)
    change_frame(Books_on_Loan_to_Member__frame, Books_on_Loan_to_Member__results_frame)
    for book in borrow_return_list_final:
        book_loan_mem_table.insert(parent='',index='end',iid=0,text='', values=(book))
    book_loan_mem_table.pack()


Search_mem = tk.Button(Books_on_Loan_to_Member__frame, text = "Search Member", fg = 'black', command = book_on_loan_mem_function)
Search_mem.place(x = 50, y = 350, anchor = "nw")
Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__frame, text = "Back to Reports Menu", fg = 'black', command = lambda: change_frame(Books_on_Loan_to_Member__frame, Rep_frame))
Back_to_Report_Main.place(x = 700, y = 350, anchor = "nw")

# Books on Loan to Member results frame
top_text = tk.Label(Books_on_Loan_to_Member__results_frame, text='Books on Loan to Member', bg='cyan')
top_text.pack(side = TOP)

Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__results_frame, text = "Back to search Menu", width=20, height=1, command = lambda: change_frame_delete_infor(Books_on_Loan_to_Member__results_frame, Books_on_Loan_to_Member__frame, book_loan_mem_table))
Back_to_Report_Main.pack(side = BOTTOM)

#xunuo ends
# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()

session.close()
conn.close()