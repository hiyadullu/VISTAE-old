#main page 
from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def landing():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard_home():
    return render_template('dashboard.html')
