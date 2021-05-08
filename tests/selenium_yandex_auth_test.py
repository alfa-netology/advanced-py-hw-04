import unittest
import time
from selenium import webdriver

LOGIN = ''
PASSWORD = ''
CHROME_DRIVER = ''


class TestYandexAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER)

    def test_yandex_auth(self):
        self.driver.get('https://passport.yandex.ru/auth/')

        time.sleep(1)

        login_input = self.driver.find_element_by_name('login')
        login_input.send_keys(LOGIN)
        login_input.submit()
        
        time.sleep(1)

        password_input = self.driver.find_element_by_name('passwd')
        password_input.send_keys(PASSWORD)
        password_input.submit()

    def tearDown(self):
        self.driver.close()
