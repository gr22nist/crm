from flask import Blueprint, render_template, request
from utils import build_query, execute_query
from queries import fetch_one

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('/')
def get_order():
    filters = {}
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    
    base_query = """
        SELECT o.id, o.orderat, s.name AS storename, u.name AS username
        FROM orders o
        JOIN users u ON o.userid = u.id
        JOIN stores s ON o.storeid = s.id
    """
    query, params = build_query(base_query, filters)
    
    result, total_pages, no_results = execute_query(query, params, page, per_page)
    

    
    return render_template('order/order.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results)


@bp.route('/<order_id>')
def order_detail(order_id):
    query = """
        SELECT o.id, o.orderat, s.name AS storename, u.name AS username
        FROM orders o
        JOIN users u ON o.userid = u.id
        JOIN stores s ON o.storeid = s.id
        WHERE o.id = ?
    """
    order = fetch_one(query, (order_id,))
    
    orders = [dict(order)] if order else []
    
    return render_template('order/order_detail.html', orders=orders)