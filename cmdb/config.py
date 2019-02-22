# 数据库
schema ='mysql+pymysql'
username = 'root'
password = '123'
host = '127.0.0.1'
port = 3306
database = 'cmdb'
params = 'charset=utf8'

URL =  "{}://{}:{}@{}:{}/{}?{}".format(
    schema, username, password, host, port, database, params
)

DATABASE_DEBUG = True