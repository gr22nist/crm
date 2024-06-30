from flask import Blueprint, render_template, request
from paginate import paginate
from database import get_db_connection

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/')
def get_user():
    name = request.args.get("name")
    gender = request.args.get("gender")
    age = request.args.get("age")

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)
    
    base_query = "SELECT * FROM users WHERE 1=1"
    params = []

    if name:
        base_query += " and name LIKE ?"
        params.append('%' + name + '%')
    if gender:
        base_query += " AND gender = ?"
        params.append(gender)
    if age:
        base_query += " AND age = ?"
        params.append(int(age))
        
    print("Query:", base_query)
    print("Params:", params)

    try:
        result, total_pages = paginate(base_query, params, page, per_page)
        no_results = not result
    except Exception as e:
        no_results = True
        result = []
        total_pages = 1

    return render_template('user/user.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results)


@bp.route('/<user_id>')
def user_detail(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE Id = ?", (user_id,))
    user = cur.fetchone()
    conn.close()
    
    users = [dict(user)] if user else []

    return render_template('user/user_detail.html', users=users)