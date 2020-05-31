


a = [25,45,158,8925,55,1255,4555,45251,545]
jieguo = 0
for i in a:
    jieguo = jieguo + i
print(jieguo)

i = 0
jieguo = 0
while i < len(a):
    jieguo = jieguo + a[i]
    i = i + 1
print(jieguo)


def leijia(a):
    '''
    累加
    '''
    jieguo = 0
    for i in a:
        jieguo = jieguo + i
    return jieguo



'''a = [25,45,158,8925,55,1255,4555,45251,545]
b = [12,4552,145,255,145,14]
xx = leijia(a)
yy = leijia(b)
print(xx,yy)


def chengfab(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(i,"X",j,"=",i*j,end="   ")
        print()'''
    


a = [25,45,158,8925,55,1255,4555,45251,545]
jieguo = 1
for i in a:
    jieguo = jieguo * i
print(jieguo)

def leicheng(a):
    jieguo = 1
    for i in a:
        jieguo = jieguo * i
    print(jieguo)

# 包-》模块-》类-》/方法/变量


print(4%2)