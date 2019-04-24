from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


EMAIL = 'test@test.com'
PASSWORD = '123456'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.broswer = webdriver.Chrome()
        self.wait = WebDriverWait(self.broswer, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def __del__(self):
        self.broswer.close()

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.broswer.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_geetest_button(self):
        '''
        获取初始验证按钮
        :return: 按钮对象
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        print(top, bottom, left, right)
        return (top, bottom, left, right)

    def crack(self):
        self.open()
        bt = self.get_geetest_button()
        bt.click()
        self.get_position()
        sleep(3)

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()