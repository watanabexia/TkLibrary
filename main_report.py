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

# report frame
Rep_frame = tk.Frame(root)

#frames in the report frame
Book_search_frame = tk.Frame(root)
Book_on_Loan_frame = tk.Frame(root)
Book_on_reservation_frame = tk.Frame(root)
Outstanding_Fines__frame = tk.Frame(root)
Books_on_Loan_to_Member__frame = tk.Frame(root)

# Report_delete_frame = tk.Frame(root)
top_word = tk.Label(root, text='Select one of the option below:', 
bg='blue', font=('Arial', 12), width=30, height=2)

top_word.pack()

Book_Search_button = tk.Button(Rep_frame, text = "Book Search", fg = 'black', command = lambda: change_frame(Rep_frame, Book_search_frame))
Book_on_Loan_button = tk.Button(Rep_frame, text = "Books on loan", fg = 'black', command = lambda: change_frame(Rep_frame, Book_on_Loan_frame) )
Book_on_reservation_button = tk.Button(Rep_frame, text = "Books on reservation", fg = 'black', command = lambda: change_frame(Rep_frame, Book_on_reservation_frame))
Outstanding_Fines__button = tk.Button(Rep_frame, text = "Outstanding Fines", fg = 'black', command = lambda: change_frame(Rep_frame, Outstanding_Fines__frame))
Books_on_Loan_to_Member__button = tk.Button(Rep_frame, text = "Books on Loan to Member", fg = 'black', command = lambda: change_frame(Rep_frame, Books_on_Loan_to_Member__frame))

Book_Search_button.pack()
Book_on_Loan_button.pack()
Book_on_reservation_button.pack()
Outstanding_Fines__button.pack()
Books_on_Loan_to_Member__button.pack()
'''
Mem_ID_label = tk.Label(Mem_create_frame, text='Membership ID', fg = 'black')
Mem_ID_label.pack()
Name_label = tk.Label(Mem_create_frame, text='Name', fg = 'black')
Name_label.pack()
Faculty_label = tk.Label(Mem_create_frame, text='Faculty', fg = 'black')
Faculty_label.pack()'''

# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()