from re import X
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

# report frame
Rep_frame = tk.Frame(root, height = win_h, width = win_w)

#other frames in the report frame
Book_search_frame = tk.Frame(root, height = win_h, width = win_w)
Book_search_results_frame = tk.Frame(root, height = win_h, width = win_w)
Book_on_Loan_frame = tk.Frame(root, height = win_h, width = win_w)
Book_on_reservation_frame = tk.Frame(root, height = win_h, width = win_w)
Outstanding_Fines__frame = tk.Frame(root, height = win_h, width = win_w)
Books_on_Loan_to_Member__frame = tk.Frame(root, height = win_h, width = win_w)
Books_on_Loan_to_Member__results_frame = tk.Frame(root, height = win_h, width = win_w)

# report frame Main menu
# top word 
top_word = tk.Label(Rep_frame, text='Select one of the Options below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# buttoms on the report frame
Book_Search_button = tk.Button(Rep_frame, text = "11. Book Search", fg = 'black', width=25, height=2, command = lambda: change_frame(Rep_frame, Book_search_frame))
Book_on_Loan_button = tk.Button(Rep_frame, text = "12. Books on Loan", fg = 'black', width=25, height=2, command = lambda: change_frame(Rep_frame, Book_on_Loan_frame) )
Book_on_reservation_button = tk.Button(Rep_frame, text = "13. Books on Reservation", fg = 'black', width=25, height=2, command = lambda: change_frame(Rep_frame, Book_on_reservation_frame))
Outstanding_Fines__button = tk.Button(Rep_frame, text = "14. Outstanding Fines", fg = 'black', width=25, height=2, command = lambda: change_frame(Rep_frame, Outstanding_Fines__frame))
Books_on_Loan_to_Member__button = tk.Button(Rep_frame, text = "15. Books on Loan to Member", fg = 'black', width=25, height=2, command = lambda: change_frame(Rep_frame, Books_on_Loan_to_Member__frame))

Book_Search_button.pack()
Book_Search_label = tk.Label(Rep_frame, text = "A member can perform a search \n on the collection of books.", fg = 'black')
Book_Search_label.pack()

Book_on_Loan_button.pack()
Book_on_Loan_label = tk.Label(Rep_frame, text = "This function displays all the books \n currently on loan to members.", fg = 'black')
Book_on_Loan_label.pack()

Book_on_reservation_button.pack()
Book_on_reservation_label = tk.Label(Rep_frame, text = "This function displays all the books \n taht members have reserved.", fg = 'black')
Book_on_reservation_label.pack()

Outstanding_Fines__button.pack()
Outstanding_Fines__label = tk.Label(Rep_frame, text = "This function displays the outstanding fines \n for members.", fg = 'black')
Outstanding_Fines__label.pack()

Books_on_Loan_to_Member__button.pack()
Books_on_Loan_to_Member__label = tk.Label(Rep_frame, text = "This function displays all the books a member \n identified by the membership ID has borrowed.", fg = 'black')
Books_on_Loan_to_Member__label.pack()


# bottom buttom
Back_to_Main = tk.Button(Rep_frame, text = "Back to Main Menu", 
bg = 'red' , fg = 'white', width=15, height=1, command = lambda: change_frame(Rep_frame, Root_frame))
Back_to_Main.pack(side = tk.BOTTOM, padx=20, pady=20)

# Book search frame
# top word 
top_word = tk.Label(Book_search_frame, text='Select based on one of the categories below:', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# category buttoms
Title_text = tk.Label(Book_search_frame, text='Title', width=20, height=1, font=('Arial',15))
Title_entry = tk.Entry(Book_search_frame, show=None, width = 50, font=('Arial', 12))
Title_entry.insert(0, "Book Name")

Author_text = tk.Label(Book_search_frame, text='Authors', width=20, height=1, font=('Arial',15))
Author_entry = tk.Entry(Book_search_frame, show=None, width = 50, font=('Arial', 12))
Author_entry.insert(0, "There can be multiple authors for a book")

ISBN_text = tk.Label(Book_search_frame, text='ISBN', width=20, height=1, font=('Arial',15))
ISBN_entry = tk.Entry(Book_search_frame, show=None, width = 50, font=('Arial', 12))
ISBN_entry.insert(0, "ISBN Number")

Publisher_text = tk.Label(Book_search_frame, text='Publisher', width=20, height=1, font=('Arial',15))
Publisher_entry = tk.Entry(Book_search_frame, show=None, width = 50, font=('Arial', 12))
Publisher_entry.insert(0, "Random House, Penguin, Cengage, Springer, etc.")

PublishYear_text = tk.Label(Book_search_frame, text='Publication Year', width=20, height=1, font=('Arial',15))
PublishYear_entry = tk.Entry(Book_search_frame, show=None, width = 50, font=('Arial', 12))
PublishYear_entry.insert(0, "Edition year")

Title_text.pack()
Title_entry.pack()
Author_text.pack()
Author_entry.pack()
ISBN_text.pack()
ISBN_entry.pack()
Publisher_text.pack()
Publisher_entry.pack()
PublishYear_text.pack()
PublishYear_entry.pack()

# search book buttom
Search_book = tk.Button(Book_search_frame, text = "Search Book", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Book_search_frame, Book_search_results_frame))
Search_book.pack(side = tk.LEFT, padx=20, pady=20)

# back to report menu buttom
Back_to_Report_Main = tk.Button(Book_search_frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Book_search_frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.RIGHT, padx=20, pady=20)

#Book Search Results frame
# top word
top_word = tk.Label(Book_search_results_frame, text='Book Search Results', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# back to search function
Back_to_Search_Function = tk.Button(Book_search_results_frame, text = "Back To Search Function", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Book_search_results_frame, Book_search_frame))
Back_to_Search_Function.pack(side = tk.BOTTOM, padx=20, pady=20)

# Book on loan frame
# top word
top_word = tk.Label(Book_on_Loan_frame, text='Books on Loan Report', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# back to report menu buttom
Back_to_Report_Main = tk.Button(Book_on_Loan_frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Book_on_Loan_frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.BOTTOM, padx=20, pady=20)


# Book on reservation frame
# top word
top_word = tk.Label(Book_on_reservation_frame, text='Books on Reservation Report', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# back to report menu buttom
Back_to_Report_Main = tk.Button(Book_on_reservation_frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Book_on_reservation_frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.BOTTOM, padx=20, pady=20)


# Outstanding Fines frame
# top word
top_word = tk.Label(Outstanding_Fines__frame, text='Members With Outstanding Fines', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# back to report menu buttom
Back_to_Report_Main = tk.Button(Outstanding_Fines__frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Outstanding_Fines__frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.BOTTOM, padx=20, pady=20)


# Books on Loan to Member search frame
# top word
top_word = tk.Label(Books_on_Loan_to_Member__frame, text='Books on Loan to Member', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# membership ID search
MemID_text = tk.Label(Books_on_Loan_to_Member__frame, text='Membership ID', width=20, height=1, font=('Arial',15))
MemID_entry = tk.Entry(Books_on_Loan_to_Member__frame, show=None, width = 60, font=('Arial', 13))
MemID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
MemID_text.pack()
MemID_entry.pack()


#seach member buttom
Search_mem = tk.Button(Books_on_Loan_to_Member__frame, text = "Search Member", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Books_on_Loan_to_Member__frame, Books_on_Loan_to_Member__results_frame))
Search_mem.pack(side = tk.LEFT, padx=20, pady=20)

# back to report menu buttom
Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Books_on_Loan_to_Member__frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.RIGHT, padx=20, pady=20)

# Books on Loan to Member results frame
# top word
top_word = tk.Label(Books_on_Loan_to_Member__results_frame, text='Books on Loan to Member', 
bg='blue', fg = 'white', font=('Arial', 12), width=50, height=2)
top_word.pack()

# back to report menu buttom
Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__results_frame, text = "Back to Reports Menu", 
bg = 'red' , fg = 'white', width=20, height=1, command = lambda: change_frame(Books_on_Loan_to_Member__results_frame, Rep_frame))
Back_to_Report_Main.pack(side = tk.BOTTOM, padx=20, pady=20)

# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()