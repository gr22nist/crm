from database import get_db_connection

def paginate(query, params, page, per_page=20):
    offset = (page - 1) * per_page
    query_with_pagination = query + " LIMIT ? OFFSET ?"
    paginated_params = params + [per_page, offset]
    
    conn = get_db_connection()
    cur = conn.cursor()
    
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
    
    # limit 와 offset 값 이외의 파라미터로 총 항목 수 계산 쿼리 실행 + 종료
    cur.execute(count_query, params)
    total_count = cur.fetchone()[0]
    conn.close()
    
    total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)
    
    return items_dict, total_pages