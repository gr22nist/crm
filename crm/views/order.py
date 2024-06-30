from flask import Blueprint, render_template, request
from paginate import paginate
from database import get_db_connection

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('/')
def get_order():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)
    
    base_query = "SELECT * FROM orders WHERE 1=1"
    params = []
    
    result, total_pages = paginate(base_query, params, page, per_page)

    return render_template('order/order.html', result=result, page=page, per_page=per_page, total_pages=total_pages)


@bp.route('/<order_id>')
def order_detail(order_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders WHERE Id = ?", (order_id,))
    order = cur.fetchone()
    conn.close()
    
    orders = [dict(order)] if order else []

    return render_template('order/order_detail.html', orders=orders)