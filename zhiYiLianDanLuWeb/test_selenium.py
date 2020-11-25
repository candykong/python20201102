#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import selenium
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions

from zhiYiLianDanLuWeb.test_base import Test_base


class TestLogin(Test_base):


    @pytest.mark.skip
    def test_selenium(self):
        self.driver.get("https://www.huo1818.com/login")
        action=ActionChains(self.driver)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[1]/input').send_keys('13107700873')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[2]/input').send_keys(
            '123456')
        click_xpath=self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/span[2]/button')
        action.click(click_xpath)
        # time.sleep(1)
        # def wait(x):
        #     return 1>0
        # WebDriverWait(self.driver,10).until(wait())
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.xPath,"xxxxx"))
        assert "炼丹炉-监控台-数据概览" in self.driver.title

    @pytest.mark.skip
    def test_touchaction(self):
        self.driver.get("https://www.baidu.com")
        touchaction=TouchActions(self.driver)
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el.send_keys('健身')
        el_search.click()
        touchaction.scroll_from_element(el,0,10000).perform()
        time.sleep(5)


    @pytest.mark.skip
    def test_switch_windows(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windows=self.driver.window_handles
        #切换窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.switch_to.window(windows[0])

    @pytest.mark.skip
    def test_switch_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to_default_content()

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://testerhome.com/")
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(1)

    def test_js_attribute(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly');a.value='2020-12-30'")
        time.sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date).value"))







if __name__ == '__main__':
    pytest.main()
