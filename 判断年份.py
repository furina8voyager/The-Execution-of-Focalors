a = int(input("请输入一个年份："))
if a <= 0:
    print("输入数据不合理，请重新输入")
else:
    if a % 4 ==0 and a % 100 != 0:
        print("是闰年")
    elif a % 400 == 0:
        print("是闰年")
    else:
        print("不是闰年")

