from flask import Blueprint, render_template, request
from paginate import paginate

bp = Blueprint('orderitem', __name__, url_prefix='/orderitems')

@bp.route('/')
def get_orderitem():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)
    query = """
        SELECT * from orderitems
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('orderitem/orderitem.html', result=result, page=page, per_page=per_page, total_pages=total_pages)