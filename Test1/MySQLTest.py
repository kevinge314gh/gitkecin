#coding='gbk'
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )
cur = conn.cursor()

sqli="insert into django1 values(%s,%s,%s)"
cur.execute(sqli,('006','gwk','59'))

cur.close()
conn.commit()
conn.close()