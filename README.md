# Question Paper Review System

A web-based academic evaluation platform built with Django that streamlines the entire answer-sheet review process. Professors can manage exams and upload evaluated scripts, Teaching Assistants can assist with grading tasks, and students can access their results, review answer scripts, and submit re-evaluation queries through a role-based interface.

**User Roles:** Admin • Professor • Teaching Assistant (TA) • Student

---

## Contents

* Requirements
* Installation Guide
* Launching the Application
* Demo Accounts
* Default Login Credentials
* Role-wise Functionalities
* Project Layout
* Database Setup
* Importing Marks via CSV
* Troubleshooting

---

# Requirements

Before running the project, make sure the following software is installed:

| Software        | Requirement                      |
| --------------- | -------------------------------- |
| Python          | Version 3.10 or above            |
| MySQL / MariaDB | Running locally on port **3306** |
| pip             | Installed with Python            |
| Git             | Required to clone the repository |

---

# Installation Guide

## 1. Start the MySQL Service

### macOS

```bash
brew services start mysql
```

### Linux

```bash
sudo systemctl start mysql
```

### Windows

```powershell
net start MySQL80
```

> Depending on your installation, the service may be named **MySQL**, **MySQL80**, or **MariaDB**.

---

## 2. Create the Database

```bash
mysql -u root -e "CREATE DATABASE IF NOT EXISTS question_paper_review;"
```

If your root account is password protected:

```bash
mysql -u root -p
```

and create the database manually.

---

## 3. Clone the Repository

```bash
git clone https://github.com/pushpendras0026/Question_paper_review_system.git
cd Question_paper_review_system
```

---

## 4. Create a Virtual Environment

### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

Command Prompt:

```powershell
python -m venv venv
venv\Scripts\activate.bat
```

PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

If PowerShell blocks execution:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

A successful activation displays `(venv)` before the command prompt.

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Populate Sample Data

```bash
python manage.py seed_data
```

This command creates sample professors, students, TAs, courses, enrollments, and an administrator account for testing.

If you prefer creating your own administrator:

```bash
python manage.py createsuperuser
```

---

# Launching the Application

Whenever you want to run the project:

### 1. Start MySQL

```bash
brew services start mysql
```

or

```bash
sudo systemctl start mysql
```

Windows:

```powershell
net start MySQL80
```

---

### 2. Activate the Virtual Environment

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate.bat
```

---

### 3. Start Django Server

```bash
python manage.py runserver
```

---

### 4. Open the Application

```
http://127.0.0.1:8000/
```

or

```
http://localhost:8000/
```

To run on another port:

```bash
python manage.py runserver 8080
```

---

# Demo Accounts

The seeded database includes the following users. Every account uses the password:

```
pass
```

| Username | Role               |
| -------- | ------------------ |
| admin1   | Administrator      |
| prof1    | Professor          |
| prof2    | Professor          |
| prof3    | Professor          |
| student1 | Student            |
| student2 | Student            |
| ta1      | Teaching Assistant |
| ta2      | Teaching Assistant |

Each user is automatically redirected to the appropriate dashboard after login.

---

# Default Credentials for Newly Created Users

When an administrator creates users through the dashboard, passwords are generated automatically.

| User Type | Default Password | Backup Password |
| --------- | ---------------- | --------------- |
| Professor | Faculty ID       | `password123!`  |
| Student   | Roll Number      | `password`      |
| TA        | Roll Number      | `password`      |

Users can update their password anytime using the **Change Password** option after signing in.

---

# Features

## Administrator

* Manage courses and departments
* Register professors, students, and TAs
* Archive completed courses
* View overall course grades
* Notify professors about pending grade submissions

## Professor

* Manage current and archived courses
* Create exams with custom weightage and query periods
* Define section-wise marking schemes
* Upload evaluated answer sheets
* Enter marks manually or import them from CSV files
* Approve enrollment requests
* Act as faculty advisor for course approvals
* Assign and manage TAs with permission controls
* Respond to student queries
* Publish final grades

## Teaching Assistant

* Access assigned courses
* Upload answer sheets when authorized
* Modify marks if permission is granted
* Handle student queries
* Upload marks in bulk using CSV

## Student

* Browse available courses
* Request enrollment
* Access answer scripts and marks
* Submit review queries during the allowed period
* View statistics such as average, median, and percentile
* Check completed course history

---

# Project Structure

```
Question_paper_review_system/
│
├── manage.py
├── requirements.txt
├── QuestionReviewSystem/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── core/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    ├── management/
    │   └── commands/
    │       └── seed_data.py
    └── templates/
        └── core/
            ├── base.html
            ├── login.html
            ├── change_password.html
            ├── admin/
            ├── professor/
            ├── student/
            └── ta/
```

---

# Database Configuration

The application uses MySQL as its backend. Configure the database in:

```
QuestionReviewSystem/settings.py
```

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "question_paper_review",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

If your MySQL account has a password, update the `PASSWORD` field before running migrations.

---

# CSV Marks Upload

Professors and authorized TAs can upload marks in bulk through CSV files.

### Supported Features

* Header row is optional.
* Accepts delimiters such as comma, semicolon, pipe, or tab.
* Students can be identified using roll number, username, or full name.
* Marks column is automatically detected using headers like:

  * `marks`
  * `score`
  * `total`
  * `totalscore`

### Sample File

```csv
Roll Number,Student Name,Marks
220101001,Student1,78.5
220101002,Student2,91
```

### Validation Rules

* Marks must lie between **0** and the exam's maximum marks.
* Invalid or unmatched records are skipped automatically.
* Existing marks are updated instead of creating duplicate entries.

---

# Troubleshooting

* Verify that the MySQL service is running before starting the application.
* Ensure the database credentials in `settings.py` are correct.
* Activate the virtual environment before executing Django commands.
* If dependencies are missing, reinstall them using:

```bash
pip install -r requirements.txt
```

* Apply pending migrations if database errors occur:

```bash
python manage.py makemigrations
python manage.py migrate
```
