import pymysql

# 连接数据库
con = pymysql.connect(host='localhost', user='root', password='Victory&40413', database='shengchanshixi',
                      charset='utf8')
print("数据库连接成功")
# 创建游标
cursor = con.cursor()


# 新增用户
def insertUser(id, password, name=""):
    sql = "select * from user where id='{}'".format(id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result != ():
        return -1  # 已经存在该用户，返回-1
    sql = "insert into user (id, password, name) values ('{}', '{}', '{}')".format(id, password, name)
    cursor.execute(sql)
    con.commit()
    return 1  # 返回1代表插入成功

# 查询用户
def selectUser(id, password):
    sql = "select * from user where id='{}' and password='{}'".format(id, password)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return -1  # 不存在该用户或者密码错误，返回-1
    return 1

