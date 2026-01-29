import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# --- Database Connection ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Change if you have a password
        database="student_db"
    )

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT,
                major VARCHAR(255)
            )
        """)
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# --- Functions ---

def show_data():
    """Refreshes the table with data from MySQL"""
    for row in tree.get_children():
        tree.delete(row)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

def add_student():
    name, age, major = entry_name.get(), entry_age.get(), entry_major.get()
    if not (name and age and major):
        messagebox.showwarning("Input Error", "All fields are required")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, major) VALUES (%s, %s, %s)", (name, age, major))
    conn.commit()
    conn.close()
    
    clear_entries()
    show_data()
    messagebox.showinfo("Success", "Student Added!")

def update_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a row from the table first")
        return

    # Get the ID of the selected row
    item = tree.item(selected)
    student_id = item['values'][0]

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE students SET name=%s, age=%s, major=%s WHERE id=%s"
    cursor.execute(query, (entry_name.get(), entry_age.get(), entry_major.get(), student_id))
    conn.commit()
    conn.close()
    
    show_data()
    messagebox.showinfo("Success", "Student Record Updated!")

def delete_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a row to delete")
        return
    
    item = tree.item(selected)
    student_id = item['values'][0]

    if messagebox.askyesno("Confirm", "Are you sure you want to delete this?"):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 1. Delete the student
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        
        # 2. Re-order the remaining IDs to be 1, 2, 3...
        # Note: This is a "hack" for small projects!
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE students SET id = (@count := @count + 1);")
        
        # 3. Reset the Auto-Increment counter so the next Add is the correct next number
        cursor.execute("ALTER TABLE students AUTO_INCREMENT = 1;")
        
        conn.commit()
        conn.close()
        
        show_data()
        clear_entries()
        messagebox.showinfo("Success", "Record deleted and IDs re-sequenced!")

def get_selected_row(event):
    """Fills the entry boxes when a row is clicked"""
    selected = tree.selection()
    if selected:
        item = tree.item(selected)['values']
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, item[1])
        entry_age.delete(0, tk.END)
        entry_age.insert(tk.END, item[2])
        entry_major.delete(0, tk.END)
        entry_major.insert(tk.END, item[3])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_major.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Student Database Manager")
root.geometry("700x500")

# Header
tk.Label(root, text="Student Management System", font=("Arial", 18, "bold")).pack(pady=10)

# Input Fields Frame
frame_in = tk.Frame(root)
frame_in.pack(pady=10)

tk.Label(frame_in, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame_in, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame_in, text="Age").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(frame_in, width=30)
entry_age.grid(row=1, column=1)

tk.Label(frame_in, text="Major").grid(row=2, column=0, padx=10, pady=5)
entry_major = tk.Entry(frame_in, width=30)
entry_major.grid(row=2, column=1)

# Buttons Frame
frame_btn = tk.Frame(root)
frame_btn.pack(pady=20)

tk.Button(frame_btn, text="ADD NEW", command=add_student, bg="#2ecc71", fg="white", width=12).pack(side=tk.LEFT, padx=5)
tk.Button(frame_btn, text="UPDATE", command=update_student, bg="#3498db", fg="white", width=12).pack(side=tk.LEFT, padx=5)
tk.Button(frame_btn, text="DELETE", command=delete_student, bg="#e74c3c", fg="white", width=12).pack(side=tk.LEFT, padx=5)
tk.Button(frame_btn, text="CLEAR", command=clear_entries, width=12).pack(side=tk.LEFT, padx=5)

# Table Section
tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Major"), show='headings')
tree.heading("ID", text="Student ID")
tree.heading("Name", text="Full Name")
tree.heading("Age", text="Age")
tree.heading("Major", text="Major")
tree.column("ID", width=100, anchor=tk.CENTER)
tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Bind the click event
tree.bind('<<TreeviewSelect>>', get_selected_row)

init_db()
show_data()
root.mainloop()