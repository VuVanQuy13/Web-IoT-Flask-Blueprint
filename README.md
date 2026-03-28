# 📦 Web IoT Flask Blueprint

## 📌 Introduction

This project is a web application built using **Flask (Python)** with the **Blueprint architecture** to manage an IoT system.

It provides a modular and scalable structure, making it easy to extend and maintain.

---

## 🏗️ Project Structure

```
Web-IoT-Flask-Blueprint/
│── app.py
│── requirements.txt
│── initDB_login.py
│
├── Blueprints/
│   ├── Auths/
│   │   ├── login.py
│   │   ├── register.py
│   │
│   ├── Garden/
│   │   ├── garden.py
│   │
│   ├── Mushroom/
│       ├── mushroom.py
│
├── templates/
├── static/
```

---

## ⚙️ Technologies Used

* Python
* Flask
* Flask Blueprint
* HTML / CSS / JavaScript
* SQLite (or local database)

---

## 🚀 How to Run the Project

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd Web-IoT-Flask-Blueprint
```

---

### 2. Virtual Environment (Recommended)

* Windows:

```bash
\Web_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Initialize Database

```bash
python initDB_login.py
```

---

### 5. Run the Server

```bash
python app.py
```

---

### 6. Open in Browser

```
http://localhost:2004
```

---

## 🔑 Features

### 🔐 Authentication

* User registration
* User login
* Basic authentication system

---

### 🌱 Garden Management

* Manage garden data
* Display garden list

---

### 🍄 Mushroom Management

* Manage mushroom data
* Track status and information

---

### 🧩 Modular Architecture (Blueprint)

* `Auths` → Authentication module
* `Garden` → Garden management
* `Mushroom` → Mushroom management

Easy to extend with new modules.

---

## 🌐 Main Routes

| Route       | Description         |
| ----------- | ------------------- |
| `/`         | Redirect to login   |
| `/login`    | Login page          |
| `/register` | Register page       |
| `/garden`   | Garden management   |
| `/mushroom` | Mushroom management |

---

## 🧠 Future Improvements

* Integrate real IoT devices (ESP32, sensors)
* Real-time dashboard
* WebSocket / MQTT support
* Role-based access control (Admin/User)
* Deploy to cloud (Render, Railway, VPS)

---

## ❗ Notes

* Default port: `2004`
* Secret key is hardcoded → change before deployment
* Debug mode is enabled (`debug=True`) → disable in production

---

## 👨‍💻 Author

* VuVanQuy
