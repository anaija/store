import re      #导入正则表达式模块

#以只读方式打开文件
f = open("baidu_x_system.log", "r")

#建立一个空数据库
arr = {}      #用字典来存储IP跟访问次数

#num表示1-255之间的字串，\b为单词的词首或词尾锚定
num='\\b([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\b'
lines = f.readlines()
#遍历文件的每一行
for line in lines:
    pattern = re.compile(r'('+num+'\.){3}'+num)  #python中用“+”来连接字符串
    match = pattern.match(line)
    if match:
        ip = match.group()
    if ip in arr:
        arr[ip] += 1
    else:
        arr[ip]=1
f.close()

#排序输出
numList=list(set(arr.values())) #set集合这里是去重
numList.sort(reverse=True)   #reverse=True表示逆序，reverse=False表示顺序
for ipNum in numList:
    for ip in arr:
         if (ipNum==arr[ip]):
             print(ip + "--->" + str(arr[ip]))
