import mysql.connector
conn=mysql.connector.connect(
 host="localhost",
 user="root",
 password="Uma@1234567890",
 database="users",
 autocommit=False
)
cursor=conn.cursor()
# cursor.execute("""
# create table user(name varchar(100),
#                password varchar(100))
#                """)
# query="insert into user(name,password) values(%s,%s)"
# data=[("uma","uma@12345678"),
# ("sourav","sourav@1238907"),
# ("Tyson","tn@567890"),
# ("Harry","hry@4567890"),
# ("lucy","lucy@135790")]
# cursor.executemany(query,data)
# attempts=3
# while attempts>0:
#     name=input("enter your name")
#     password=input("enter your password")
#     query="select * from user where name=%s and password=%s"
#     cursor.execute(query,(name,password))
#     result=cursor.fetchone()
#     if result:
#         print("User found")
#         break
#     else:
#         attempts -= 1
#         print("Wrong password. Attempts left:", attempts)
# conn.commit()
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("simple form")
root.geometry("500x500")
attempts=3
def user_details():
    global attempts
    user_name=user_entry.get()
    user_password=password_entry.get()
    query="select * from user where name=%s and password=%s"
    cursor.execute(query,(user_name,user_password))
    result=cursor.fetchone()
    print(result)
    if result:
        messagebox.showinfo("Success", "User found!")
    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Warning", f"Wrong password! Attempts left: {attempts}")
        else:
            messagebox.showerror("Error", "No attempts left! Access blocked.")
            root.destroy()
user_name = tk.Label(root, text="User Name:", font=("Times New Roman", 15))
user_name.grid(row=0, column=0, pady=20)

user_entry = tk.Entry(root, font=("Times New Roman", 15))
user_entry.grid(row=0, column=1)

user_password = tk.Label(root, text="Password:", font=("Times New Roman", 15))
user_password.grid(row=1, column=0, pady=20)

password_entry = tk.Entry(root, font=("Times New Roman", 15), show='*')
password_entry.grid(row=1, column=1)

button=tk.Button(root,text='click me',command=user_details)
button.grid(row=2,column=1,pady=20)

root.mainloop()
