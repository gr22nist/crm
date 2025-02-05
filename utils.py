from database import get_db_connection

def build_query(base_query, filters):
    query = base_query
    params = []
    
    for key, value in filters.items():
        if value:
            if key == 'age':
                query += f" AND {key} = ?"
                params.append(value)
            else:
                query += f" AND {key} LIKE ?"
                params.append(f'%{value}%')
    
    return query, params

def execute_query(query, params, page, per_page):
    try:
        result, total_pages = paginate(query, params, page, per_page)
        no_results = not result
    except Exception as e:
        print(f"Error executing query: {e}")
        no_results = True
        result = []
        total_pages = 1

    return result, total_pages, no_results

def paginate(query, params, page, per_page=15):
    offset = (page - 1) * per_page
    query_with_pagination = query + " LIMIT ? OFFSET ?"
    paginated_params = params + [per_page, offset]

    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # 페이지네이션 적용된 쿼리 실행
        cur.execute(query_with_pagination, paginated_params)
        items = cur.fetchall()
        items_dict = [dict(row) for row in items]

        # where절 추출
        where_start = query.upper().find("WHERE")
        if where_start == -1:
            where_start = len(query)
            conditions = ""
        else:
            conditions = query[where_start:]

        # 총 항목 수 계산
        count_query = "SELECT COUNT(*) FROM " + query[query.upper().find("FROM ") + 5:where_start] + " " + conditions
        cur.execute(count_query, params)
        total_count = cur.fetchone()[0]
        total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)
        
    except Exception as e:
        print(f"페이징 오류: {e}")
        items_dict = []
        total_pages = 1

    conn.close()
    
    return items_dict, total_pages