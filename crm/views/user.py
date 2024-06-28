from flask import Blueprint, render_template, request
from pagination import paginate

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/')
def get_user():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    query = "SELECT * FROM users WHERE 1=1"
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('user/user.html', result=result, page=page, per_page=per_page, total_pages=total_pages)