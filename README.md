# Tooter

Tooter is a social media platform built with Python and Flask, where users can write posts, view posts from other users, and interact within a secure environment. 
The app incorporates essential security features such as strong password confirmation, hashed database entries, and input validation to protect user data and prevent malicious attacks.

<br>

## 📋 <a name="table">Table of Contents</a>

1. ⚙️ [Tech Stack](#tech-stack)
2. 🔋 [Features](#features)
3. 🤸 [Installation](#installation)

<br>

## <a name="tech-stack">⚙️ Tech Stack</a>

- Python
- Flask
- HTML
- SQLAlchemy
- Bootstrap

<br>

## <a name="features">🔋 Features</a>

👉 **User Authentication**: Secure login and registration system with strong password validation and hashing.

👉 **Post Creation and Viewing**: Users can create posts and view posts from other users. Users can also delete their posts and their entire account from the database.

👉 **Security Features**:

  - **Strong Password Confirmation**: Ensures passwords meet complexity requirements.
  
  - **Hashed Database Entries**: All sensitive information, including passwords, is securely hashed using industry-standard algorithms.
  
  - **Escaping User Inputs**: User inputs are sanitized to prevent SQL injection and XSS attacks.

<br>

## <a name="installation">🤸 Installation</a>

Follow these steps to set up the project locally on your machine.

<br>

**Prerequisites**

Make sure you have the following installed on your machine:
- Git
- Python3
- pip

<br>

**Cloning the Repository**

```bash
git clone [https://github.com/hanselzheng/Tooter.git]
cd Tooter
```

<br>

**Installation**

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

Create .env file containing your own secret key:

```bash
SECRET_KEY='your_own_secret_key'
```

<br>

**Running the Project**

```bash
run the main.py file
```

<br>

Open [http://localhost:3000](http://localhost:3000) in your browser to view the project.
