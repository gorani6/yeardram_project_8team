from . import app
from .db_control import DB
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test-mysql")
def check_db_connection():
    try: connection = DB().check_connection()
    except: return "error in DB instance"
    return f"{connection}"