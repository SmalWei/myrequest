from sqlalchemy import create_engine
# 第一步创建引擎
egine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test')#  我的引擎
# create_engine('dialect+driver://username:password@host:port/database')
#         """
#         # dialect -- 数据库类型
#         # driver -- 数据库驱动选择
#         # username -- 数据库用户名
#         # password -- 用户密码
#         # host 服务器地址
#         # port 端口
#         # database 数据库
#         """
# 具体参数 网上都有
# 第二部 执行相关的操作  # 注意 egine 也可以执行 sql一句 eg :
# 关键字传参和位置传参一定要记牢参数的类型  以及写法
#cur=egine.execute('insert into t1 values(%s,%s);',[(1,"egon1"),(2,"egon2"),(3,"egon3")]) #按位置传值
# cur=egine.execute('insert into t1 values(%(id)s,%(name)s);',name='egon4',id=4) #按关键字传值
# 查询语句 和mysqldb 一样  eg:
# cur=egine.execute('select * from t1')
# cur.fetchone() #获取一行
# cur.fetchmany(2) #获取多行
# cur.fetchall() #获取所有行
# 注意
# SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，
# Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如：
# 二、创建表
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Enum,ForeignKey,UniqueConstraint,ForeignKeyConstraint,Index
from sqlalchemy.orm import sessionmaker
Base = declarative_base()  #生成orm基类
class Business(Base):
    __tablename__='business'
    id = Column(Integer,primary_key=True,autoincrement=True)
    bname = Column(String(32),nullable=False,index=True)
class Service(Base):
    __tablename__='service'
    id=Column(Integer,primary_key=True,autoincrement=True)
    sname=Column(String(32),nullable=False,index=True)
    ip=Column(String(15),nullable=False)
    port=Column(Integer,nullable=False)

    business_id=Column(Integer,ForeignKey('business.id'))
    #设置约束
    __table_args__=(
        UniqueConstraint(ip,port,name='uix_ip_port'),
        Index('ix_id_sname',id,sname)
    )
#多对多:多个用户可以是同一个role,多个role可以包含同一个用户
class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    uname=Column(String(32),nullable=False,index=True)


class Users2Role(Base):
    __tablename__='users2role'
    id=Column(Integer,primary_key=True,autoincrement=True)
    uid=Column(Integer,ForeignKey('users.id'))
    rid=Column(Integer,ForeignKey('role.id'))

    __table_args__=(
        UniqueConstraint(uid,rid,name='uix_uid_rid'),
    )


def init_db(): #创建表结构
    Base.metadata.create_all(egine)

def drop_db(): # 删除表结构
    Base.metadata.drop_all(egine)

# if __name__ == '__main__':
#     init_db()

# 注：设置外键的另一种方式 ForeignKeyConstraint(['other_id'], ['othertable.other_id'])
# 增删改查 需要创建会话 Sessoin
# 需要注意的是
# 特别注意
# Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
# Session = Session_class()

#增
#增
# row_obj=Dep(dname='销售') #按关键字传参,无需指定id,因其是自增长的
# session.add(row_obj)
# session.add_all([
#     Dep(dname='技术'),
#     Dep(dname='运营'),
#     Dep(dname='人事'),
# ])
#
# session.commit() 特别注意 需要提交一下 才会创建


# 删除
# session.query(Dep).filter(Dep.id > 3).delete()
# session.commit()


# 改
# session.query(Dep).filter(Dep.id > 0).update({'dname':'哇哈哈'})
# session.query(Dep).filter(Dep.id > 0).update({'dname':Dep.dname+'_SB'},synchronize_session=False)
# session.query(Dep).filter(Dep.id > 0).update({'id':Dep.id*100},synchronize_session='evaluate')
#
# session.commit()


# 查



#查所有,取所有字段
# res=session.query(Dep).all() #for row in res:print(row.id,row.dname) 查询所有数据
#
# #查所有,取指定字段
# res=session.query(Dep.dname).order_by(Dep.id).all() #for row in res:print(row.dname)
#
# res=session.query(Dep.dname).first()
# print(res) # ('哇哈哈_SB',)
#
# #过滤查
# res=session.query(Dep).filter(Dep.id > 1,Dep.id <1000) #逗号分隔,默认为and
# print([(row.id,row.dname) for row in res])