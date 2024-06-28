from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pagination import paginate

store_bp = Blueprint('store', __name__, url_prefix='/store')

@store_bp.route('/')
def get_store():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    query = """
        SELECT * from stores
    """
    params = []
    
    result, total_pages = paginate(query, params, page, per_page)

    return render_template('./store/store.html', result=result, page=page, per_page=per_page, total_pages=total_pages)