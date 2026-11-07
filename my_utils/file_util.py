def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        context = f.read()
        print("文件内容如下：")
        print(context)
    except  Exception as e:
        print("文件不存在，请重新操作")
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    print_file_info("D:/bill./text")

def append_to_info(file_name,data):
    f = open(file_name, 'a',encoding='UTF-8')
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    append_to_info("D:/billl.text","furina")