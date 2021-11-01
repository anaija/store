#分析一个水杯的属性和功能，使用类描述并创建对象

class cup:
    __high=""
    __volumee=""
    __color=""
    __material=""

    def setHigh(self,high):
        if high < 0 or high > 30:
            print("水杯高度输入错误")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    def setVolumee(self,volumee):
        if volumee<0 or volumee>350:
            print("水杯容积输入错误")
        else:
            self.__volumee=volumee
    def getVolumee(self):
        return self.__volumee

    def setColor(self,color):
        if color!="白" and color!="黑" and color!="银" and color!="绿" and color!="青" and color!="蓝" and color!="紫":
            print("水杯颜色输入错误")
        else:
            self.__color=color
    def getColor(self):
        return self.__color

    def setMaterial(self,material):
        if material!="塑料" and material!="玻璃" and material!="钢":
            print("水杯材质输入错误")
        else:
            self.__material=material
    def getMaterial(self):
        return  self.__material

    def Waterhoding(self,water):
        print("我装饮用物品：",water)

    def showme(self):
        print("我身高",self.__high,
              ",容量",self.__volumee,
              ",颜色为：", self.__color,
              ",我的材质是", self.__material,"特质的"
              )

c=cup()

c.setHigh(15)
c.setVolumee(220)
c.setColor("白")
c.setMaterial("塑料")
c.Waterhoding("咖啡")
c.showme()



#分析笔记本电脑
class computer:
    __size=""
    __price=""
    __cpu=""
    __memory=""
    __time=""

    def setSize(self,size):
        if size>7 or size<=0:
            print("电脑尺寸有问题，请重新输入！")
        else:
            self.__size=size
    def getSize(self):
        return self.__size

    def setPrice(self,price):
        if price<=0 or price>1000000:
            print("价格输入有误，请重新输入！")
        else:
            self.__price=price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        if cpu<0 or cpu>20000:
            print("cpu运行速度有误，请重新输入！")
        else:
            self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setMemory(self,memory):
        if memory!=64 and memory!=128 and memory!=256 and memory!=512 and memory!=1024:
            print("内存输入有误，请重新输入！")
        else:
            self.__memory=memory
    def getMemory(self):
        return self.__memory

    def setTime(self,time):
        if time<0 or time>5:
            print("待机时间错误，请重新调整！")
        else:
            self.__time=time
    def getTime(self):
        return self.__time

    def Typing(self,speed):
        print("我的打字速度：", speed)
    def Playgames(self,hour):
        print("东东玩游戏已经", hour,"小时了")
    def Watchvideos(self,hour):
        print("猪八戒正在睡觉！已经睡了", hour, "小时！")

    def showme(self):
        print("我", self.__size,"寸",
               ",价格", self.__price,"元",
               ",cpu运行", self.__cpu,"hz",
               ",内存大小", self.__memory,
               ",待机时长", self.__time,"小时"
               )
c = computer()

c.setSize(3)
c.setPrice(7000)
c.setCpu(4)
c.setMemory(1024)
c.setTime(2)

c.Typing(50)
c.Playgames(2)
c.Watchvideos(1)

c.showme()



#对象版的中国工商银行系统

class bank:
    __account = ""
    __username = ""
    __password = ""
    __country = ""
    __province = ""
    __street = ""
    __door = ""
    __money = ""

    def setAccount(self, account):
        if len(account) != 8:
            print("账号必须为8位数字")
        elif not account.isdigit():
            print("账号不允许有非数字字符")
        else:
            self.__account = account

    def getAccount(self):
        return self.__account

    def setUsername(self, username):
        if username == "":
            print("用户名不能为空，请重新输入！")
        else:
            self.__username = username

    def getUsername(self):
        return self.__username

    def setPassword(self, password):
        if not password.isdigit():
            print("密码必须为数字，请重新输入！")
        else:
            self.__password = password

    def getPassword(self):
        return self.__password

    def setCountry(self, country):
        if country != "中国":
            print("只允许中国用户输入！")
        else:
            self.__country = country

    def getCountry(self):
        return self.__country

    def setProvince(self, province):
        if province != "北京" and province != "上海" and province != "广东" and province != "深圳" and province != "青海" and province != "台湾" and province != "澳门" and province != "陕西" and province != "山西" and province != "浙江" and province != "湖南" and province != "海南" and province != "安徽" and province != "贵州" and province != "河南" and province != "湖北" and province != "宁夏" and province != "青藏" and province != "广西" and province != "哈尔滨" and province != "甘肃":
            print("只允许中国用户输入！")
        else:
            self.__province = province

    def getProvince(self):
        return self.__province

    def setStreet(self, street):
        if street != "":
            self.__street = street
        else:
            print("请输入你所在的街道！")
    def getStreet(self):
        return self.__street

    def setDoor(self, door):
        if door != "":
            self.__door = door
        else:
            print("请输入您的门牌号！")


    def getDoor(self):
        return self.__door

    def setMoney(self, money):
        if money < 0:
            print("金额输入错误，请重新输入！")
        else:
            self.__money = money

    def getMoney(self):
        return self.__money

    def openaccount(self,open_account):
        print(self.__username,"我的账号为：",open_account, "我的密码为：",self.__password)

    def savemoney(self,save_money):
        print(self.__username,"我存入金额为",save_money, "元")

    def drawmoney(self,drawmoney):
        print(self.__username,"取出金额为",drawmoney, "元")

    def transfer(self,transfer_money):
        print(self.__username,"转账金额为",transfer_money, "元")

    def query(self,address,e_money):
        print(self.__username,"的居住地址为",address, "我卡內余额为：", e_money)

    def getover(self):
        print("ByeBye!")

    def showme(self):
        print("我的账号为", self.__account,
              "密码是", self.__username,
              "住址为",self.__country,
              self.__province,
              self.__street,
              self.__door,
              )

b = bank()

b.setAccount("27685770")
b.setUsername("anaija")
b.setPassword("657432")
b.setCountry("中国")
b.setProvince("上海")
b.setStreet("沙河")
b.setDoor(374)
b.setMoney(1000000)

b.openaccount("anaija1")
b.savemoney(100000)
b.drawmoney(10000)
b.transfer(10000)
b.query("北京市海淀区",1000)
b.showme()
