#import library
import psycopg2

#connect to postgreSQL
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

#Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS coba(
        id serial PRIMARY KEY
        ,email text
        ,name text
        ,phone text
        ,postal_code text)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS coba_using_copy(
        id serial PRIMARY KEY
        ,email text
        ,name text
        ,phone text
        ,postal_code text)
""")