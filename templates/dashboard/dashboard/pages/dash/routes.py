from flask import Blueprint, render_template
from flask import current_app as app

dash_bp = Blueprint('dash_bp', __name__,
                    template_folder='templates',
                    static_folder='static'
                    )

@dash_bp.route('/dashboard')
def dash():
    return render_template('dashboard.html')
