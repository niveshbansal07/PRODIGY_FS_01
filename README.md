# Flask Authentication System 🔐

This project is a **full-stack authentication system** developed using **Flask, MySQL, and modern frontend UI**.  
It is created as part of an **internship project (Prodigy)** to demonstrate real-world backend development skills.

The application includes secure **user registration, login, session handling**, and animated success/error pages.

---
![Preview](https://github.com/niveshbansal07/PRODIGY_FS_01/blob/main/Signup%20Page%20-%20Brave%2012_18_2025%203_29_23%20PM.png)
![Preview](https://github.com/niveshbansal07/PRODIGY_FS_01/blob/main/Signup%20Page%20-%20Brave%2012_18_2025%203_29_32%20PM.png)
![Preview](https://github.com/niveshbansal07/PRODIGY_FS_01/blob/main/Signup%20Page%20-%20Brave%2012_18_2025%203_29_52%20PM.png)

## 🚀 Features

- User Signup & Login system
- Password hashing using **bcrypt**
- Secure session management
- MySQL database integration
- Environment variable support using `.env`
- Clean project structure
- Fully responsive UI with animations
- Separate success and error pages
- Protected dashboard route
- Logout functionality

---

## 🛠 Tech Stack

**Frontend**
- HTML5
- CSS3 (animations & responsive design)
- JavaScript

**Backend**
- Python (Flask)
- MySQL
- bcrypt (password hashing)
- Flask Sessions

**Other Tools**
- python-dotenv
- MySQL Connector

---

## 📁 Project Structure

```
FIRST/
│
├── config/
│ └── config.py
│
├── static/
│ └── css/
│ └── style.css
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ ├── success.html
│ └── error.html
│
├── .env
├── app.py
├── requirements.txt
└── venv/
```


---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```SECRET_KEY=your_secret_key_here```

⚠️ Make sure `.env` is added to `.gitignore`

---

## 🗄 Database Structure (MySQL)

```
CREATE TABLE user_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash TEXT
);
```

## ⚙ Installation & Setup

1. Clone Repository
```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```

4. Configure Database
```
Update config/config.py with your MySQL credentials.
```
▶ Run the Application
```
python app.py
```


Open browser:

http://127.0.0.1:5000

## 🧠 What I Learned:
- Flask project structuring
- Secure password hashing
- Session-based authentication
- MySQL CRUD operations
- Environment variable security
- Connecting frontend UI with backend logic
- Writing clean and maintainable code

## 📌 Internship Note
This project was developed as part of my internship at Prodigy, focusing on backend development, authentication systems, and full-stack integration.

## 📬 Contact
Nivesh Bansal
Aspiring Full Stack Developer
📧 Email: niveshbansal52@gmail.com
🔗 Portfolio: [Portfolio-link](https://nivesh-bansal.vercel.app/)
