# Demo Web IoT – Flask Blueprint + SQLite

Ứng dụng web mô phỏng quản lý hệ thống IoT đơn giản, bao gồm: đăng ký / đăng nhập, hiển thị dữ liệu cảm biến, và CRUD dữ liệu Farm – Boards.  
Dự án áp dụng **Flask Blueprint** để tách module rõ ràng, dễ mở rộng và bảo trì.

---

## 🚀 Tính năng chính

### 🔐 Authentication
- Đăng ký tài khoản (có nhập lại mật khẩu)
- Đăng nhập + lưu session
- Chặn truy cập nếu chưa login

### 📊 IoT Dashboard
- Hiển thị dữ liệu cảm biến mẫu (nhiệt độ, độ ẩm, bụi)
- Mô phỏng giao diện điều khiển thiết bị

### 📝 CRUD (Farm / Boards)
- Thêm – Xóa – Sửa – Xem chi tiết dữ liệu
- Kết nối backend bằng REST API
- Template riêng cho từng module

### 🧩 Kiến trúc Blueprint
- `Auths/` – xử lý đăng ký, đăng nhập  
- `Boards/` – hiển thị & quản lý board  
- `Farms/` – CRUD farm  
- Mỗi Blueprint có **templates** và **static** riêng

---

## 🛠️ Công nghệ sử dụng

| Công nghệ | Mục đích |
|----------|----------|
| **Python 3.x** | Ngôn ngữ chính |
| **Flask** | Web framework |
| **Flask Blueprint** | Tổ chức module |
| **SQLite3** | Cơ sở dữ liệu |
| **HTML – CSS – JS** | Giao diện |
| **Bootstrap** | Tối ưu UI |
| **Fetch API** | Kết nối frontend – backend |

---

## 📁 Cấu trúc dự án

```
CRUD_Web_HDH/
│── app.py
│── database.db
│── initDB_login.py
│── requirements.txt
│
├── Blueprints/
│   ├── Auths/
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── auth_templates/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── static/auth.css
│   │
│   ├── Boards/
│   │   ├── board.py
│   │   ├── board_templates/list_farm.html
│   │   └── static/board.js
│   │
│   └── Farms/
│       ├── farm.py
│       ├── farm_templates/farm.html
│       └── static/...
│
└── Web_env/ (virtual environment)
```



---

## ▶️ Cách chạy dự án

### 1. Clone dự án:

bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

### 2. Tạo môi trường ảo:
python -m venv venv

### 3. Kích hoạt env:
Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

### 4. Cài thư viện:
pip install -r requirements.txt

### 5. Chạy ứng dụng:
python app.py

Mặc định chạy tại:
[http://127.0.0.1:2004/](http://192.168.1.6:2004/)

#### 📸 Ảnh giao diện:
<img width="1915" height="907" alt="Screenshot 2025-11-19 175642" src="https://github.com/user-attachments/assets/f4308cc0-54c1-4fa9-8f8b-eb2be6380b4a" />

<img width="1912" height="898" alt="Screenshot 2025-11-19 175703" src="https://github.com/user-attachments/assets/a5e186ef-560d-42a8-8adb-2a1127bcd5bf" />

<img width="1914" height="903" alt="Screenshot 2025-11-19 175738" src="https://github.com/user-attachments/assets/2aa0d852-b9cf-499e-b2bf-b6d17e17b10b" />


## Khi chọn 1 farm:
<img width="1910" height="910" alt="Screenshot 2025-11-19 175805" src="https://github.com/user-attachments/assets/205d7048-c3c6-4699-a0e6-b5c5f543607f" />

<img width="1916" height="915" alt="Screenshot 2025-11-19 175821" src="https://github.com/user-attachments/assets/ca6e3780-5478-43cc-b0ee-0d3f65b5da75" />

### 6. Tắt ứng dụng:
deactivate
