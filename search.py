from flask import Blueprint, render_template, request, flash
from pagination import paginate

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search():
    search_type = request.args.get("type")
    name = request.args.get("name")
    gender = request.args.get("gender")
    age = request.args.get("age")
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if search_type == "user":
        query = "SELECT name, gender, age, birthdate FROM users WHERE 1=1"
    else:
        return "Invalid search type", 400

    params = []

    if search_type == "user":
        if name:
            query += " AND name LIKE ?"
            params.append('%' + name + '%')
        if gender:
            query += " AND gender = ?"
            params.append(gender)
        if age:
            query += " AND age = ?"
            params.append(age)
    # 다른 검색 타입에 대한 조건을 추가할 수 있음

    items, total_pages = paginate(query, params, page, per_page)
    
    return render_template('user.html', items=items, page=page, per_page=per_page, total_pages=total_pages)