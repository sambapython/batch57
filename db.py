import psycopg2
con = psycopg2.connect(host="localhost",
	port=5432,
	user="postgres",
	password="root",database="db2")
cur=con.cursor()
q="create table customer (id int, name varchar(250))"
cur.execute(q)
import random
names=["samba","vikas","srinivas","praneeth","mahesh","ram"]
for i in range(2,200):
    q="insert into customer(id, name) values(%s,'%s')"%(i, random.choice(names))
    cur.execute(q)
    con.commit()
q="select name, count(*) as cnt from customer group by name order by cnt"
cur.execute(q)
data = cur.fetchall()
print(data)