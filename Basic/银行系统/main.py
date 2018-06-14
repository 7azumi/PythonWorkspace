'''
用户
类名：Person
属性：姓名 卡号 手机 身份证号
行为：


卡
类名：Card
属性：卡号 密码 余额
行为：


ATM取款机
类名：ATM
属性：
行为：开户 查询 取款 存款 转账 改密 锁定 解锁 补卡 销户 退出


ATM界面
类名：View
属性：
行为：用户登录 用户界面 操作功能界面


'''
from admin import Admin
from atm import ATM
import pickle
import os


# 文件保存路径
filePath = os.path.join(os.getcwd(), "allUsers.txt")
# allUsers = {}


def main():
    try:
        f = open(filePath, "rb")
        allUsers = pickle.load(f)
    except EOFError:
        allUsers = {}

    # 初始化实例
    admin = Admin()
    atm = ATM(allUsers)

    # 登录界面
    admin.printLoginView()
    # 验证信息
    if admin.logCheck():
        return -1
    # 进入操作界面
    else: admin.printFuncView()

    while 1:
        option = input("$ Please input your choice： ")
        if option == 'q':
            print("Thanks for support! Bye~")
            # 将用户信息保存在本地
            f = open(filePath, "wb")
            pickle.dump(atm.allUsers, f)
            f.close()

            return 0
        # 验证身份

        # 进行操作
        optionSel(atm, option)


def optionSel(object, option):

    if option == '1':
        print("查询")
        object.search()

    elif option == '2':
        print("开户")
        object.createUser()

    elif option == '3':
        print("取款")
        object.getMoney()

    elif option == '4':
        print("存款")
        object.saveMoney()

    elif option == '5':
        print("转账")
        object.transfer()

    elif option == '6':
        print("改密")
        object.changePasswd()

    elif option == '7':
        print("锁定")
        object.lock()

    elif option == '8':
        print("解锁")
        object.unlock()

    elif option == '9':
        print("补卡")
        object.regetcard()

    elif option == '0':
        print("销户")
        object.delete()


if __name__ == '__main__':
    main()