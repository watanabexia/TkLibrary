import tkinter as tk
root = tk.Tk()
root.title('Reports Portal')
root.geometry('1000x1000')
root.option_add("*font", "SF\ Pro 14")

Report_frame = tk.Frame(root)
Report_create_frame = tk.Frame(root)
# Report_delete_frame = tk.Frame(root)
top_word = tk.Label(root, text='Select one of the option below:', 
bg='blue', font=('Arial', 12), width=30, height=2)

top_word.pack()

def Mem_to_Mem_create():
    Mem_frame.pack_forget()
    Mem_create_frame.pack()

Book_Search_button = tk.Button(Report_frame, text = "Book Search", fg = 'black', command = Mem_to_Mem_create)
Book_on_Loan_button = tk.Button(Report_frame, text = "Books on loan", fg = 'black')
Book_on_reservation_button = tk.Button(Report_frame, text = "Books on reservation", fg = 'black', command = Mem_to_Mem_create)
Outstanding_Fines__button = tk.Button(Report_frame, text = "Outstanding Fines", fg = 'black', command = Mem_to_Mem_create)
Books_on_Loan_to_Member__button = tk.Button(Report_frame, text = "Books on Loan to Member", fg = 'black', command = Mem_to_Mem_create)

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

Report_frame.pack()

if __name__ == "__main__":
    root.mainloop()