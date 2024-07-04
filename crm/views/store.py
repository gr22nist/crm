from flask import Blueprint, render_template, request
from database import get_db_connection
from utils import build_query, execute_query, paginate
from search import get_store_search_fields
from queries import store_revenue_info

bp = Blueprint('store', __name__, url_prefix='/stores')

@bp.route('/')
def get_store():
    filters = {
        'name': request.args.get("name"),
        'type': request.args.get("type")
    }

    types = filters['type']
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    
    base_query = "SELECT * FROM stores WHERE 1=1"
    query, params = build_query(base_query, filters)
    
    result, total_pages, no_results = execute_query(query, params, page, per_page)
    fields = get_store_search_fields(request.args)
    
    return render_template('store/store.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results, fields=fields, filters=filters, types=types)

@bp.route('/<store_id>')
def store_detail(store_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stores WHERE Id = ?", (store_id,))
    store = cur.fetchone()
    conn.close()
    
    item_sales_data = store_revenue_info(store_id)
    
    stores = [dict(store)] if store else []

    return render_template('store/store_detail.html', stores=stores, item_sales_data=item_sales_data)