import pymysql

class Db:
    def __init__(self,host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def qurey(self,sql):
        '''
        数据库的查询方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cur = db.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        db.close()
        return res

    def commit(self,sql):
        '''
        数据库的修改方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        db.close()



class suanfa:

    def jiafa(self,a):
        jieguo = 0
        for i in a:
            jieguo = jieguo + i
        return jieguo

    def jianfa(self,a,b):
        jieguo = a - b
        return jieguo

    def chengfa(self,a):
        jieguo = 1
        for i in a:
            jieguo = jieguo * i
        return jieguo

    def chufa(delf,a,b):
        jieguo = a / b
        return jieguo



