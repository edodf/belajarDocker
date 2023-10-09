import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

cur.execute("""
    SELECT * FROM coba_using_pandas1
""")

all = cur.fetchall()
print(all)