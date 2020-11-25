import os

from selenium import webdriver


class Test_base():
    # def setup(self):
    #     browers = os.getenv("brower")
    #     if browers == "firefox":
    #             self.driver = webdriver.Firefox()
    #     elif browers == "Chrome":
    #         option = webdriver.ChromeOptions()
    #         option.add_experimental_option('w3c', False)
    #         self.driver = webdriver.Chrome(options=option)
    #     else:
    #         self.driver = webdriver.PhantomJS()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(1)  # 每次打开页面动态等待页面加载出来，不用每次在打开页面中编写sleep


    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)


    def teardown(self):
        self.driver.quit()