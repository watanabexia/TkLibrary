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

root = tk.Tk()
root.title('Library Portal')
root.geometry('1000x1000')
root.option_add("*font", "SF\ Pro 14")

Mem_frame = tk.Frame(root)
Mem_create_frame = tk.Frame(root)
Mem_delete_frame = tk.Frame(root)

def Mem_to_Mem_create():
    Mem_frame.pack_forget()
    Mem_create_frame.pack() 

Mem_create_button = tk.Button(Mem_frame, text = "Membership Creation", fg = 'black', command = Mem_to_Mem_create)
Mem_delete_button = tk.Button(Mem_frame, text = "Membership Deletion", fg = 'black')
Mem_create_button.pack()
Mem_delete_button.pack()

Mem_ID_label = tk.Label(Mem_create_frame, text='Membership ID', fg = 'black')
Mem_ID_label.pack()
Name_label = tk.Label(Mem_create_frame, text='Name', fg = 'black')
Name_label.pack()
Faculty_label = tk.Label(Mem_create_frame, text='Faculty', fg = 'black')
Faculty_label.pack()

Mem_frame.pack()

if __name__ == "__main__":
    root.mainloop()

