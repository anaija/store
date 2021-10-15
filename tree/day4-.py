#1.  有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
#names = [
#    ["曹操","56","男","106","IBM", 500 ,"50"],
#    ["大乔","19","女","230","微软", 501 ,"60"],
#    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
#]
#1.统计每个人的平均薪资
#2.统计每个人的平均年龄
#3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
#4.统计公司男女人数
#5.每个部门的人数

# 姓名  年龄  性别  编号  任职公司 薪资 部门编号
names = [
    ["曹操",56,"男","106","IBM", 500 ,"50"],
    ["大乔",19,"女","230","微软", 501 ,"60"],
    ["小乔", 19, "女", "210", "Oracle", 600, "60"],
    ["许褚", 45, "男", "230", "Tencent", 700 , "10"]
]

salary=0
ages=0
man_num=0
female_num=0
apartment=[]
count=0
#平均薪资
for i in range(4):   #左闭右开
    salary =names[i][5]+salary
print("平均薪资为：",salary/4)

#平均年龄
for i in range(4):
    ages=names[i][1]+ages
print("平均年龄为：",ages/4)

#公司新添加一个员工
names.append(["刘备",45,"男","220","alibaba",500,"30"])
print(names)

#统计公司男女人数
for i in range(4):
  if names[i][2] == "男":
      man_num=man_num+1
  else:
      female_num=female_num+1
print("该公司男生人数为：",man_num,"该公司女生人数为：",female_num)

#每个部门的人数
for i in range(4):

    if names[i][6] not in apartment:
        apartment.append(names[i][6])
    print(apartment)
    else:
        count[i]=count[i]+1
    zip(apartment,count)
print(zip)


#2.现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
#[罗恩, 23 ,35 ,44]
#[哈利 ,60, 77 ,68 ,88, 90]
#[赫敏, 97 ,99 ,89 ,91, 95, 90]
#[马尔福 ,100, 85 ,90]
#求每个人的总成绩？
people=[["罗恩",23,35,44],
["哈利",60,77,68,88,90],
["赫敏",97,99,89,91,95,90],
["马尔福",100,85,90]]
for i in range(len(people)):
    sum0=0
    for j in range(1,len(people[i])):
        sum0=sum0+people[i][j]
    print(people[i][0],"的成绩是",sum0)
    
   
  
  
#3.当输入54321时，写出下面的执行结果
#num=int(input("请输入一个数："))
#while num != 0:
#    print(num&10)
#    num=num//10

#输出结果：    
#0
#8
#10
#2
#0




#4.请对下列列表进行冒泡排序（网易测试开发笔试题）                      
#a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
n = len(a)    #求出a的长度
for x in range(n-1):
   for y in range(n-1-x):
      if a[y]>a[y+1]:
         a[y],a[y+1]=a[y+1],a[y]
print(a)
