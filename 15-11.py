
import mysql.connector
conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Uma@1234567890',
        database='college',
        port=3306,
        autocommit=False,
    )
print(conn.is_connected())
cur=conn.cursor()
cur.execute('SHOW TABLES')
print(cur.fetchall())
cur.execute(
    """CREATE TABLE uma(
    ROLLNO INT PRIMARY KEY,
   NAME VARCHAR(100),
     AGE INT)"""
)
cur.execute(
    """INSERT INTO uma VALUES(1,"uma",22)
    """
)
cur.execute(
    """INSERT INTO uma VALUES(2,"singdha",30)
    """
)
query="""Insert into uma (ROLLNO, NAME, AGE)
Values(%s,%s,%s)"""
data=[
    (3,"rama",34),
    (4,"suma",30),
    (5,"radha",6),
    (6,"vasudev",50),
]
cur.execute("select * from uma")
for row in cur.fetchall():
    print(row)
cur.executemany(query,data)
cur.execute("select * from uma limit 3")
print(cur.fetchall())
cur.execute("select* from uma ORDER BY NAME ASC")
cur.execute("select * from uma where age=%s",[22])
for row in cur.fetchall():
  print(row)
update_query="update uma set age=%s where name=%s"
cur.execute(update_query,("23","radha"))
cur.execute("delete from uma where name=%s",("uma",))
conn.commit()
cur.close()
conn.close()

