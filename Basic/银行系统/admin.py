import time
from atm import ATM


class Admin(object):

    admin  = 'admin'
    passwd = 'admin'

    # 登录界面
    def printLoginView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*                                                 *")
        print("*                                                 *")
        print("*                                                 *")
        print("*              Welcome to Xs'Bank                 *")
        print("*                                                 *")
        print("*                                                 *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")

    # 验证登录
    def logCheck(self):
        if self.admin != input("$ 请输入登录名："):
            print("没有此用户")
            return -1
        elif self.passwd != input("$ 请输入密码：  "):
            print("密码错误！")
            return -1
        else:
            print("Login Successful...")
            time.sleep(1)
            return 0





    # 功能界面
    def printFuncView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*           查询 (1)           开户 (2)            *")
        print("*           取款 (3)           存款 (4)            *")
        print("*           转账 (5)           改密 (6)            *")
        print("*           锁定 (7)           解锁 (8)            *")
        print("*           补卡 (9)           销户 (0)            *")
        print("*                     退出(q)                      *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")

