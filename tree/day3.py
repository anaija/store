#1.输入10个数字，并打印10个数的求和结果

L=[1,2,3,4,5,6,7,8,9,10]

a=sum(L)

print("请输出数字求和的结果：",a)





#2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数#最大的数
n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    if a>n:
        n=a
print("10个数字中最大数为：",n)

#10个数的和
n=0
for i in range(0,10):
    print("请输入数字：")
    b = int(input())
    n += a
print("10个数字的和为：",n)

#平均数
n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    n=n+a
print("数字平均数为：",n/10)





#3.使用random模块，如何产生 50~150之间的数？
import random
print(random.randint(50, 150))  # 随机一个[50,150]之间的整数





#4.从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
#print('输入三角形的三条边，判断这是什么三角形。')

a = float(input('请输入第一条边：'))
b = float(input('请输入第二条边：'))
c = float(input('请输入第三条边：'))

# 放进列表排序
li = [a, b, c]
li.sort()

# 如果两个短边之和不大于最长边，就不是三角形！
if li[2] <= 0 or li[0] + li[1] <= li[2]:
    print('这不是三角形！')
# 如果两个短边或者两个长边相等
elif li[0] == li[1] or li[1] == li[2]:
    # 如果最短边和最长边相等，就是全等三角形！
    if li[0] == li[2]:
        print('等边三角形！')
    # 如果最短边=(最长边^2 / 2)^0.5（勾股定理），就是等腰直角三角形！
    # round(number, digits)，返回浮点数number的四舍五入值，digits是四舍五入时要使用的小数位数。
    elif li[0] == round(((li[2] ** 2) / 2) ** 0.5, 3):
        print('等腰直角三角形！')
    # 如果仅是两个短边或3
    # 6
    # 10者两个长边相等，就是等腰三角形！
    else:
        print('等腰三角形！')
# 如果满足勾股定理并且两个短边不相等，就是直角三角形！
elif li[0] ** 2 + li[1] ** 2 == li[2] ** 2 and li[0] != li[1]:
    print('直角三角形！')
# 如果仅满足两个短边之和大于最长边，就是普通三角形！，
else:
    print('普通三角形！')





#5.有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56

print("请输入两个整数：")
a = int(input("第一个整数："))
b = int(input("第二个整数："))

a,b = b,a
print("使用Python内置方法得出结果：")
print("a变换后为：%d"% a)
print("b变换后为：%d"% b)



#6.实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
count = 0   #计数器
username = "aaa"  #登录用户名
userpassword = "asd"  #登录密码

#读取黑名单用户
f = open("aaa.txt","r")
file_list = f.readlines()
f.close()
lock = []
name = input("登录用户名:")
#判断用户是否在黑名单
for i in file_list:
    line=i.strip("\n")
    lock.append(line)
if name in lock:
    print ("您的账号已锁定，请联系管理员。")
else:
#如果用户没有在黑名单，判断用户是否存在。
     if name == username:
         #如果密码连续输错三次，锁定账号。
         while count <3:
             password = input("登录密码：")
             if name == username and password == userpassword:
                   print("欢迎，%s"  %name )
                   break
             else:
                   print("账号密码不匹配")
                   count += 1
         else:
             print ("对不起，您的账号连续输错三次账号已锁定，请联系管理员。")
             f=open("aaa.txt","w+")
             li=['%s'%username]
             f.writelines(li)
             f.close()
     else:
         print("用户名不存在，请输入正确的用户名。")





#7.编程实现下列图形的打印

def equil_tri(n):
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        for j in range(1,i+1):
            print('*'*1,end=' ')
        print('')

equil_tri(7)




#8.使用while循环实现NxN乘法表的打印。
i = 1
num = int(input("请输入需要打印的行数:"))
while i <= num:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, i*j), end="\t")
        j += 1
    print("")
    i += 1





#9.编程实现99乘法表的倒叙打印
x=9
#x在1-9中遍历
while x>=0:
  y=1
  while y<=x:
     print(str(y)+"*"+str(x)+"=",x*y,end='')
     y+=1
  print()  #print空在x变化时插入换行
  x-=1






#10.一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。

jing=-20
up=3
down=-2
num=1
while jing<0:
    print ('day ',num,end="   ")
    jing+=up
    print('up',jing,end="   ")
    if jing>=0:
        break
    jing+=down
    print('down',jing)
    if jing>=0:
        break
    num+=1





#11.判断下列变量命名是否合法
#标识符	是否合法	标识符	是否合法
#char		Cy%ty	
#Oax_li		$123	
#fLul		3_3 	
#BYTE		T_T	

# 变量名是否合法:
# 1.变量名可以由字母, 数字或者下划线组成
# 2.变量名只能以字母或者下划线开头    s = 'hello@'
# 3.判断变量名的第一个元素是否为字母或者下划线   s[0]
# 4.如果第一个元素符合条件, 判断除了第一个元素之外的其他元素   s[1:]

# 思路：
# 1.变量名的第一个字符是否为字母或下划线
# 2.如果是，继续判断 --> 4
# 3.如果不是，报错
# 4.依次判断除了第一个字符之外的其他字符
# 5.判断是否为字母数字或者下划线

while True:

    s = input('变量名:')

    # 定义退出

    if s == 'exit':

        print('欢迎下次使用')

        break

    # 判断字符串第一个变量是否满足条件

    if s[0].isalpha() or s[0] == '_':

        for i in s[1:]:

            # 判断字符串以后的变量是否满足条件

            if not (i.isalnum() or i == '_'):

                print('%s变量名不合法' % s)

                break

            else:

                print('%s变量名合法' % s)

    else:

        print('%s变量名不合法' % s)




#12.继续完成上午的猜数字游戏的需求功能。
#1.添加计数打印功能
#2.添加次数金币功能和锁定系统功能。

import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("猜数字：")
    guess = int(temp)

    if guess == answer:
        print("猜对啦")
        break
    else:
        if guess < answer:
            print("猜小啦")
        if guess > answer:
            print("猜大啦")
    counts = counts - 1
print("end.")



#13.用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
def  recursion(n): #'定义递归函数实现求阶乘功能'
    if n==1:
        return 1
    else:
        return  n*recursion(n-1)

list=[ ] #定义一个空的列表，将调用递归函数生成的阶乘值追加到列表
for  i  in range(1,21):
    list.append(recursion(i))# 将调用递归函数生成的阶乘值追加到列表
print(sum(list)) #列表求和

Sum = 0
for  i  in range(1,21):
    Sum +=recursion(i)
print(Sum)
