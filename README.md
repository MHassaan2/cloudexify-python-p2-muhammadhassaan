# 🎓 Student Grade Management System

## 👨‍💻 Student Information

**Name:** Muhammad Hassaan  
**Registration Number:** CX-INT-2026-PY-0277

---

# 📖 Project Overview

The **Student Grade Management System** is a Python console-based application developed as part of the **CloudExify Python Internship (Project 2)**. The system helps manage student academic records by allowing users to add, view, search, update, and delete student information. It also calculates averages automatically, assigns letter grades, generates class rankings, and stores data permanently using CSV files.

The project demonstrates the practical implementation of Python fundamentals such as functions, nested dictionaries, file handling, exception handling, sorting, and CSV operations.

---

# ✨ Features Implemented

## ✅ Core Features

- ➕ Add Student
- 👀 View All Students
- 🔍 Search Student by ID
- ✏️ Update Student Information
- ❌ Delete Student Record
- 🆔 Automatic Student ID Generation
- ✔️ Grade Validation (0–100)
- 🚫 Duplicate Student Name Validation
- 🧮 Automatic Average Calculation
- 📊 Class Report & Ranking
- 💾 Save Student Records to CSV
- 📂 Load Student Records from CSV
- 🔄 Automatic Data Saving
- ⚠️ Exception Handling
- 📋 Formatted Table Output

## 🌟 Bonus Features

- 🏆 Letter Grade System (A, B, C, D, F)
- 💾 Automatic CSV Saving after Data Modification

---

# 🛠 Python Concepts Used

- ⚙️ Functions
- 📚 List of Dictionaries
- 🗂 Nested Dictionaries
- 📑 Dictionary `.items()`
- ➕ `sum()` and `len()`
- 🔢 `sorted()` with `key`
- 🔗 `zip()`
- 🔢 `enumerate()`
- 📄 CSV File Handling
- 📁 File Handling
- ⚠️ Exception Handling
- ✂️ String `.strip()`
- 📝 Advanced F-Strings

---

# 💻 Sample Output

## 📌 Main Menu

```text
---------------------------------------
Student Grade Management System
---------------------------------------
1. Add Student
2. View Students
3. Class Report & Ranking
4. Search Student
5. Update Student
6. Delete Student
7. Exit
---------------------------------------
```

## 📋 Student Records

```text
----------------------------------------------------------------------------------------------------
ID   Name              Maths Physics Computer Urdu English Average Grade
----------------------------------------------------------------------------------------------------
1    Ali               90     85      80       75    95      85.00   B
2    Ahmed             95     90      88       80    92      89.00   B
----------------------------------------------------------------------------------------------------
```

---

# ⚡ Challenges Faced and Solutions

### 🧩 1. Designing the Data Structure

The biggest challenge was organizing student information efficiently. This was solved by using a **list of nested dictionaries**, allowing each student to store multiple subject grades in a structured format.

### ✅ 2. Input Validation

Handling invalid user input required careful validation. This was implemented using **while loops** and **try-except** blocks to ensure only valid data is accepted.

### 📄 3. CSV File Handling

Saving and loading nested data from CSV files was initially challenging. The issue was solved using Python's built-in **csv** module to read and write structured data correctly.

### 🔄 4. Updating Student Records

Updating grades while keeping the average accurate required recalculating the average whenever grades were modified.

### 📊 5. Table Formatting

Displaying student records in a clean and readable table was achieved using **advanced formatted f-strings** with proper column alignment.

---

# 📝 Brief Report

## ❓ What was the hardest part to implement?

The most challenging part of this project was implementing the **update functionality** and managing **nested dictionaries** while ensuring that grades, averages, and CSV data remained consistent after every modification.

## 🚀 What would you add if given more time?

If given more time, I would extend this project by adding:

- 🎯 GPA calculation
- 📈 Subject-wise class average
- 📄 Individual student report cards
- 🗓 Attendance management
- 📚 Custom subjects instead of fixed subjects
- 🖥 Graphical User Interface (GUI) using Tkinter or PyQt

---

# 📁 Project Structure

```text
Student Grade Management System/
│
├── student_grade_management.py
├── students.csv
├── screenshots/
└── README.md
```

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/MHassaan2/cloudexify-python-p2-muhammadhassaan.git
```

Move to the project directory:

```bash
cd cloudexify-python-p2-muhammadhassaan
```

Run the application:

```bash
python student_grade_management.py
```

---

# 📸 Screenshots

Application screenshots are available in the **screenshots** folder.

---

# 👤 Author

**Muhammad Hassaan**  
BS Software Engineering  
International Islamic University Islamabad (IIUI)

---

# 📜 License

This project was developed for educational and internship purposes.
