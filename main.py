import tkinter as tk

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
root.geometry('1000x1000')
root.option_add("*font", "SF\ Pro 14")

# Frame Definition
Root_frame = tk.Frame(root)
Mem_frame = tk.Frame(root)
Book_frame = tk.Frame(root)
Loan_frame = tk.Frame(root)
Res_frame = tk.Frame(root)
Fine_frame = tk.Frame(root)
Rep_frame = tk.Frame(root)

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

# Membership Frame
Mem_create_frame = tk.Frame(root)
Mem_delete_frame = tk.Frame(root)
Mem_update_frame = tk.Frame(root)

def Mem_to_Mem_create():
    Mem_frame.pack_forget()
    Mem_create_frame.pack() 

def Mem_to_Mem_delete():
    Mem_frame.pack_forget()
    Mem_delete_frame.pack()

def Mem_to_Mem_update():
    Mem_frame.pack_forget()
    Mem_update_frame.pack()


# Membership menu labels and buttons
top_word1 = tk.Label(Mem_frame, text='Select one of the Options below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word1.pack()

Mem_create_button = tk.Button(Mem_frame, text = "Membership Creation", fg = 'black', command = Mem_to_Mem_create)
Mem_delete_button = tk.Button(Mem_frame, text = "Membership Deletion", fg = 'black', command = Mem_to_Mem_delete)
Mem_update_button = tk.Button(Mem_frame, text = "Membership Update", fg = 'black', command = Mem_to_Mem_update)
Back_to_main_menu = tk.Button(Mem_frame, text = "Back To Main Menu ", fg = 'black', command = lambda: change_frame(Mem_frame, Root_frame))

Mem_create_button.pack()
Mem_delete_button.pack()
Mem_update_button.pack()
Back_to_main_menu.pack()

# Membership creation labels and buttons
top_word2 = tk.Label(Mem_create_frame, text='To Create Member, Please Enter Requested Information Below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word2.pack()
Mem_ID_label1 = tk.Label(Mem_create_frame, text = 'Membership ID', fg = 'black')
Mem_ID_label1.pack(side = tk.RIGHT, padx=10, pady=10)
Name_label = tk.Label(Mem_create_frame, text = 'Name', fg = 'black')
Name_label.pack(side = tk.RIGHT, padx=10, pady=20)
Faculty_label = tk.Label(Mem_create_frame, text = 'Faculty', fg = 'black')
Faculty_label.pack(side = tk.RIGHT, padx=10, pady=30)
Phone_number_label = tk.Label(Mem_create_frame, text = 'Phone Number', fg = 'black')
Phone_number_label.pack(side = tk.RIGHT, padx=10, pady=40)
Email_Address_label = tk.Label(Mem_create_frame, text = 'Email Address', fg = 'black')
Email_Address_label.pack(side = tk.RIGHT, padx=10, pady=50)


Back_to_membership_menu_button_C = tk.Button(Mem_create_frame, text = "Back To Membership Menu ", fg = 'black', command = lambda: change_frame(Mem_create_frame, Mem_frame))
Back_to_membership_menu_button_C.pack(side = tk.RIGHT, padx=10, pady=60)

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




