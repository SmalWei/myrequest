from sqlalchemy import  create_engine

HOSTNAME = '127.0.0.1'  # ip地址
PORT = '3306'  # 端口号
DATABASE = 'mysqldb'  # 数据库名
USERNAME = 'root'  # 用户名
PASSWORD = 'password'  # 用户登录密码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
engine = create_engine(DB_URI)

# 2. 声明映像
from sqlalchemy.ext.declarative import  declarative_base
Base = declarative_base(engine)

# 5.创建会话
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()