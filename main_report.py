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
top_text = tk.Label(Rep_frame, text='Select One Of The Options Below', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Book_Search_label = tk.Label(Rep_frame, text = "A member can perform a search \n on the collection of books.", fg = 'black')
Book_Search_label.place(x = 400, y = 50, anchor = "nw")
Book_Search_button = tk.Button(Rep_frame, text = "11. Book Search", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Book_search_frame))
Book_Search_button.place(x = 50, y = 50, anchor = "nw")

Book_on_Loan_label = tk.Label(Rep_frame, text = "This function displays all the books \n currently on loan to members.", fg = 'black')
Book_on_Loan_label.place(x = 400, y = 120, anchor = "nw")
Book_on_Loan_button = tk.Button(Rep_frame, text = "Books on Loan", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Book_on_Loan_frame))
Book_on_Loan_button.place(x = 50, y = 120, anchor = "nw")

Book_on_reservation_label = tk.Label(Rep_frame, text = "This function displays all the books \n that members have reserved.", fg = 'black')
Book_on_reservation_label.place(x = 400, y = 190, anchor = "nw")
Book_on_reservation_button = tk.Button(Rep_frame, text = "Books on Reservation", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Book_on_reservation_frame))
Book_on_reservation_button.place(x = 50, y = 190, anchor = "nw")

Outstanding_Fines__label = tk.Label(Rep_frame, text = "This function displays the \n outstanding fines for members.", fg = 'black')
Outstanding_Fines__label.place(x = 400, y = 260, anchor = "nw")
Outstanding_Fines__button = tk.Button(Rep_frame, text = "Outstanding Fines", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Outstanding_Fines__frame))
Outstanding_Fines__button.place(x = 50, y = 260, anchor = "nw")

Books_on_Loan_to_Member__label = tk.Label(Rep_frame, text = "This function displays all the books a member \n identified by the membership ID has borrowed.", fg = 'black')
Books_on_Loan_to_Member__label.place(x = 400, y = 330, anchor = "nw")
Books_on_Loan_to_Member__button = tk.Button(Rep_frame, text = "Books on Loan to Member", width=25, fg = 'black', command = lambda: change_frame(Rep_frame, Books_on_Loan_to_Member__frame))
Books_on_Loan_to_Member__button.place(x = 50, y = 330, anchor = "nw")

Back_button = tk.Button(Rep_frame, text = "Back To Main Menu", fg = 'black', command = lambda: change_frame(Rep_frame, Root_frame))
Back_button.place(x = 300, y = 400, anchor = "nw")

# Book search frame
top_text = tk.Label(Book_search_frame, text='Select based on one of the categories below:', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Title_label = tk.Label(Book_search_frame, text='Title', fg = 'black')
Title_label.place(x = 50, y = 50, anchor = "nw")
Title_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
Title_entry.insert(0, "Book Name")
Title_entry.place(x = 300, y = 50, anchor = "nw")

Author_label = tk.Label(Book_search_frame, text='Authors', fg = 'black')
Author_label.place(x = 50, y = 100, anchor = "nw")
Author_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
Author_entry.insert(0, "There can be multiple authors for a book")
Author_entry.place(x = 300, y = 100, anchor = "nw")

ISBN_label = tk.Label(Book_search_frame, text='ISBN', fg = 'black')
ISBN_label.place(x = 50, y = 150, anchor = "nw")
ISBN_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
ISBN_entry.insert(0, "ISBN Number")
ISBN_entry.place(x = 300, y = 150, anchor = "nw")

Publisher_label = tk.Label(Book_search_frame, text='Publisher', fg = 'black')
Publisher_label.place(x = 50, y = 200, anchor = "nw")
Publisher_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
Publisher_entry.insert(0, "PRandom House, Penguin, Cengage, Springer, etc.")
Publisher_entry.place(x = 300, y = 200, anchor = "nw")

Year_label = tk.Label(Book_search_frame, text='Publication Year', fg = 'black')
Year_label.place(x = 50, y = 250, anchor = "nw")
Year_entry = tk.Entry(Book_search_frame, fg = 'black', width = 60)
Year_entry.insert(0, "Edition year")
Year_entry.place(x = 300, y = 250, anchor = "nw")

Search_book_buttom = tk.Button(Book_search_frame, text = "Search Book", width=20, height=1, command = lambda: change_frame(Book_search_frame, Book_search_results_frame))
Search_book_buttom.place(x = 50, y = 300, anchor = "nw")

Back_to_Report_Main = tk.Button(Book_search_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Book_search_frame, Rep_frame))
Back_to_Report_Main.place(x = 700, y = 300, anchor = "nw")

#Book Search Results frame
# top word
top_text = tk.Label(Book_search_results_frame, text='Book Search Results', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Back_to_Search_Function = tk.Button(Book_search_results_frame, text = "Back To Search Function", width=20, height=1, command = lambda: change_frame(Book_search_results_frame, Book_search_frame))
Back_to_Search_Function.place(x = 50, y = 100, anchor = "nw")

# Book on loan frame
top_text = tk.Label(Book_on_Loan_frame, text='Books on Loan Report', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Back_to_Report_Main = tk.Button(Book_on_Loan_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Book_on_Loan_frame, Rep_frame))
Back_to_Report_Main.place(x = 50, y = 100, anchor = "nw")

# Book on reservation frame
top_text = tk.Label(Book_on_reservation_frame, text='Books on Reservation Report', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Back_to_Report_Main = tk.Button(Book_on_reservation_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Book_on_reservation_frame, Rep_frame))
Back_to_Report_Main.place(x = 50, y = 100, anchor = "nw")


# Outstanding Fines frame
top_text = tk.Label(Outstanding_Fines__frame, text='Members With Outstanding Fines', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Back_to_Report_Main = tk.Button(Outstanding_Fines__frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Outstanding_Fines__frame, Rep_frame))
Back_to_Report_Main.place(x = 50, y = 100, anchor = "nw")


# Books on Loan to Member search frame
top_text = tk.Label(Books_on_Loan_to_Member__frame, text='Books on Loan to Member', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

MemID_text = tk.Label(Books_on_Loan_to_Member__frame, text='Membership ID')
MemID_text.place(x = 50, y = 200, anchor = "nw")
MemID_entry = tk.Entry(Books_on_Loan_to_Member__frame, fg = 'black', width = 60)
MemID_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
MemID_entry.place(x = 300, y = 200, anchor = "nw")

Search_mem = tk.Button(Books_on_Loan_to_Member__frame, text = "Search Member", fg = 'black', command = lambda: change_frame(Books_on_Loan_to_Member__frame, Books_on_Loan_to_Member__results_frame))
Search_mem.place(x = 50, y = 350, anchor = "nw")
Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__frame, text = "Back to Reports Menu", fg = 'black', command = lambda: change_frame(Books_on_Loan_to_Member__frame, Rep_frame))
Back_to_Report_Main.place(x = 700, y = 350, anchor = "nw")

# Books on Loan to Member results frame
top_text = tk.Label(Books_on_Loan_to_Member__results_frame, text='Books on Loan to Member', bg='cyan')
top_text.place(x = 50, y = 0, anchor = "nw")

Back_to_Report_Main = tk.Button(Books_on_Loan_to_Member__results_frame, text = "Back to Reports Menu", width=20, height=1, command = lambda: change_frame(Books_on_Loan_to_Member__results_frame, Rep_frame))
Back_to_Report_Main.place(x = 50, y = 100, anchor = "nw")

# Root Frame Application
Root_frame.pack()
if __name__ == "__main__":
    root.mainloop()

    