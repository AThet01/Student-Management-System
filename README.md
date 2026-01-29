# 🎓 Student Management System

A lightweight, desktop-based CRUD (Create, Read, Update, Delete) application. This tool leverages Python's Tkinter library for a streamlined graphical interface and MySQL for robust data persistence.

# 🚀 Key Features

    Add Students: Register new records with name, age, and major details.

    View Records: Real-time display of student data in a structured, sortable Treeview table.

    Update Info: Select any record from the table to modify student details instantly.

    Delete & Re-sequence: Remove records with a built-in "hack" to re-order remaining IDs and reset the auto-increment counter for a clean sequence.

    Smart Auto-fill: Clicking a record in the table automatically populates input fields for rapid editing.

# 🛠️ Prerequisites

Ensure you have the following installed on your local environment:

   1. Python 3.x
   2. MySQL Server (XAMPP, WAMP, or standalone MySQL installation)

MySQL Connector for Python:
```
pip install mysql-connector-python
```

# ⚙️ Setup Instructions
1. Database Configuration

Create the database in your MySQL environment. The application handles table creation (students) automatically on its first run.
SQL
```
CREATE DATABASE student_db;
```
2. Connection Settings

If your MySQL configuration differs from the defaults, update the get_db_connection() function in hello.py:

    Host: localhost

    User: root

    Password: "" (Enter your password if applicable)

# 🖥️ Usage

1. Run the application:
```
python hello.py
```
2. To Add: Enter the student's details and click ADD NEW.

3. To Update: Click on a student in the table, change the text in the input boxes, and click UPDATE.

4. To Delete: Select a student from the table and click DELETE. The system will prompt for confirmation and then re-sequence the IDs.

# 📁 File Structure
1. hello.py -> Main script containing the Tkinter GUI logic and SQL queries.
2. mysql.connector -> SQL initialization script for database setup.
