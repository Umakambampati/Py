import tkinter as tk
import csv
from tkinter import filedialog,messagebox
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Uma@1234567890",
        database="college",
        autocommit=False
    )
    print(conn.is_connected())
    cursor=conn.cursor()
except mysql.connector.Error as e:
    messagebox.showerror("Database Connection Error", str(e))
    exit()

def csv_file_upload():
    filename=filedialog.askopenfilename(filetypes=[('CSV FILES','*.csv')])
    try:
        with open(filename,'r') as f:
            data=csv.reader(f)
        try:
            next(data)
        except StopIteration:
            messagebox.showwarning("CSV Warning", "CSV file is empty")
            return
        for row in data:
            try:
                cursor.execute('''
                Insert into stu(name,age,grade) values(%s, %s, %s)
                            ''',(row))
            except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", f"Error inserting row {row}: {e}")
        conn.commit()
        messagebox.showinfo('Succes',"Data has been inserted")
    except FileNotFoundError:
        messagebox.showerror("File Error","File not found")
    except csv.Error as e:
        messagebox.showerror("CSV Error", str(e))


def show_grid():
    try:
        grid.configure(state=tk.NORMAL)
        grid.delete('1.0', tk.END)
        cursor.execute('SELECT * FROM stu')
        for row in cursor.fetchall():
            grid.insert(tk.END, f'id:{row[0]},name:{row[1]},age:{row[2]},grade:{row[3]}\n')
        grid.configure(state=tk.DISABLED)
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))


def add_record():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    try:
        if not name or not age or not grade:
            raise ValueError("All fields are required")
        if not age.isdigit():
            raise ValueError("Age must be a number")
        cursor.execute(
            "INSERT INTO stu(name, age, grade) VALUES (%s, %s, %s)",
            (name, age, grade)
        )
        conn.commit()
        messagebox.showinfo("INFO", "Record added successfully")
        show_grid()

    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))

    except mysql.connector.Error as db_err:
        conn.rollback()
        messagebox.showerror("Database Error", str(db_err))

def edit_record():
    record_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    try:
        if not record_id:
            raise ValueError("ID is required to update a record")

        if not record_id.isdigit():
            raise ValueError("ID must be a number")

        if not name and not age and not grade:
            raise ValueError("Enter at least one field to update")

        if age and not age.isdigit():
            raise ValueError("Age must be a number")

        updated = False
        if name:
            cursor.execute("UPDATE stu SET name=%s WHERE id=%s", (name, record_id))
            updated = True

        if age:
            cursor.execute("UPDATE stu SET age=%s WHERE id=%s", (age, record_id))
            updated = True

        if grade:
            cursor.execute("UPDATE stu SET grade=%s WHERE id=%s", (grade, record_id))
            updated = True

        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with this ID")
        elif updated:
            messagebox.showinfo("Success", "Record updated successfully")

        show_grid()

    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))

    except mysql.connector.Error as db_err:
        conn.rollback()
        messagebox.showerror("Database Error", str(db_err))
def delete_record():
    record_id = id_entry.get()

    try:
        if not record_id:
            raise ValueError("ID is required to delete a record")
        if not record_id.isdigit():
            raise ValueError("ID must be a number")

        cursor.execute("DELETE FROM stu WHERE id=%s", (record_id,))
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with this ID")
        else:
            messagebox.showinfo("Success", "Record deleted successfully")

        show_grid()

    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))
    except mysql.connector.Error as db_err:
        conn.rollback()
        messagebox.showerror("Database Error", str(db_err))


root=tk.Tk()
root.geometry('500x500')

tk.Button(root,text="upload CSV", command=csv_file_upload).pack()
grid=tk.Text(root,height=20,width=100)
grid.pack(pady=10)

frame=tk.Frame(root)
frame.pack()

id_label=tk.Label(frame,text='ID').grid(row=0, column=0)
id_entry=tk.Entry(frame,width=4)
id_entry.grid(row=0,column=1)

name_label=tk.Label(frame,text='NAME').grid(row=0, column=2)
name_entry=tk.Entry(frame,width=15)
name_entry.grid(row=0,column=3,padx=5)

age_label=tk.Label(frame,text='AGE').grid(row=0, column=4)
age_entry=tk.Entry(frame,width=8)
age_entry.grid(row=0,column=5,padx=5)

grade_label=tk.Label(frame,text='GRADE').grid(row=0, column=6)
grade_entry=tk.Entry(frame,width=8)
grade_entry.grid(row=0,column=7,padx=5)

button=tk.Button(frame,text="ADD", command=add_record).grid(row=1,column=2,padx=5,pady=8)
tk.Button(frame,text="EDIT", command=edit_record).grid(row=1,column=3,pady=8)
tk.Button(frame,text="DELETE", command=delete_record).grid(row=1,column=4,padx=5,pady=8)



show_grid()
root.mainloop()
