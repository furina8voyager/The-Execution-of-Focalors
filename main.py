# import warnings
# warnings.filterwarnings("ignore")
import math
import re
import os
# #将数字转换成字符串
# num_str = str(11)
# print(type(num_str), num_str)
# ##字符串转换数字
# float_st = str(1.14514)
# print(type(float_st), float_st)
# int_st = str(11)
# print(type(int_st), int_st)
# ##字符串转换成数字
# num1 = int("32")
# print(type(num1), num1)
# ##字符串转换成浮点数
# num2 = float("12.3454")
# print(type(num2), num2)
# ##整数转换成浮点数
# float_num = float(11)
# print(type(float_num), float_num)
# ##浮点数转换成整数
# int_num = int(1.9678)
# print(type(int_num), int_num)
# ##算数运算符
# #print("1+1=",1+1)
# name = "voyager"
# age = 18
# team = 1.88
# massage = "我是：%s,年龄是:%d,来自：%f" %(name,age,team)
# print(massage)
# num1 = 78
# num2 = 7.891
# print(f"5宽1精度:{num1:5.1f}")
# print(f"18宽7精度:{num2:18.7f}")
# #股价报价小程序（超级简陋版）
# product = "Astral Crystal Cargo  Unit"
# stock_price = 3240
# stock_code = 2602047
# stock_price_daily_growth_factor = 1.62
# growth_days = 1
# finally_price = stock_price * (stock_price_daily_growth_factor ** growth_days)
# print(f"产品名：{product},股票代码：{stock_code:8d},当前股价：{stock_price:8.2f}元/股")
# print(f"相比昨日增长：{stock_price_daily_growth_factor:3.8f},增长时间:{growth_days:2d}天")
# print(f"最新股价:{finally_price:8.4f}元/股")

# print("欢迎来到暴雨基金会")
# user_name = input("请输入用户名：")
# user_type = input("请输入您的身份：")
# #num  = int(num)
# print(f"尊敬的：{user_name:}您好,您的身份为：{user_type},请保管好随身物品")
# age = int(input("请输入您的年龄："))
# if age > 18:
#     print("您已成年，请交30元门票")
# else:
#     print("年龄不够，可以免费进入")
# print("祝您游玩愉快")

# import random
# num = random.randint(1,10)
# max_attempts = 3
# for attempt in range(1, max_attempts + 1):
#     guess = int(input(f"请输入第{attempt}次猜想数："))
#     if guess == num:
#         print(f"恭喜你，第{attempt}次就猜对了！")
#         break
#     elif guess > num:
#         print("猜测过大，请重新猜测")
#     else:
#         print("猜测过小，请重新猜测")
# else:
#     print(f"机会耗尽,正确答案为：{num}")
# print("今天发放年终奖，但需要满足以下条件")
# work_time = 9
# rution = 1
# level =5
# onboarding_time = int(input("入职时长："))
# job_level = int(input("工作职级："))
# if int(input("今年工作时长：")) >= work_time:
#     print("可以获得年终奖")
#     if onboarding_time >= rution or job_level >= level:
#         if onboarding_time >= rution and job_level >= level:
#             print("可以获得额外大礼包")
#         else:
#             print("可以获得双份")
#     else:
#         print("只可以领取一份")
# else:
#     print("感谢你今年对公司的付出，请来年继续努力")

# i = 1
# sum = 0
# while i<100:
#     sum += i
#     i += 1
# print(f"从1加到100的和为：{sum}")
# import random
# num = random.randint(1,100)
# tempet,guess = 0
# while guess != num:
#     guess = int(input("请输入猜测："))
#     tempet += 1
#     if guess < num:
#         print("猜测过小，猜测错误，请重新猜测，机会剩余...")
#     elif guess > num:
#         print("猜测过大，猜测错误，请重新猜测，机会剩余...")
#     else:
#         print("猜测正确")
#     while guess == num:
#         break
# print(f"本次共猜测：{tempet}次")

# i = 1
# while i<=9:
#     j = 1
#     while j<=i:
#         print(f"{i}*{j} = {j*i}\t",end="")
#         j +=1
#     i +=1
#     print()

# name = 'voyager&furina'
# count = 0
# for x in name:
#     if x == 'a':
#         count += 1
# print(f"{name}中共含有：{count}个a\t",end="")

# money = 10000
# import random
# for i in range(1,21):
#     if money<1000:
#         print("工资不足，停止发放")
#         continue
#     num = random.randint(1,10)
#     if num>=5:
#         money -=1000
#         print(f"绩效分:{num}，向员工:{i}发放工资1000元，账户余额：{money}")
#     else:
#         print(f"员工：{i},绩效分:{num}，低于5，不发工资，下是一位")
# print("工资已经发完，请下个月再来领取")

# def add(a,b):
#     result = a + b
#     return result
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# x=add(a, b)
# print(x)

# def temperature(a):
#     print("欢迎来到圣罗夫基金会！请出示您的健康码，并配合测量体温")
#     if 36.0<=a<=37.2:
#         print(f"经过测量，您的体温为：{a},温度正常请进")
#     else:
#         print(f"经过测量，您的体温为：{a}，体温不正常，请隔离")
# while True:
#     try:
#         a = float(input("测量体温："))
#         break
#     except ValueError:
#         print("系统错误，请重新测量！")
# temperature(a)

# money=0
# user_name = input("请输入用户名：")
# def panel1():
#     print("--------------查询余额--------------")
#     print(f"{user_name},您好，您的余额为{money}元")
# def panel2():
#     print("----------------存款---------------")
#     global money
#     num1 = int(input("请输入存款金额："))
#     money += num1
#     print(f"{user_name},您好，您存款{money}元成功")
# def panel3():
#     global money
#     print("----------------取款---------------")
#     num2=int(input("请输入取款金额："))
#     money -= num2
#     if money <= 0:
#         print("余额不足无法取款，请重新操作")
#     else:
#         print(f"{user_name},您好，取款{money}成功")
# def panel4():
#     return
# def main():
#     print("-----------------主菜单-------------------")
#     print(f"{user_name}，您好，欢迎来到黑马银行ATM，请选择操作：")
#     print("查询余额\t【请输入1】")
#     print("存款\t\t【请输入2】")
#     print("取款\t\t【请输入3】")
#     print("退出\t\t【请输入4】")
#     return input("请输入您的选择：")
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         panel1()
#     elif keyboard_input == "2":
#         panel2()
#     elif keyboard_input == "3":
#         panel3()
#     elif keyboard_input == "4":
#         panel4()
#     else:
#         break

# list1 = [21,25,23,22,20]
# furina = [21,25,23,22,20]
# print(furina)
# list1.append(31)
# print(list1)
# list2 = [29,33,30]
# list1.extend(list2)
# print(list1)
# element = list1.pop(0)
# print(element)
# element = list1.pop(-1)
# print(element)
# list1.index(31)
# print(list1)
# list1.insert(2,114)
# print(list1)
# count = len(list1)
# print(count)

# a = 0
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# while a <len(list1):
#     element = list1[a]
#     if element % 2 == 0:
#         print(element)
#     a += 1
#     list2.append(element)
#
# for i in list1:
#     if i % 2 == 0:
#         print(i)
#     list2.append(element)

# truple1 = ('furina',18,['music','dance'])
# sit = truple1.index(18)
# name = truple1[0]
# print(f"年龄所在为：{sit}")
# print(f"学生姓名为:{name}")
# hobby_list = truple1[2]
# hobby_list.remove('dance')
# print(truple1)
# hobby_list.append('coding')
# print(truple1)

# a = 0
# str = "    furina  de fontaine     "
# while a <len(str):
#     print(str)
#     a += 1
# for b in str:
#     print(b)
# c = str.count("a")
# print(c)
# str1 = str.replace(" ","|")
# print(str1)
# str2 = str1.strip("|")
# print(str2)
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
# a = set()
# for i in my_list:
#     a.add(i)
# print(f"列表的内容为:{i}")
# print(f"遍历后的集合：{a}")

# def hannuota(n,source,target,help):
#     if n==1:
#         print(f"移动盘子{n} 从 {source} 到 {target}")
#         return 1
#     step1 = (hannuota(n - 1, source , help , target))
#     print(f"移动盘子{n} 从 {source} 到 {target}")
#     step2 = 1
#     step3 = (hannuota(n - 1, help  , target , source))
#     return step1 + step2 + step3
# if __name__ == '__main__':
#     while True:
#         try:
#             n = int(input("请输入汉诺塔的圆盘数量（正整数）："))
#             if n <= 0:
#                 print("错误：圆盘数量必须是正整数！请重新输入!")
#                 continue
#             elif n >=20:
#                 total_steps = 2 ** n - 1
#             break
#         except ValueError:
#             print("错误：请输入有效的数字！请重新输入!")
#     total_steps = hannuota(n, 'A', 'C', 'B')
#     print(f"移动 {n} 个圆盘的总步数：{total_steps}")

# my_dict = {"furina":{"部门":"舞蹈部","工资":3000,"级别":1},
#         "voyager":{"部门":"音乐部","工资":5000,"级别":2},
#         "cooper_wreath":{"部门":"理线学","工资":7000,"级别":3},
#         "cold_saturday":{"部门":"研发部","工资":4000,"级别":1},
#         "northern_ballad":{"部门":"舞蹈部","工资":6000,"级别":2}}
# print("全体员工中级别为1的工资加1000，全体员工级别加1")
# for name in my_dict:
#     a = my_dict[name]["级别"]
#     if a <= 1:
#         my_dict[name]["工资"] += 1000
#         print(f"{name} 涨薪后工资：{my_dict[name]['工资']}")
#         my_dict[name]["级别"] +=1
#         print(my_dict[name])
#     else:
#         my_dict[name]["级别"] +=1
#         print(f"{name} 级别增加后为：{my_dict[name]['级别']}")

# print(f"adaaf小于asaAf，结果是：{'adaaf' < 'asaAf'}")
# str1 = "d mnd nas daj dj jael"
# str2 = "fjhdjsldfha a  hwi iwh "
# str3 = str1 + str2
# print(str3)
#
# def func1():
#     print ("Hello World1")
#     num = 1/0
# def func2():
#     print ("Hello World2")
#     func1()
# def main():
#     try:
#         func2()
#         func1()
#     except Exception as e:
#         print (type(e))
#         print(f"出现{e}异常")
# main()

# import time
# print("Hello",end="")
# time.sleep(5)
# print("World",end="")
#
# import my_module001
# my_module001.test(3,90)

# from my_utils.str_util import str_reverse
# from my_utils.str_util import suber
# b = " gwfweuduwehdewhdehwdohwedfh,2,8"
# print(b)
# from my_utils.file_util import print_file_info
# c = ("D：//python.text")
# from my_utils.file_util import append_to_info
# c = ("D：//python.text",'I love furina')

# from pyecharts.charts import Line
# from pyecharts import options as opts  # 统一用别名导入，避免拼写错误
#
# line = Line()  # 创建折线图对象
# line.add_xaxis(["中国", "英国", "美国"])
# line.add_yaxis("GDP", [30, 20, 10])  # 参数用=
# line.set_global_opts(  # 方法名补全s
#     title_opts=opts.TitleOpts(title="GDP展示图", pos_left="center", pos_top="1%"),
#     legend_opts=opts.LegendOpts(is_show=True),
#     toolbox_opts=opts.ToolboxOpts(is_show=True),
#     visualmap_opts=opts.VisualMapOpts(is_show=True)
# )
# line.render("gdp_chart.html")

# class Student:
#     name = None
#     gender = None
#     age = None
#     nationality = None
#     native_place = None
# stu001 = Student()
# stu001.name = "芙宁娜"
# stu001.gender = "女"
# stu001.age = 18
# stu001.nationality = "提瓦特"
# stu001.native_place = "枫丹"
# print(stu001.name)
# print(stu001.gender)
# print(stu001.age)
# print(stu001.nationality)
# print(stu001.native_place)
#
# class Student:
#     name = None
#     def say_hi (self):
#         print(f'大家好，我是{self.name}')
# str001 = Student()
# str001.name = "furina"
# str001.say_hi()

# class clock:
#     id = None
#     price = None
#     def ring(self):
#         import winsound
#         winsound.Beep(2000,3000)

# class Student:
#     def __init__(self, name,age,place):
#         self.name = name
#         self.age = age
#         self.place = place
#     def __str__(self):
#         return f"[学生姓名：{self.name},年龄：{self.age},地址：{self.place}]"
#
# students=[]
# # print(*students)
# for i in range(11):
#     print(f"开始录入第{i+1}位学生")
#     name = input("请输入学生姓名：")
#     age = int(input("请输入学生年龄："))
#     place = input("请输入学生地址：")
#     stu = Student(name,age,place)
#     students.append(stu)
#     # students.append(stu.age)
#     # students.append(stu.place)
#     print(f"第{i+1}位学生已经录取完成，信息为：{stu}，请进行下一位学生的录入")
# for id, stu in enumerate(students, 1):
#     print(f"学生{id}：{stu}")
#
# class Phone:
#     def __init__(self):
#         self.__is__5g__enable = False
#     def __check__5g(self):
#         if self.__is__5g__enable == True:
#             print("5g开启")
#         else:
#             print("5g关闭，切换为4g")
#     def call__by__5g(self):
#         self.__check__5g()
#         print("正在通话中")
# phone = Phone()
# phone.call__by__5g()

# a = "nononononononon"
# # result = re.match("python", a)
# # print(result.span())
# # print(result.group())
# result = re.search("no", a)
# print(result.span())
# print(result.group())
# result = re.findall("no", a)
# print(result)

# r = '^[1-9][0-9]{4,10}$'
# s = '123456789'
# print(re.findall(r, s))

# r = ('^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$')
# def func():
#     print(os.listdir(" "))
#     print(os.path.isdir(""))
#     print(os.path.exists(""))
#
# def get_files_return_from_dir(path):
#     file.list = []
#     if os.path.exists(path):
#         for f in os.listdir(path):
#             new.path = path += "/" + f
#             if os.path.isdir(new_path):
#                 file_list += get_files_return_from_dir(new_path)
#             else:
#                 file_list.append(new_path)
#     else:
#         print(f"指定的目录为：{path}，不存在")
#         return []
#     return file_list
#
# if __name__ == "__main__":
#     print(get_files_return_from_dir(""))

# n = int(input("请输入台座数："))
# def func(n):
#     y = n*(n-1)*(n-2)/6
#     if n>=3:
#         return f"缇里西庇俄丝们最多可以开启{y}道门扉"
#     else:
#         return "缇里西庇俄丝至少为三人"
# print(func(n))

# import math
# def main():
#     import sys
#     input = sys.stdin.read().split()
#     i = 0
#     T = int(input[i])
#     i += 1
#     a, b, c = map(float, input().split())
#     S = math.sqrt(a * a * b * b + a * a * c * c + b * b * c * c - a ** 4 - b ** 4 - c ** 4) / 2
#     def square_area(L):
#         x = (2*S*L)/(L*L+2*S)
#         return x*x
#     max_square_area = max(square_area(a), square_area(b), square_area(c))
#     print(max_square_area)
# if __name__ == '__main__':
#     main()

# start_tu = {"A":["B","C","D"],"B":["D","E"],"C":["D"],"D":["E"],"E": []}
# MOD  = 998244353
# def main():
#     import sys
#     input = sys.stdin.read().strip()
#     n = int(input)
#     if n == 0:
#         print(0)
#         return
#     a = [0]*(n+1)
#     a[1] = 1
#     for p in range(2,n+1):
#         a[p] = MOD - MOD//p*a[MOD%p]%MOD
#     b = 0
#     for i in range(1, n + 1):
#         b = b + a[i]
#     result = n * b % MOD
#     print(result)
# if __name__ == '__main__':
#      main()

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# cut = 0
# num = 0
# while True:
#     if is_prime(num):
#         cut += 1
#         if cut == 2025:
#             print(num)
#             break
#     num +=1

#
# p = 0
# n = int(data[p])
# p += 1
# a = list(map(int, data[p:p+n]))
# p += n
# a.insert(0, 0)
# s = [0] * (n + 1)
# for i in range(1, n+1):
#     s[i] = s[i-1] + a[i]
# q = int(data[p])
# p += 1
# res = []
# for _ in range(q):
#     l = int(data[p])
#     r = int(data[p+1])
#     p+= 2
# print('\n'.join(res))

for i in range(1,10):
    if i <= 5:
        a = i;
    else:
        a =10 - i;
    b =5 - a;
    print(' '*b+' *'*a);

def fn2(nums):
    if nums % 2 == 0:
        return True
    else:
        return False
lst = [1,2,3,4,5,6,7,8,9]
print(filter(fn2,lst))

a = ["VOYAGER","FURINA"]
for i in a:
    print(i)

x = [1,2,3,4,5,6,7,8,9]
x.pop()
print(x)
x.pop(0)
print(x)

import random
lst = [1,2,3,4,5,6,7,8,9]
random.shuffle(lst)

course = "课程","Python"
print(course)
a_tuple = ()
a = ("课程")
print(a)
print(type(a))
b = ("课程")
print(b)
print(type(b))

random_number = (random.randint(1,10) for i in range(10))
print(random_number)
random_number = tuple(random_number)
print("转化后：",random_number)

number = (i for i in range(10))
print(number.__next__())
print(number.__next__())
print(number.__next__())

V1 = ["乒乓球","羽毛球","跳水"]
V2 = ["陈梦","陈雨霏","全红蝉"]
V3 = dict(zip(V1,V2))
print(V3)

dictionary = dict(zip(乒乓球 = "陈梦",羽毛球="陈雨霏",跳水="全红蝉"))
dictionary["游泳"]="张雨霏"
print(dictionary)