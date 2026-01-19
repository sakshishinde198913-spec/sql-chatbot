import pymysql

def run_query(sql: str):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="donations_db"
    )

    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()

    conn.close()
    return result
