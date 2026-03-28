import sqlite3

conn = sqlite3.connect('Farm_Database.db')
cur = conn.cursor()

# ========================
# 1. Login
# ========================
sql_login = """
    CREATE TABLE IF NOT EXISTS login_user(
        login_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
"""
cur.execute(sql_login)

# ========================
# 2. KHU VUON
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS khu_vuon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_khu TEXT NOT NULL,
    mo_ta TEXT
)
""")
# ,
#     login_id INTEGER,
#     FOREIGN KEY (login_id) REFERENCES login_user(login_id) ON DELETE SET NULL

# ========================
# 3. LOAI NAM
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS loai_nam (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_nam TEXT NOT NULL,
    thoi_gian_sinh_truong INTEGER
)
""")

# ========================
# 4. LUONG NAM
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS luong_nam (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    khu_id INTEGER,
    loai_nam_id INTEGER,
    ngay_trong DATE,
    trang_thai TEXT DEFAULT 'dang_trong',
    FOREIGN KEY (khu_id) REFERENCES khu_vuon(id) ON DELETE CASCADE,
    FOREIGN KEY (loai_nam_id) REFERENCES loai_nam(id) ON DELETE CASCADE
)
""")

# ========================
# 5. DU LIEU CAM BIEN
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS du_lieu_cam_bien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    khu_id INTEGER,
    nhiet_do REAL,
    do_am REAL,
    anh_sang REAL,
    thoi_gian DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (khu_id) REFERENCES khu_vuon(id) ON DELETE CASCADE
)
""")

# ========================
# 6. LICH TUOI
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS lich_tuoi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    khu_id INTEGER,
    thoi_gian_tuoi DATETIME,
    trang_thai TEXT DEFAULT 'chua_tuoi',
    FOREIGN KEY (khu_id) REFERENCES khu_vuon(id) ON DELETE CASCADE
)
""")

# ========================
# 7. THU HOACH
# ========================
cur.execute("""
CREATE TABLE IF NOT EXISTS thu_hoach (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    luong_nam_id INTEGER,
    ngay_thu_hoach DATE,
    san_luong REAL,
    FOREIGN KEY (luong_nam_id) REFERENCES luong_nam(id) ON DELETE CASCADE
)
""")

# Lưu và đóng
conn.commit()
conn.close()

print("✅ Tạo database thành công!")