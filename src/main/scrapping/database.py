import psycopg2

conn = psycopg2.connect("dbname=labarus user=server password=qwedsazxc")

cur = conn.cursor()


def list(table, limit=10):
    cur.execute("SELECT * FROM ", table, " LIMIT ", limit, ";")
