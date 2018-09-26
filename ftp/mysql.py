# mysql.py
import pymysql
# 创建数据库连接对象
db = pymysql.connect(host="localhost",user="root",
    passwd="123456",database="day04",charset="utf8")
# 利用db 创建游标对象
cursor = db.cursor()
# 利用cursor的execute()方法执行SQL命令
# cursor.execute("create database db5;")
# cursor.execute("use db5;")
# cursor.execute("create table t1(id int, name varchar(20);")
cursor.execute("insert into sheng values (30,400000,'吉林省')")
# cursor.execute(sql_insert)
# 提交到数据库执行
db.commit()
print("ok")
# 关闭游标对象
cursor.close()
# 断开数据库连接
db.close()




