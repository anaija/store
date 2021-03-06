练习1:华氏温度转换为摄氏温度。
提示:华氏温度到摄氏温度的转换公式为: $C=(F -32) )div 1.8$。
for i in range (5):       #此处为循环次数，可自由设置
	val = input ("请输入带温度标识符号的温度值（例如26C）:")
	if val[-1] in ['C','c']:              #判断是否为摄氏温度
		f = 1.8 * float(val[0:-1]) + 32
		print("转换后的温度为:%.2fF"%f)    #%f表示原值，默认小数点后五位；%.2f浮点数后保留两位小数
	elif val[-1] in ['F','f']:          #判断是否为华氏温度
		c = (float(val[0:-1]) - 32) / 1.8
		print("转换后的温度为:%.2fC"%c)  #%c整数转成对应的ASCII
	else:
		print("输入的温度格式有误，请重新输入")



练习2:输入圆的半径计算计算周长和面积。
import math #导入数学函数
#输入圆半径，求圆周长和圆面积
r=eval(input("请输入圆的半径："))    #获取输入半径的值;eval（）执行一个字符串表达式，并返回表达式的值
PI=math.pi
L=2*PI*r             #计算圆周长公式
S=PI*r**2            #计算面积公式
print("圆的周长为{:.2f},圆的面积为{:.2f}".format(L,S))   #format函数通过格式操作将任意类型转换成一个字符串



练习3:输入年份判断是闰年。
import math #导入数学函数
#输入圆半径，求圆周长和圆面积
r=eval(input("请输入圆的半径："))    #获取输入半径的值;eval（）执行一个字符串表达式，并返回表达式的值
PI=math.pi
L=2*PI*r             #计算圆周长公式
S=PI*r**2            #计算面积公式
print("圆的周长为{:.2f},圆的面积为{:.2f}".format(L,S))   #format函数通过格式操作将任意类型转换成一个字符串



练习4:英制单位英寸与公制单位厘米互换。
提示:需要键盘输入长度，需要键盘输入单位
#英寸与厘米转换器
choice = int(input("这里是英寸与厘米转换器。如需英寸转换为厘米，请按1；如需厘米转换为英寸，请按2。"))
if choice == 1:
    x = float(input("请输入需要转换的英寸数："))
    result = x * 2.54
    print("%f 英寸 = %.3f 厘米" %(x, result))
elif choice == 2:
    x = float(input("请输入需要转换的厘米数："))
    result = x / 2.54
    print("%f 厘米 = %.2f 英寸" %(x, result))
else:
    print("输入有误，请重新输入。")
    
    
    
练习5:百分制成绩转换为等级制成绩。
要求:如果输入的成绩在90分以上(含90分)输出A; 80分-90分(不含90分)输出B; 70分-80分(不含80分)输出C; 60分-70分(不含70分)输出D; 60分以下输出E。
score = int(input("请输入你的成绩："))
grade = ""
if score > 100 or score < 0:
    score = int(input("输入错误！请重新输入一个在 0-100 之间的数字："))
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print("分数为{0},等级为{1}".format(score, grade))
    
    
    
练习6:输入三条边长，如果能构成三角形就计算周长和面积
print('输入三角形的三条边，判断这是什么三角形。')
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
    # 如果仅是两个短边或者两个长边相等，就是等腰三角形！
    else:
        print('等腰三角形！')
# 如果满足勾股定理并且两个短边不相等，就是直角三角形！
elif li[0] ** 2 + li[1] ** 2 == li[2] ** 2 and li[0] != li[1]:
    print('直角三角形！')
# 如果仅满足两个短边之和大于最长边，就是普通三角形！，
else:
    print('普通三角形！')
