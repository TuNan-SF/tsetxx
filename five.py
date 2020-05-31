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
        try:
            cur.execute(sql)
            db.commit()
            db.close()
            return True
        except:
            return False


class Db2(Db):
    
    def desctable(self,tablename):
        '''
        数据库的查询方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cur = db.cursor()
        cur.execute('desc '+tablename+';')
        res = cur.fetchall()
        db.close()
        return res

    def commit(self,sql):
        '''
        数据库的修改方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cur = db.cursor()
        try:
            cur.execute(sql)
            db.commit()
            db.close()
            return True
        except:
            return False



'''for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a != b) and (b != c) and (c != a):
                print(a,b,c)

i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print((i - arr[idx]) * rat[idx])
        i = arr[idx]
print(r)

for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)

year = input('请输入年份:')
month = input('请输入月份:')
day = input('请输入日份:')
d = 0
m = [0,31,59,90,120,151,181,212,243,273,304,334]
if :
    d = d + 1
else:
    d = 0
monthdays = m[month-1]
days = monthdays + day + d
print(days)

x = int(input('请输入整数：'))
y = int(input('请输入整数：'))
z = int(input('请输入整数：'))
a = [x,y,z]
a.sort()
print(a)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

a = [0,1,2,3,4,5,6,7,8,9]
b =a.copy()
print(b)

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'x',j,'=',i*j,end='  ')
    print()

import time

a = [1,2,3,4]
for i in range(len(a)):
    print(a[i])
    time.sleep(1) 

time.sleep(1) 
print(time.strftime("%Y-%m-%d %H:%M:%S"))

a = [34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
da = []
xiao = []
for i in a:
    if i <= 100 :
        da.append(i)
    else:
        xiao.append(i)
print(da,xiao)

'''