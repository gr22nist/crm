from database import get_db_connection

def paginate(query, params, page, per_page=10):
    offset = (page - 1) * per_page
    query_with_pagination = query + " LIMIT ? OFFSET ?"
    params.extend([per_page, offset])
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # 페이지네이션 적용된 쿼리 실행
    cur.execute(query_with_pagination, params)
    items = cur.fetchall()
    items_dict = [dict(row) for row in items]
    
    # where절 추출
    where_start = query.find("WHERE 1=1")
    conditions = query[where_start + len("WHERE 1=1"):]
    
    # 총 항목 수 계산
    count_query = "SELECT COUNT(*) FROM " + query[query.find("FROM ") + 5:query.find("WHERE 1=1")] + " WHERE 1=1" + conditions
    
    # limit 와 offset 값 이외의 파라미터로 총 항목 수 계산 쿼리 실행 + 종료
    cur.execute(count_query, params[:-2])
    total_count = cur.fetchone()[0]
    conn.close()
    
    total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)
    
    return items_dict, total_pages