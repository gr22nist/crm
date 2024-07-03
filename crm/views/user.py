from flask import Blueprint, render_template, request
from database import get_db_connection
from utils import build_query, execute_query
from search import get_user_search_fields
from queries import user_order_info

bp = Blueprint('user', __name__, url_prefix='/users')

@bp.route('/')
def get_user():
    filters = {
        'name': request.args.get("name"),
        'gender': request.args.get("gender"),
        'age': request.args.get("age")
    }
    
    error = None
    try:
        if filters['age']:
            age = int(filters['age'])
            if age < 1:
                error = 'Age must be a positive number.'
    except ValueError:
        error = '올바른 입력 값이 아닙니다'

    if error:
        result = []
        total_pages = 0
        no_results = True
    else:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', default=15, type=int)
        
        base_query = "SELECT * FROM users WHERE 1=1"
        query, params = build_query(base_query, filters)
        
        result, total_pages, no_results = execute_query(query, params, page, per_page)
    
    fields = get_user_search_fields(request.args)
    
    return render_template('user/user.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results, fields=fields, error=error)  # 에러 메시지 전달

@bp.route('/<user_id>')
def user_detail(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    conn.close()

    user_info = dict(user) if user else []
    user_orders = user_order_info(user_id)

    return render_template('user/user_detail.html', user=user_info, user_orders=user_orders)