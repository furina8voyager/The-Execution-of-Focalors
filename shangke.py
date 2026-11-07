# # # # # # # # # # # # score = int(input('请输入一个整数:'))
# # # # # # # # # # # # degree = 'DCBAAF'
# # # # # # # # # # # # if score > 100 or score < 0:
# # # # # # # # # # # #     print('wrong score.must between 0and 100')
# # # # # # # # # # # # else:
# # # # # # # # # # # #     index = (score-60)//10
# # # # # # # # # # # #     if index >= 0:
# # # # # # # # # # # #         print(degree[index])
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print(degree[-1])
# # # # # # # # # # #
# # # # # # # # # # # num = int(input("输入一个数字："))
# # # # # # # # # # # if num%2 == 0:
# # # # # # # # # # #     if num%3 == 0:
# # # # # # # # # # #         if num%5 == 0:
# # # # # # # # # # #             print("该数可以被2和3整除")
# # # # # # # # # # #     else:
# # # # # # # # # # #         if num%3 == 0:
# # # # # # # # # # #             print("该数可以被3整除但不能被2整除")
# # # # # # # # # # #         else:
# # # # # # # # # # #             print("这个数不能被2，3整除")
# # # # # # # # # #
# # # # # # # # # # scores =  [33,32,41,25,39,43,27,38,40]
# # # # # # # # # # games = 0
# # # # # # # # # # for score in scores:
# # # # # # # # # #     if score < 30:
# # # # # # # # # #         continue
# # # # # # # # # #     games+=1
# # # # # # # # # # print("有%d场得分超过30分",games)
# # # # # # # # # #
# # # # # # # # # # i = 0
# # # # # # # # # # while i <= 10:
# # # # # # # # # #     i+=1
# # # # # # # # # #     if i == 3:
# # # # # # # # # #         continue
# # # # # # # # # #     print(i)
# # # # # # # # #
# # # # # # # # # print("测试1")
# # # # # # # # # for i in range(1,11):
# # # # # # # # #     if i == 5:
# # # # # # # # #         break
# # # # # # # # #     print(i,end=", ")
# # # # # # # # # print()
# # # # # # # # # print("测试2")
# # # # # # # # # for j in range(0,11,2):
# # # # # # # # #     if j == 5:
# # # # # # # # #         break
# # # # # # # # #     print(j,end=", ")
# # # # # # # # # print()
# # # # # # # # #
# # # # # # # # # answer = 30
# # # # # # # # # guess = 0
# # # # # # # # # while guess != answer:
# # # # # # # # #     guess = int(input("猜一猜1-100间的数字="))
# # # # # # # # #     if guess <= answer:
# # # # # # # # #         print("猜小了")
# # # # # # # # #     if guess >= answer:
# # # # # # # # #         print("猜大了")
# # # # # # # # #     else:
# # # # # # # # #         print("恭喜猜对了")
# # # # # # # # #
# # # # # # # # # for i in range(1,10):
# # # # # # # # #     for j in range(1,i+1):
# # # # # # # # #         print("{0}*{1} = {2}".format(i,j,i*j),end=' ')
# # # # # # # # # print()
# # # # # # # #
# # # # # # # # from math import pi
# # # # # # # # area = lambda r:pi*r**2
# # # # # # # # r = 10
# # # # # # # # print(area(r))
# # # # # # # # sum = lambda a,b:a+b
# # # # # # # # print(sum(10,20))
# # # # # # # #
# # # # # # # # g = lambda x,y = 2,z = 3:x+y+z
# # # # # # # # print(g(1))
# # # # # # # # print(g(2,z = 4,y = 5))
# # # # # # # #
# # # # # # # # def  fact(n):
# # # # # # # #     if n == 0:
# # # # # # # #         return 1
# # # # # # # #     return n*fact(n-1)
# # # # # # # # print(fact(5))
# # # # # # # #
# # # # # # # # message = "furina"
# # # # # # # # def f_demo():
# # # # # # # #     print(message)
# # # # # # # # f_demo()
# # # # # # # # print(message)
# # # # # # # #
# # # # # # #
# # # # # # # message = "de fontain"
# # # # # # # print("furina "+message)
# # # # # # # def f_demo():
# # # # # # #     message = "voyager"
# # # # # # #     print("Hello!"+message)
# # # # # # # f_demo()
# # # # # # # print("12345678"+message)
# # # # # # #
# # # # # # # def produce():
# # # # # # #     for i in range(19999):
# # # # # # #         yield "生产了第%s件衣服"%i
# # # # # # # product_g = produce()
# # # # # # # print(product_g.__next__())
# # # # # # # print(product_g.__next__())
# # # # # # # print(product_g.__next__())
# # # # # # # num = 0
# # # # # # # for i in product_g:
# # # # # # #     print(i)
# # # # # # #     num += 1
# # # # # # #     if num == 10:
# # # # # # #         break
# # # # # # #
# # # # # # # name = input("Name:")
# # # # # # # age = input("Age:")
# # # # # # # job = input("Job:")
# # # # # # # hobby = input("Hobby:")
# # # # # # # print(name)
# # # # # # # print(age)
# # # # # # # print(job)
# # # # # # # print(hobby)
# # # # # # # info =(name, age, job, hobby)
# # # # # # # print(info)
# # # # # #
# # # # # # path = "C:\windows\netplan.exe"
# # # # # # print(path)
# # # # # # path = r"C:\windows\netplan.exe"
# # # # # # print(path)
# # # # #
# # # # # print(1,3,5,7,sep = "\t")
# # # # # print(1,3,5,7,sep = " ")
# # # # # for i in range(18):
# # # # #     print(i,end = ' ')
# # # # #     print(i,end = '')
# # # # #     print(i)
# # # # #
# # # #
# # # # str1 = "人生苦难"
# # # # substr1 = str1[1]
# # # # substr2 = substr1[5:]
# # # # substr3 = substr2[:5]
# # # # substr4 = substr3[2:5]
# # # # pr int(":",str1)
# # # # print(substr1 + "\n" + substr2 + "\n" + substr3 + "\n" + substr4)
# # # #
# # # # str1 = "12324455"
# # # # length = len(str1)
# # # # print(length)
# # # #
# # #
# # # print('{0},{1}'.format('hello','world'))
# # # print('{0} ,{1},{0}'.format('hello','world'))
# # # print('{1},{1},{0}'.format('hello','world'))
# # # print('{a},{b},{a}'.format(b='hello',a='world'))
# # #
# # # width = 18
# # # pre = 4
# # # value = 11/3
# # # print(f"result:{value}.{pre}")
# # # print(f"result:{value}.{pre}")
# # #
# # # s = "apple,peach,banana,pear"
# # # print(s.split(","))
# # # print(s.partition(","))
# # # print(s.rpartition(','))
# # # print(s.rpartition('banbana'))
# # #
# # # s = "2017-10-31"
# # # t = s.split("-")
# # # print(t)
# # # print(list(map(int,t)))
# # #
# # # s = "What is your name?"
# # # print(s.lower())
# # # print(s.upper())
# # # print(s.capitalize())
# # # print(s.title())
# # # print(s.swapcase())
# # #
# # # s = "中国，中国"
# # # print(s)
# # # s2 = s.replace("中国","中华人民共和国")
# # # print(s2)
# # #
# # # print('hello world!'.center(20))
# # # print('hello world!'.center(20,"="))
# # # print('hello world!'.ljust(20,"="))
# # # print('hello world!'.rjust(20,"="))
# # #
# # # import re
# # # print(re.search('www','www.baidu.com').span())
# # # print(re.search('com','www.baidu.com').span())
# # # print(re.match('www','www.baidu.com').span())
# # # print(re.match('com','www.baidu.com').span())
# # import re
# # a = "123abc456"
# # print(re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(0))
# # print(re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(1))
# # print(re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(2))
# # print(re.match("([0-9]*)([a-z]*)([0-9]*)",a).group(3))
#
# #print(2/0)
#
# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("错误除0")
#
# try:
#     print('a'+2)
#     print(2/0)
# except ZeroDivisionError:
#     print('除0错误')
#
# try:
#     #print('a'+2)
#     print(2/0)
# except ZeroDivisionError:
#     print('除0错误')
# except TypeError:
#     print("操作类型不支持")
# try:
#     print(5+2)
# except TypeError:
#     print("操作类型不支持")
s1 = 'A'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(" try内没有异常")
finally:
    print('最后的清理模块')

f = open('测试文件.txt',mode = 'r',encoding = 'utf-8')
context = f.read()
print(context)
f.close()

import docx
from docx.shared import RGBColor
boldText = []
redText = []
doc = docx.Document()#这里有一个文件路径
for p in doc.paragraphs:
