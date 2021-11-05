import time
from threading import Thread

#篮子
eggtart_basket=500

class Cooker(Thread):
    cooker_name=""
    eggtart_count = 0
    def run(self) -> None:
        global eggtart_basket
        while True:
            if eggtart_basket<500:
                self.eggtart_count=self.eggtart_count+1
                eggtart_basket+=1
            else:
                time.sleep(3)
                self.eggtart_count = self.eggtart_count + 1
                eggtart_basket += 1
            print(self.cooker_name,"做了",self.eggtart_count,"个蛋挞，工资是",self.eggtart_count*12)

class Customer(Thread):
    customer_name=""
    eggtart_num=0

    def run(self)->None:
        global eggtart_basket
        while True:
            if eggtart_basket>=0:
                eggtart_basket-=1
                self.eggtart_num+=1
            else:
                time.sleep(3)
                eggtart_basket -= 1
                self.eggtart_num += 1
            print(self.customer_name, "买了", self.eggtart_num, "个蛋挞")

            if self.eggtart_num*3<=30 and eggtart_basket>0:
                print(self.customer_name,"买了",self.eggtart_num,"个蛋挞")
            else:
                break
            print(self.customer_name,"买了",self.eggtart_num,"个蛋挞")

c1=Cooker()
c2=Cooker()
c3=Cooker()

c1.cooker_name="厨师1"
c2.cooker_name="厨师2"
c3.cooker_name="厨师3"

c1.start()
c2.start()
c3.start()


p1=Customer()
p2=Customer()
p3=Customer()
p4=Customer()
p5=Customer()
p6=Customer()

p1.customer_name="奕小辰"
p2.customer_name="佳多"
p3.customer_name="思得"
p4.customer_name="志致"
p5.customer_name="君宇"
p6.customer_name="诗而"

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
