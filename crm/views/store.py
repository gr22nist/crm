from flask import Blueprint, render_template, request
from paginate import paginate
from database import get_db_connection

bp = Blueprint('store', __name__, url_prefix='/stores')

@bp.route('/')
def get_store():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)
    query = """
        SELECT * from stores
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('store/store.html', result=result, page=page, per_page=per_page, total_pages=total_pages)

@bp.route('/<store_id>')
def store_detail(store_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stores WHERE Id = ?", (store_id,))
    store = cur.fetchone()
    conn.close()
    
    stores = [dict(store)] if store else []

    return render_template('store/store_detail.html', stores=stores)