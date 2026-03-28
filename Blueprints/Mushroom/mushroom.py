from flask import Blueprint, render_template
import sqlite3
import os

mushroom_bp = Blueprint('mushroom', __name__, 
                        template_folder='mushroom_template', 
                        static_folder="static", 
                        url_prefix='/mushroom')

# ĐƯỜNG DẪN DATABASE TỐI ƯU
def get_db_connection():
    # Lấy thư mục gốc (Parent của folder Mushroom)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', '..', 'Farm_Database.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Import các thành phần con để đăng ký route vào mushroom_bp
from . import data_env
from . import number_mush
from . import wash_cal

@mushroom_bp.route('/<int:mushroom_id>')
def index(mushroom_id):
    return render_template('mushroom.html', garden_id=mushroom_id)