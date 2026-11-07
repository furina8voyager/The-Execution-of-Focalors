import time
from DrissionPage import ChromiumPage, ChromiumOptions
##官网：https://www.damai.cn/
##登录
login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
##抢票
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.searchtxt.ditem_0.461c75948m2QZy&id=1035663663342'

class Damai:
    # def __init__(self):
    #     self.status = 0
    #     self.page = ChromiumPage(
    #         browser_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    #     )
    #     self.page = ChromiumPage()
    #     self.page.set.window.max()

    def __init__(self):
        self.status = 0
        from DrissionPage import ChromiumOptions
        co = ChromiumOptions()
        co.auto_port()
        # 直接手动指定 Edge 路径，兼容所有版本
        co.set_browser_path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        self.page = ChromiumPage(co)
        self.page.set.window.max()

    def login(self):
        ##打开登录页面
        self.page.get(login_url)
        print('登陆账号')

        while self.page.title.find('大麦登录') != -1:
            time.sleep(1)

        ##打开抢票网页
        self.page.get(target_url)

    def enter_concert(self):
        print('打开浏览器，进入大麦网')
        self.page.get(target_url)
        self.login()   ##调用登录

        self.page.refresh()  ##刷新
        self.status = 2  ##登陆成
        print('登陆成功')

        ##下单
        def choose_ticket(self):
            if self.status == 2:
                print('=' * 30)
                print('开始进行日期及票价选择')
                while self.page.title.find('确认订单') == -1:
                    try:
                        self.page.ele('@class=buy-link').click()

                    except:
                        print('订单确认失败')

                    self.choice_seats()
                    print('选择成功')##选择购票逻辑

                    self.check_order()
                    print('下单成功')

        def  choice_seats(self):
            try:##提交订单
                while self.isElementExist('//span[text()="立即提交"]'):
                    time.sleep(0.5)
                    self.page.ele('xpath=//span[text()="立即提交"]').click()

                self.status = 3  ##提交后立刻更改状态

            except Exception as e:
                print('提交订单失败:',e)

        def isElementExist(self,element):
            ##判断元素是否存在
            flag =  True
            browser = self.page
            try:
                browser.ele(f'xpath={element}]')
                return flag
            except Exception as e:
                flag = False
                return flag

        def finish(self):##抢票成功，跑路
            self.page.quit()

if __name__ == '__main__':
    try:
        damai = Damai()
        damai.enter_concert()
        damai.choose_ticket()
    except Exception as e:
        print('程序异常:', e)
        print('关闭程序')