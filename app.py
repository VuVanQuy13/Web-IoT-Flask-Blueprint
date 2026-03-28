from flask import Flask, redirect, url_for
from Blueprints.Auths.login import login_bp 
from Blueprints.Auths.register import register_bp
from Blueprints.Garden.garden import garden_bp
from Blueprints.Mushroom.mushroom import mushroom_bp

app = Flask(__name__ , template_folder='templates' )
app.secret_key = 'ABC123'

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(garden_bp)
app.register_blueprint(mushroom_bp)

@app.route('/')
def index():
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    app.run(debug=True , host="0.0.0.0" , port=2004)
