# Student-Management-System
A lightweight, desktop-based CRUD (Create, Read, Update, Delete) application built with Python using the tkinter library for the graphical interface and MySQL for data persistence.

# 🚀 Features

    Add Students: Register new students with their name, age, and major.

    View Records: Real-time display of student data in a structured table (Treeview).

    Update Info: Select a record from the table to modify student details.

    Delete & Re-sequence: Remove a student and automatically re-order the remaining IDs to maintain a clean sequence.

    Auto-fill: Clicking a record in the table automatically populates the input fields for quick editing. 

# 🛠️ Prerequisites

Before running the application, ensure you have the following installed:
    Python 3.x
    MySQL Server (e.g., XAMPP, WAMP, or a standalone MySQL installation)
    
    MySQL Connector for Python:
```
    pip install mysql-connector-python
```

# ⚙️ Setup Instructions
1. Database Configuration

First, create the database in your MySQL environment:
SQL
```
CREATE DATABASE student_db;
```
The application will automatically create the students table upon its first run.

2. Connection Settings

Open hello.py and update the get_db_connection() function with your MySQL credentials if they differ from the default:
```
    host: "localhost"

    user: "root"

    password: "" (Change if you have a password set) 
```

# 🖥️ Usage

     Run the application:
     bash
```
    python hello.py
```
    To Add: Enter the student's details and click ADD NEW.

    To Update: Click on a student in the table, change the text in the input boxes, and click UPDATE.

    To Delete: Select a student from the table and click DELETE. The system will prompt for confirmation and then re-sequence the IDs. 

# 📁 File Structure

    1. hello.py: The main Python script containing the GUI logic and database queries.

    2. mysql.connector: SQL script for database initialization.
