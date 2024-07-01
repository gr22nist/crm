from flask import Blueprint, render_template, request
from paginate import paginate
from database import get_db_connection

bp = Blueprint('item', __name__, url_prefix='/items')

@bp.route('/')
def get_item():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    query = """
        SELECT * from items
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('item/item.html', result=result, page=page, per_page=per_page, total_pages=total_pages)

@bp.route('/<item_id>')
def item_detail(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE Id = ?", (item_id,))
    item = cur.fetchone()
    conn.close()
    
    items = [dict(item)] if item else []

    return render_template('item/item_detail.html', items=items)