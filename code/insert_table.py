#import library
import psycopg2
import csv
import pandas as pd
from sqlalchemy import create_engine


#connect to postgreSQL
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

#insert table - pake cara universal
with open('C:/Users/Edo DF/Desktop/bootcamp data engineer/Project/Project_3/source/users_w_postal_code.csv') as f :
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO coba VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

conn.commit()

#insert table - pake yang ada di posgres aja -> COPY
with open('C:/Users/Edo DF/Desktop/bootcamp data engineer/Project/Project_3/source/users_w_postal_code.csv', 'r') as f :
    next(f)
    cur.copy_from(f, 'coba_using_copy', sep=',', columns=('email', 'name', 'phone', 'postal_code'))

conn.commit()

#insert table - pake pandas
#kalo datanya ga ada perubahan apa2 (Transform) dan cuma extrac dan load aja jgn pake pandas soalnya makan resouce yg banyak
df = pd.read_csv('C:/Users/Edo DF/Desktop/bootcamp data engineer/Project/Project_3/source/users_w_postal_code.csv', sep=',')
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
df.to_sql("coba_using_pandas1", engine)

