#1.开户
#开户逻辑
bank={}#空的银行账户数据库
#'Frank': {'account': 10936377, 'password': '123', 'country': '中国', 'province': '山东', 'street': '蓝翔', 'door': '001'},
bank_name="中国银行M78分行"
#传入参数添加到字典里面
def bank_add(account,username,password,country,province,street,door):
    if username in bank:#说明用户已存在
        return 3
    elif len(bank)>=100:
        return 2
    else:
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的用户名")
    password=input("请输入您的用户密码")
    print("下面请输入你的详细地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add == 3:
        print("数据库已满请到其他银行开户")
    elif add ==2:
        print("请输入其他用户名")
    elif add== 1:
        print("开户成功,下面是你的详细信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
index=int(input("请输入您的操作"))

# 2.存钱
def saveMoney(account,money):
    if account in bank.keys():
        bank[account][3] += money
        bank[account]={
            "account": account,
            "money": 0,
        }
        return True
    else:
        return False
def saveMoney():
    account = input("请输入您的账户")
    username=input("请输入您的用户名")
    password=input("请输入您的用户密码")
    print("下面请输入你的存钱数")
    money=input("\t\t请输入存钱数")

    save=saveMoney(account,username,password,money)
    if save == 3:
        print("数据库已满请到其他银行开户")
    elif save ==2:
        print("请输入其他用户名")
    elif save== 1:
        print("开户成功,下面是你的详细信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    存入金额：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, money, bank[username]["money"]))
index=int(input("请输入您的操作"))

# 3.取钱
def drawMoney(account,password,money,user):
    if account in user.keys():
        if user[account][1] == password:
            if money<=user[account][3]:
                user[account][3]-=money
                bank[account] = {
                    "password":password,
                    "money": 0,
                }
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def drawMoney():
    account = input("请输入您的账户")
    username=input("请输入您的用户名")
    password=input("请输入您的用户密码")
    print("下面请输入你的取钱数")
    money=input("\t\t请输入取钱数")

    draw=drawMoney(account,username,password,money)
    if draw == 3:
        print("钱不够")
    elif draw ==2:
        print("密码不对")
    elif draw== 1:
        print("账户不存在")
    elif draw==0:
        print("正常")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    取出金额：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, money, bank[username]["money"]))
index=int(input("请输入您的操作"))
# 4.转账
def transfer(account,account1,password,money,user):
    if account in user.keys() and account1 in user.keys():
        if password == user[account][1]:
            if money <= user[account][3]:
                user[account][3] -= money
                user[account1][3] += money
                bank[account] = {
                    "account": account,
                    "account1":account1,
                    "password": password,
                    "money": 0
                }
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def transfer():
    account = input("请输入您的账户")
    username = input("请输入您的用户名")
    password = input("请输入您的用户密码")
    print("下面请输入转账信息")
    account1 = input("请输入您要转入金额的账户")
    money = input("\t\t请输入取钱数")

    transf = transfer(account, username, password, money)
    if transf == 3:
        print("钱不够")
    elif transf == 2:
        print("账户不对")
    elif transf == 1:
        print("密码不对")
    elif transf == 0:
        print("正常")
        info = '''
                    ------------个人信息------------
                    用户名：%s
                    转出账户:%s
                    转入账号：%s
                    转出金额：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, account,money, bank[username]["money"]))
index = int(input("请输入您的操作"))

# 5.查询
def inquire(account,password,user):
    if account in user.keys():
        if user[account][1] == password:
            return
        else:
            return 2
    else:
        return 1

def inquire():
    account = input("请输入您的账户")
    username = input("请输入您的用户名")
    password = input("请输入您的用户密码")
    print("下面请输入查询信息")
    account = input("\t\t请输入查询账户")

    inquir = inquire(account, username, password)
    if inquir == 2:
        print("账户不存在")
    elif inquir == 1:
        print("密码错误")
    elif inquir == 0:
        print("正常")
        info = '''
                    ------------个人信息------------
                    当前账户：%s
                    姓名：%s
                    余额：%s
                    用户居住地址：%s
                    当前账户的开户行：%s
                    print("当前账户：",account)
        # 每个元素都可传入%
        print(info % (account,username, bank[username]["money"],address, bank))
index = int(input("请输入您的操作"))
