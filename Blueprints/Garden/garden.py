from flask import Blueprint , render_template , url_for , redirect , request , jsonify
import sqlite3
import os

garden_bp = Blueprint('garden', __name__, template_folder='garden_template', static_folder="static", url_prefix='/garden')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR , '..' , '..' , 'Farm_Database.db')


def get_db_connection():
    conn = sqlite3.connect(DB_PATH , timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


# render garden
@garden_bp.route('/')
def garden():
    conn = get_db_connection()
    sql_list_garden = """
        SELECT * FROM khu_vuon 
        ORDER BY id ASC
    """
    gardens = conn.execute(sql_list_garden).fetchall()
    conn.close()
    return render_template('garden.html', all_farms=gardens)

# Add farm
@garden_bp.route('/api/add' , methods=["POST"])
def add_farm():
    data = request.get_json()
    desc = data.get('description', '')         
    name = data.get('namefarm')      

    if not name: 
        return jsonify({
            "error": "Tên vườn phải bắt buộc"
        }) , 400
    
    with sqlite3.connect(DB_PATH , timeout=10) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        sql_addFarm = """
            INSERT INTO khu_vuon(ten_khu , mo_ta)
            VALUES (:ten_khu , :mo_ta)
        """
        cur.execute(sql_addFarm , {
            "ten_khu": name,
            "mo_ta": desc
        })
        farm_id = cur.lastrowid

    return jsonify({
        "id": farm_id,
        "namefarm": name,
        "description": desc
    })

# Delete Farm
@garden_bp.route('/api/delete/<int:id>' , methods=["DELETE"])
def delete_farm(id):
    with sqlite3.connect(DB_PATH, timeout=10) as conn:
        conn.row_factory = sqlite3.Row
        sql_deleteFarm = """
            DELETE FROM khu_vuon
            WHERE id=:id
        """
        conn.execute(sql_deleteFarm , {
            "id": id
        })

    return  jsonify({
        "success": True
    })

# Update Farm
@garden_bp.route('/api/update/<int:id>', methods=["POST"])
def update_farm(id):
    data = request.get_json()
    newname = data.get('namefarm')
    newdesc = data.get('description' ,'')

    if not newname:
        return jsonify({"error": "Tên vườn không được để trống!"}), 400
    
    with sqlite3.connect(DB_PATH, timeout=10) as conn:
        conn.row_factory = sqlite3.Row
        sql_updateFarm = """
            UPDATE khu_vuon 
            SET ten_khu=:newname, mo_ta=:newdescription
            WHERE id=:id
        """
        conn.execute(sql_updateFarm, {
            "newname": newname,
            "newdescription": newdesc,
            "id": id
        })

    return jsonify({
        'success': True
    })


