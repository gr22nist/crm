import sqlite3

DATABASE = './crm.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn

def get_query(query, params=None):
    conn = get_db_connection()
    cur = conn.cursor()

    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)

    result = cur.fetchall()
    result = [dict(row) for row in result]
    conn.close()

    return result