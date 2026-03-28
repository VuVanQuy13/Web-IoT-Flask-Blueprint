from flask import render_template, request, jsonify
from .mushroom import mushroom_bp, get_db_connection

# 1. API Render nội dung cho Tab (Dùng cho loadTab trong JS)
@mushroom_bp.route('/api/quantity/<int:id>')
def get_quantity(id):
    conn = get_db_connection()
    # loai_nam để hiển thị gợi ý datalist và chu kỳ mặc định
    loai_nam = conn.execute("SELECT * FROM loai_nam").fetchall()

    # luong_nam: Lấy nấm ĐANG TRỒNG (JOIN thêm thoi_gian_sinh_truong)
    luong_nam = conn.execute("""
        SELECT ln.*, l.ten_nam, l.thoi_gian_sinh_truong 
        FROM luong_nam ln
        JOIN loai_nam l ON ln.loai_nam_id = l.id
        WHERE ln.khu_id = ? AND ln.trang_thai = 'dang_trong'
        ORDER BY ln.id DESC
    """, (id,)).fetchall()

    # thu_hoach: Lấy lịch sử thu hoạch (JOIN 3 bảng để lấy tên nấm)
    thu_hoach = conn.execute("""
        SELECT th.id, th.luong_nam_id, th.ngay_thu_hoach, th.san_luong, l.ten_nam 
        FROM thu_hoach th
        JOIN luong_nam ln ON th.luong_nam_id = ln.id
        JOIN loai_nam l ON ln.loai_nam_id = l.id
        WHERE ln.khu_id = ?
        ORDER BY th.id DESC
    """, (id,)).fetchall()

    conn.close()
    return render_template("number_mush.html", 
                           loai_nam=loai_nam, 
                           luong_nam=luong_nam, 
                           thu_hoach=thu_hoach, 
                           garden_id=id)

# 2. API Xử lý thêm nấm mới (Cập nhật lưu thời gian sinh trưởng)
@mushroom_bp.route('/api/add_mushroom/<int:id>', methods=['POST'])
def add_mushroom(id):
    data = request.get_json()
    ten_nam = data.get('ten_nam')
    date = data.get('date')
    tg_sinh_truong = data.get('tg_sinh_truong') # Lấy chu kỳ sinh trưởng từ JS

    if not ten_nam or not date or not tg_sinh_truong:
        return jsonify({"status": "error", "message": "Vui lòng nhập đầy đủ thông tin"}), 400

    conn = get_db_connection()
    try:
        # Kiểm tra xem loại nấm đã có trong database chưa
        row = conn.execute("SELECT id FROM loai_nam WHERE ten_nam = ?", (ten_nam,)).fetchone()
        
        if row:
            loai_id = row['id']
            # Cập nhật lại chu kỳ sinh trưởng nếu người dùng nhập số mới
            conn.execute("UPDATE loai_nam SET thoi_gian_sinh_truong = ? WHERE id = ?", (tg_sinh_truong, loai_id))
        else:
            # Nếu chưa có loại nấm này, thêm mới vào bảng loai_nam kèm chu kỳ
            cur = conn.execute("INSERT INTO loai_nam (ten_nam, thoi_gian_sinh_truong) VALUES (?, ?)", 
                               (ten_nam, tg_sinh_truong))
            loai_id = cur.lastrowid

        # Thêm vào bảng luong_nam (đại diện cho một lô trồng cụ thể)
        conn.execute("""
            INSERT INTO luong_nam (khu_id, loai_nam_id, ngay_trong, trang_thai)
            VALUES (?, ?, ?, 'dang_trong')
        """, (id, loai_id, date))
        
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        conn.close()

# 3. API Xử lý Thu hoạch (Giữ nguyên logic cũ)
@mushroom_bp.route('/api/harvest/<int:id>', methods=['POST'])
def harvest(id):
    data = request.get_json()
    kg = data.get('kg')

    if not kg:
        return jsonify({"status": "error", "message": "Thiếu sản lượng"}), 400

    conn = get_db_connection()
    try:
        # id ở đây là ID của LÔ NẤM (luong_nam_id)
        conn.execute("""
            INSERT INTO thu_hoach (luong_nam_id, ngay_thu_hoach, san_luong)
            VALUES (?, DATE('now'), ?)
        """, (id, kg))

        conn.execute("UPDATE luong_nam SET trang_thai = 'da_thu_hoach' WHERE id = ?", (id,))
        
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        conn.close()