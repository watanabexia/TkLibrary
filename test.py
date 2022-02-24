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

#Book frame object
Acq_frame = tk.Frame(root)
Withd_frame = tk.Frame(root)
top_text = tk.Label(Book_frame, text='Select One Of The Options Below', bg='cyan', width=30, height=2, font=('Helvatical bold',20))
top_text.pack()
Acq_button = tk.Button(Book_frame, text = "4. Book Acquisition", fg = 'black', height = 10, width = 20, command = lambda: change_frame(Book_frame, Acq_frame))
Acq_button.pack()
Withd_button = tk.Button(Book_frame, text = "5. Book Withdrawal", fg = 'black',height = 10, width = 20, command = lambda: change_frame(Book_frame, Withd_frame))
Withd_button.pack()
Back_button = tk.Button(Book_frame, text = "Back To Main Menu", fg = 'black', height = 2, width = 50, command = lambda: change_frame(Book_frame, Root_frame))
Back_button.pack()

#Book Acquisition object

def add_new_book():
    tkinter.messagebox.showinfo(title='Success!', message='New Book Added In Library!')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Already Added; Duplicate, Missing or Incomplete fields')

top_text = tk.Label(Acq_frame, text='For New Book Acquisition, Please Enter Information Below', bg='cyan', width=50, height=2, font=('Helvatical bold',20))
top_text.pack()
AN_text = tk.Label(Acq_frame, text='Accession Number', width=20, height=1, font=('Arial',14)).place(x=100,y=53)
AN_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
Title_text = tk.Label(Acq_frame, text='Title', width=10, height=1, font=('Arial',14)).place(x=180,y=76)
Title_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
Author_text = tk.Label(Acq_frame, text='Author', width=10, height=1, font=('Arial',14)).place(x=180,y=99)
Author_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
ISBN_text = tk.Label(Acq_frame, text='ISBN', width=10, height=1, font=('Arial',14)).place(x=180,y=122)
ISBN_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
Publisher_text = tk.Label(Acq_frame, text='Publisher', width=15, height=1, font=('Arial',14)).place(x=165,y=145)
Publisher_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
Year_text = tk.Label(Acq_frame, text='Year', width=10, height=1, font=('Arial',14)).place(x=180,y=168)
Year_entry = tk.Entry(Acq_frame, show=None, font=('Arial', 10)).pack()
Add_new_book_button = tk.Button(Acq_frame, text = "Add New Book", fg = 'black', height = 2, width = 15, command = add_new_book).place(x=0,y=150)
Back_to_book_button = tk.Button(Acq_frame, text = "Back To Book", fg = 'black', height = 2, width = 15, command = lambda: change_frame(Acq_frame, Book_frame)).place(x=500,y=150)

#Book Withdrawal object
def withdraw_book():
    tkinter.messagebox.askyesno(title='Please Confirm The Details Are Correct', message='New Book Added In Library!')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Is Currently On Loan.')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Is Currently Reserved.')
top_text = tk.Label(Withd_frame, text='To Remove Outdated Books From System, Please Enter Information Below', bg='cyan', width=50, height=2, font=('Helvatical bold',20)).pack()
AN_text = tk.Label(Withd_frame, text='Accession Number', width=20, height=1, font=('Arial',14)).place(x=100,y=90)
Empty_text = tk.Label(Withd_frame, text='', width=20, height=2).pack()
AN_entry = tk.Entry(Withd_frame, show=None, font=('Arial', 10)).pack()
Empty_text = tk.Label(Withd_frame, text='', width=20, height=5).pack()
Withdraw_button = tk.Button(Withd_frame, text = "Withdraw Book", fg = 'black', height = 2, width = 15, command = withdraw_book).place(x=0,y=150)
Back_to_book_button = tk.Button(Withd_frame, text = "Back To Book", fg = 'black', height = 2, width = 15, command = lambda: change_frame(Withd_frame, Book_frame)).place(x=500,y=150)

#Loan frame object
Borrow_frame = tk.Frame(root)
Return_frame = tk.Frame(root)
top_text = tk.Label(Loan_frame, text='Select One Of The Options Below', bg='cyan', width=30, height=2, font=('Helvatical bold',20)).pack()
Borrow_button = tk.Button(Loan_frame, text = "6. Borrow", fg = 'black', height = 10, width = 20, command = lambda: change_frame(Loan_frame, Borrow_frame)).pack()
Return_button = tk.Button(Loan_frame, text = "7. Return", fg = 'black',height = 10, width = 20, command = lambda: change_frame(Loan_frame, Return_frame)).pack()
Back_button = tk.Button(Loan_frame, text = "Back To Main Menu", fg = 'black', height = 2, width = 50, command = lambda: change_frame(Loan_frame, Root_frame)).pack()

#Borrow object
def borrow_book():
    tkinter.messagebox.askyesno(title='Please Confirm The Loan Details To Be Correct', message='New Book Added In Library!')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Currently On Loan Until.')
    # tkinter.messagebox.showinfo(title='Error!', message='Member Loan Quota Exceeded.')
    # tkinter.messagebox.showinfo(title='Error!', message='Member Has Outstanding Fines.')

top_text = tk.Label(Borrow_frame, text='To Borrow A Book , Please Enter Information Below', bg='cyan', width=50, height=2, font=('Helvatical bold',20)).pack()
AN_text = tk.Label(Borrow_frame, text='Accession Number', width=20, height=1, font=('Arial',14)).place(x=110,y=55)
ID_text = tk.Label(Borrow_frame, text='Membership ID', width=20, height=1, font=('Arial',14)).place(x=110,y=75)
AN_entry = tk.Entry(Borrow_frame, show=None, font=('Arial', 10)).pack()
ID_entry = tk.Entry(Borrow_frame, show=None, font=('Arial', 10)).pack()
Empty_text = tk.Label(Borrow_frame, text='', width=20, height=5).pack()
Borrow_button = tk.Button(Borrow_frame, text = "Borrow Book", fg = 'black', height = 2, width = 15, command = borrow_book).place(x=0,y=150)
Back_to_Loan_button = tk.Button(Borrow_frame, text = "Back To Loans", fg = 'black', height = 2, width = 15, command = lambda: change_frame(Borrow_frame, Loan_frame)).place(x=500,y=150)


#Return object
def return_book():
    tkinter.messagebox.askyesno(title='Please Confirm The Return Details To Be Correct', message='New Book Added In Library!')
    # tkinter.messagebox.showinfo(title='Success!', message='Book Returned Successfully.')
    # tkinter.messagebox.showinfo(title='Error!', message='Book Returned Successfully. But Has Fines')

top_text = tk.Label(Return_frame, text='To Return A Book , Please Enter Information Below', bg='cyan', width=50, height=2, font=('Helvatical bold',20)).pack()
AN_text = tk.Label(Return_frame, text='Accession Number', width=20, height=1, font=('Arial',14)).place(x=110,y=55)
ID_text = tk.Label(Return_frame, text='Membership ID', width=20, height=1, font=('Arial',14)).place(x=110,y=75)
AN_entry = tk.Entry(Return_frame, show=None, font=('Arial', 10)).pack()
ID_entry = tk.Entry(Return_frame, show=None, font=('Arial', 10)).pack()
Empty_text = tk.Label(Return_frame, text='', width=20, height=5).pack()
Borrow_button = tk.Button(Return_frame, text = "Return Book", fg = 'black', height = 2, width = 15, command = return_book).place(x=0,y=150)
Back_to_Loan_button = tk.Button(Return_frame, text = "Back To Loans", fg = 'black', height = 2, width = 15, command = lambda: change_frame(Return_frame, Loan_frame)).place(x=500,y=150)









# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()