from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from paginate import paginate

bp = Blueprint('item', __name__, url_prefix='/items')

@bp.route('/')
def get_item():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    query = """
        SELECT * from items
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('./item/item.html', result=result, page=page, per_page=per_page, total_pages=total_pages)