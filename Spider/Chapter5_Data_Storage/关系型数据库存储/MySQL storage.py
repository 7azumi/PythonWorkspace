import pymysql

# 连接MySQL，并查询版本号及所有数据库
db = pymysql.connect(host='localhost', user='root', password='Fl+13+Mysql', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('VERSION: ',data)
# cursor.execute('CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET UTF8')
cursor.execute('SHOW DATABASES')
data = cursor.fetchall()
print('BASES: \n',data)

# 建表
cursor.execute('USE spiders')
sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(31) NOT NULL,name VARCHAR(31) NOT NULL,' \
      'age INT NOT NULL, PRIMARY KEY(id))'
# cursor.execute(sql)
cursor.execute('SHOW TABLES')
data = cursor.fetchall()
print('TABLES: \n',data)

# 插入数据
# 更新数据
# 删除数据
# 查询数据

db.close()