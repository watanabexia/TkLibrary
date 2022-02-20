import tkinter as tk
import tkinter.messagebox 


# from venv import create
# from sqlalchemy import Column, String, create_engine, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # Database Schema Definition
# Base = declarative_base()
# class Book(Base):
#     __tablename__ = 'Book'
#     Accession_Number = Column(String(3), primary_key = True)
#     Title = Column(String(57))
#     Authors = Column(String(28))
#     FIELD4 = Column(String(16))
#     FIELD5 = Column(String(8))
#     ISBN = Column(String(13))
#     Publisher = Column(String(32))
#     Year = Column(Integer)

# # Database Connection Initialization
# engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/BT2102-AS1')
# DBSession = sessionmaker(bind = engine)

# # session = DBSession()

# # book = session.query(Book).all()

# # print(book[0].Title)

# # session.close()

# UI Initialization
root = tk.Tk()
root.title('ALS')

win_w = 1000
win_h = 1000

root.geometry(str(win_w) + "x" + str(win_h))
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
    tkinter.messagebox.showinfo(title='Success!', message='ALS Membership Created')

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




# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()




