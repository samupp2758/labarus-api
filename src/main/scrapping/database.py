import psycopg2

conn = psycopg2.connect("dbname=labarus user=server password=qwedsazxc")
cur = conn.cursor()

def list(table, limit=10):
    cur.execute("SELECT * FROM %s LIMIT %s;",(table,limit))
    return cur.fetchAll()

def findByPk(table, pk):
    cur.execute("SELECT * FROM %s WHERE id=%s;",(table,pk))
    return cur.fetchAll()

def findByField(table, field, value,limit = 10):
    cur.execute("SELECT * FROM %s WHERE %s=%s LIMIT %s;",(table,field,value,limit))
    return cur.fetchAll()