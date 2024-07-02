from flask import Blueprint, render_template, request
from utils import build_query, execute_query
from database import get_db_connection

bp = Blueprint('orderitem', __name__, url_prefix='/orderitems')

@bp.route('/')
def get_orderitem():
    filters = {}
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    
    base_query = "SELECT * FROM orderitems WHERE 1=1"
    query, params = build_query(base_query, filters)
    
    result, total_pages, no_results = execute_query(query, params, page, per_page)

    return render_template('orderitem/orderitem.html', result=result, page=page, per_page=per_page, total_pages=total_pages, no_results=no_results)