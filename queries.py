from database import get_db_connection

def fetch_one(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchone()
    conn.close()
    return dict(result) if result else {}

def fetch_all(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    results = cur.fetchall()
    conn.close()
    return [dict(row) for row in results] if results else []

# 페이지별 쿼리

def user_order_info(user_id):
    query = """
        SELECT o.id AS "주문아이디", o.orderat AS "주문시간", s.name AS "매장명", i.name AS "상품명"
        FROM users u
        JOIN orders o ON u.id = o.userid
        JOIN stores s ON o.storeid = s.id
        JOIN orderitems oi On o.id = oi.id
        JOIN items i ON oi.itemid = i.id
        WHERE u.id = ?
    """
    return fetch_all(query, (user_id,))

def store_revenue_info(store_id):
    query = """
        SELECT s.name AS "매장명", strftime('%Y', o.orderat) AS "년", strftime('%m', o.orderat) AS "월",
        SUM(i.unitprice) AS "총매출액"
        FROM stores s
        JOIN orders o ON s.id = o.storeid
        JOIN orderitems oi ON o.id = oi.orderid
        JOIN items i ON oi.itemid = i.id
        WHERE s.id = ?
        GROUP BY s.id, s.name, strftime('%Y', o.orderat), strftime('%m', o.orderat)
        ORDER BY s.id, s.name, strftime('%Y', o.orderat), strftime('%m', o.orderat);
    """
    return fetch_all(query, (store_id,))

def item_revenue_info(item_id):
    query = """
        SELECT i.name AS "제품명", strftime('%Y', o.orderat) AS "년", strftime('%m', o.orderat) AS "월",
        COUNT(*) * (i.unitprice) AS "총매출액"
        FROM items i
        JOIN orderitems oi ON i.id = oi.itemid
        JOIN orders o ON oi.orderid = o.id
        JOIN stores s ON s.id = o.storeid
        WHERE i.id = ?
        GROUP BY i.name, strftime('%Y', o.orderat), strftime('%m', o.orderat)
        ORDER BY strftime('%Y', o.orderat), strftime('%m', o.orderat);
    """
    return fetch_all(query, (item_id,))

# def fetch_most_ordered_menu(user_id):
#     query = """
#         SELECT menu_id, COUNT(*) AS order_count
#         FROM orders
#         WHERE user_id = ?
#         GROUP BY menu_id
#         ORDER BY order_count DESC
#         LIMIT 1
#     """
#     return fetch_one(query, (user_id,))

# def fetch_most_ordered_item(order_id):
#     query = """
#         SELECT item_id, COUNT(*) AS order_count
#         FROM orderitems
#         WHERE order_id = ?
#         GROUP BY item_id
#         ORDER BY order_count DESC
#         LIMIT 1
#     """
#     return fetch_one(query, (order_id,))