from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from paginate import paginate

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('/')
def get_order():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    query = """
        SELECT * from orders WHERE 1=1
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('./order/order.html', result=result, page=page, per_page=per_page, total_pages=total_pages)