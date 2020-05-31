'''
a = input("请输入您的姓名：")
b = input("请输入您的年龄：")
c = input("请输入您的身高：")
d = input('请输入您的体重：')
x = {'name':a,'age':b,'shengao':c,'tizhong':d}
print(x)
y = {}
y["name"] = a
y['age'] = b
y['shengao'] = c
y['tizhong'] = d
print(y)


a = '10'
if a in [10,'10']:
    print("哈哈哈")
else:
    print("嘻嘻嘻")
m = input('请输入你的名字：')
n = ['图南','老狗','最光阴']
if m in n:
    print(m)
else:
    n.append(m)
    print(n)



'''


'''for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="   ")
    print()

for i in ['红','黄','绿']:
    if i == "红":
        for j in range(30):
            print(i,30-j)
    elif i == '黄':
        for j in range(3):
            print(i,3-j)
    else:
        for j in range(30):
            print(i,30-j)

light = {'红':30,'黄':3,'绿':30}
for i in light:
    for j in range(light[i]):
        print(i,light[i]-j)


a = 1
while a < 10:
    print("哈哈哈")
    a = a + 1

print("-----------------")
light = ['红','黄','绿']
i = 0
while i < 3:
    j = 0 
    if light[i] =="黄":
        j = 27
        while j < 30:
            print(light[i],30-j)
            j += 1
    else:
        while j < 30:
            print(light[i],30-j)
            j += 1
    i = i +1'''

'''a = [12,55,885,56,47,4556,55,547,22,45,79,4452,41,62,14,33]
lowlist =[]
highlist =[]
i = 0
while i < len(a):
    if a[i] >= 100:
        highlist.append(a[i])
    else:
        lowlist.append(a[i])
    i += 1 
print(lowlist,highlist)


for i in a:
    if i <= 100:
        lowlist.append(i)
    else:
        highlist.append(i)
print(lowlist,highlist)



sstr = "125155125151635132123125154878987986512516565451233652121245987142594461"

for i in range(len(sstr)-2):
    if sstr[i]+sstr[i+1]+sstr[i+2] == "461":
        print(i)'''

a = [12,55,885,56,47,4556,55,547,22,45,79,4452,41,62,14,33]
lowlist =[]
highlist =[]
for i in a:
    if i <= 60:
        lowlist.append(i)
    else:
        highlist.append(i)
print(lowlist,highlist)

      
i = 0
while i < len(a):
    if a[i] <= 60:
        lowlist.append(a[i])
    else:
        highlist.append(a[i])
    i = i + 1
print(lowlist,highlist)



sstr = "125155125151635132123125154878987986512516565451233652121245987142594461"
for i in range(len(sstr)-2):
    if sstr[i]+sstr[i+1]+sstr[i+2] == '233':
        print(i)

for i in range(len(sstr)-2):
    if sstr[i:i+3] == '233':
        print(i)

