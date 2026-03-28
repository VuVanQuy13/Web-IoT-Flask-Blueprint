from flask import render_template, request, jsonify
from .mushroom import mushroom_bp, get_db_connection

# LOAD VIEW
@mushroom_bp.route('/api/schedule/<int:id>')
def get_schedule_view(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lich_tuoi WHERE khu_id = ? ORDER BY id DESC", (id,))
    schedules = cur.fetchall()
    conn.close()
    return render_template('wash_cal.html', schedules=schedules, garden_id=id)

# THÊM
@mushroom_bp.route('/api/add_schedule/<int:id>', methods=['POST'])
def add_schedule(id):
    data = request.get_json()
    time_val = data.get('time')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO lich_tuoi (khu_id, thoi_gian_tuoi)
        VALUES (?, ?)
    """, (id, time_val))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

# XÓA
@mushroom_bp.route('/api/delete_schedule/<int:id>', methods=['DELETE'])
def delete_schedule(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM lich_tuoi WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

# SỬA
@mushroom_bp.route('/api/update_schedule/<int:id>', methods=['PUT'])
def update_schedule(id):
    data = request.get_json()
    time_val = data.get('time')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE lich_tuoi 
        SET thoi_gian_tuoi = ?
        WHERE id = ?
    """, (time_val, id))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})