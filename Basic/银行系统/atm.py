from user import User
from card import Card

import random


class ATM(object):

    # 用户集合
    def __init__(self, allUsers):
        self.allUsers = allUsers


        # 开户
    def createUser(self):
        name = input("Please input your name： ")
        idnum = input("Please input your ID number：")
        tel = input("Please input your tel number：")
        premoney = input("The total amount of deposit: ")
        if int(premoney) < 0:
            print("----Error for input！operation aborted...")
        else:
            passwd = int(input("Plaese input your password: "))
            if self.checkPasswd(passwd):
                cardId = self.randCardId()
                # 生成用户信息实例
                card = Card(cardId, passwd, premoney)
                user = User(name, card, idnum, tel)
                self.allUsers[cardId] = user
                print("----Create account successful!")
                print("----Your Card ID is ",cardId)



    # 查询
    def search(self):
        # 验证身份
        curuser = self.checkUser()
        # 展示数据
        if curuser:
            print("----Name:", curuser.name)
            print("----Card ID:",curuser.card.id)
            print("----Money:", curuser.card.money)


    # 存钱
    def getMoney(self):
        # 验证身份
        curuser = self.checkUser()
        # 存钱
        if curuser:
            cash = int(input("$ The amount of cash you want to store:"))
            curuser.card.money += cash
            print("----Your deposit:",curuser.card.money)

    # 取钱
    def saveMoney(self):
        # 验证身份
        curuser = self.checkUser()
        # 取钱
        if curuser:
            cash = int(input("$ The amount of cash you want to get:"))
            if cash > curuser.card.money:
                print("----You don't have enough money!")
            else:
                curuser.card.money -= cash
                print("----Your deposit:", curuser.card.money)


    def transfer(self):
        # 验证身份
        curuser = self.checkUser()


    def changePasswd(self):
        # 验证身份
        curuser = self.checkUser()


    def lock(self):
        # 身份验证
        curuser = self.checkUser()
        # 锁定账户
        if curuser:
            print("----locked successful!")
            curuser.card.lock = True

    def unlock(self):
        # 身份验证
        cardnum = input("Please input your card ID: ")
        user = self.allUsers.get(cardnum)
        if not user:
            print("----ID not found!")
            return 0
        # 如果被锁定则解锁
        elif user.card.lock:
            if self.checkPasswd(user.card.passwd):
                print("----unlocked successful!")
                user.card.lock = False
        else: print("----The card dosen't locked!")


    def regetCard(self):
        pass

    # 销户
    def deleteUser(self):
        pass

    # 身份验证
    def checkUser(self):
        cardnum = input("Please input your card ID: ")
        user = self.allUsers.get(cardnum)
        if not user:
            print("----ID not found!")
            return 0
        elif user.card.lock:
            print("----This card has been locked!")
            return 0
        elif self.checkPasswd(user.card.passwd):
            return user

    # 校验密码
    def checkPasswd(self, pwd):
        checkpwd = int(input("Please input your password: "))
        if checkpwd != pwd:
            print("----Password wrong!")
            return 0
        return 1

    # 生成随机卡号
    def randCardId(self):
        while True:
            str = ''
            for i in range(0,6):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str += ch
            if not self.allUsers.get(str):
                return str