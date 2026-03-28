from flask import render_template
import random
from .mushroom import mushroom_bp, get_db_connection

@mushroom_bp.route('/api/sensor/<int:id>')
def get_sensor_view(id):
    # 1. Random dữ liệu
    nhiet_do = round(random.uniform(22.0, 32.0), 1)
    do_am = round(random.uniform(60.0, 90.0), 1)
    anh_sang = round(random.uniform(100.0, 600.0), 1)

    conn = get_db_connection()
    cur = conn.cursor()
    sensor_data = None
    
    try:
        # 2. Lưu vào bảng du_lieu_cam_bien
        cur.execute("""
            INSERT INTO du_lieu_cam_bien (khu_id, nhiet_do, do_am, anh_sang)
            VALUES (?, ?, ?, ?)
        """, (id, nhiet_do, do_am, anh_sang))
        conn.commit()
        
        # 3. Lấy bản ghi vừa mới chèn xong
        cur.execute("""
            SELECT * FROM du_lieu_cam_bien 
            WHERE khu_id = ? 
            ORDER BY thoi_gian DESC LIMIT 1
        """, (id,))
        sensor_data = cur.fetchone()
    except Exception as e:
        print(f"Lỗi DB: {e}")
    finally:
        conn.close()

    return render_template('data_env.html', sensor=sensor_data)