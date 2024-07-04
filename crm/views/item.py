from flask import Blueprint, render_template, request
from database import get_db_connection
from utils import build_query, execute_query
from search import get_item_search_fields
from queries import item_revenue_info

bp = Blueprint('item', __name__, url_prefix='/items')

@bp.route('/')
def get_item():
    filters = {
        'name': request.args.get("name"),
        'type': request.args.get("type")
    }
    types = filters['type']
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    
    base_query = "SELECT * FROM items WHERE 1=1"
    query, params = build_query(base_query, filters)
    
    result, total_pages, no_results = execute_query(query, params, page, per_page)
    fields = get_item_search_fields(request.args)
    
    return render_template('item/item.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results, fields=fields, filters=filters, types=types)

@bp.route('/<item_id>')
def item_detail(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE Id = ?", (item_id,))
    item = cur.fetchone()
    conn.close()
    
    item_sales_data = item_revenue_info(item_id)
    
    items = [dict(item)] if item else []

    return render_template('item/item_detail.html', items=items, item_sales_data=item_sales_data)