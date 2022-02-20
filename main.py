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
Mem_update_frame = tk.Frame(root, height = win_h, width = win_w)

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
Mem_update_button = tk.Button(Mem_frame, text = "Update A Member", fg = 'black', command = lambda: change_frame(Mem_frame, Mem_update_frame))
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
Name_entry.insert(0, "Enter member’s name")
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
top_word3 = tk.Label(Mem_delete_frame, text='To Delete Member, Please Enter Membership ID:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word3.pack()
Mem_ID_label2 = tk.Label(Mem_delete_frame, text = 'Membership ID', fg = 'black')
Mem_ID_label2.pack()

Back_to_membership_menu_button_D = tk.Button(Mem_delete_frame, text = "Back To Membership Menu ", fg = 'black', command = lambda: change_frame(Mem_delete_frame, Mem_frame))
Back_to_membership_menu_button_D.pack()

# Membership update labels and buttons
top_word4 = tk.Label(Mem_update_frame, text='To Update a Member, Please Enter Membership ID:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word4.pack()
Mem_ID_label3 = tk.Label(Mem_update_frame, text = 'Membership ID', fg = 'black')
Mem_ID_label3.pack()

Back_to_membership_menu_button_U = tk.Button(Mem_update_frame, text = "Back To Membership Menu ", fg = 'black', command = lambda: change_frame(Mem_update_frame, Mem_frame))
Back_to_membership_menu_button_U.pack()


# Fine Frame

Fine_frame = tk.Frame(root)
Fine_payment_frame = tk.Frame(root)

def Fine_to_Fine_payment():
    Fine_frame.pack_forget()
    Fine_payment_frame.pack() 

# Fine menu labels and buttons
top_word5 = tk.Label(Fine_frame, text='Select one of the Options below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word5.pack()

Fine_payment_button = tk.Button(Fine_frame, text = "Fine Payment", fg = 'black', command = Fine_to_Fine_payment)
Fine_payment_button.pack()
Back_to_main_menu1 = tk.Button(Fine_frame, text = "Back To Main Menu ", fg = 'black', command = lambda: change_frame(Fine_frame, Root_frame))
Back_to_main_menu1.pack()

# Fine payment labels and buttons
top_word6 = tk.Label(Fine_payment_frame, text='To Pay a Fine, Please Enter Information Below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word6.pack()
Mem_ID_label4 = tk.Label(Fine_payment_frame, text = 'Membership ID', fg = 'black')
Mem_ID_label4.pack()
Payment_date = tk.Label(Fine_payment_frame, text = 'Payment Date', fg = 'black')
Payment_date.pack()
Payment_amount = tk.Label(Fine_payment_frame, text = 'Payment Amount', fg = 'black')
Payment_amount.pack()
Back_to_Fine_menu = tk.Button(Fine_payment_frame, text = "Back To Fine Menu ", fg = 'black', command = lambda: change_frame(Fine_payment_frame, Fine_frame))
Back_to_Fine_menu.pack()






# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()




