#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: test_weixin.py
# time: 2021/6/26 4:21 下午
import random
import yaml
import allure
import logging
from selenium import webdriver



class TestSelenium:
    '''
    setup
    '''
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        Base_Url = 'https://work.weixin.qq.com/'
        self.driver.get(Base_Url)
        logging.info('设置浏览器驱动，窗口最大化')

    def teardown(self):
        self.driver.quit()
        logging.info('关闭浏览器')

    # 添加成员
    @allure.story('添加联系人')
    @allure.title('添加成员')
    def test_add_contacts(self):
        with allure.step('读取cookie'):
            with open("./datas/cookies.yaml", encoding='UTF-8') as f:
                cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        logging.info('添加cookie')

        with allure.step('进入企业微信主页'):
            index_page = 'https://work.weixin.qq.com/wework_admin/frame'
            self.driver.get(index_page)
            logging.info('进入企业微信主页')
            self.driver.implicitly_wait(10)

        # 点击通讯录
        with allure.step('进入通讯录页面'):
            self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
            logging.info('进入通讯录页面')
            self.driver.implicitly_wait(10)

        # 点击添加成员
        with allure.step('点击添加成员按钮'):
            self.driver.find_element_by_link_text('添加成员').click()
            logging.info('进入添加成员页面')

        # 填写姓名
        with allure.step('填写姓名、账号、手机号'):
            name = r"致幻"
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
            logging.info('填写姓名')
            # 填写账号
            acctid = str(int(random.uniform(1, 1000)))
            self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys(acctid)
            logging.info('填写账号')
            # 填写手机号
            mobile = str(int(random.uniform(10000000, 99999999)))
            self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('131'+mobile)

        # 点击保存按钮
        with allure.step('点击保存'):
            self.driver.find_element_by_link_text('保存').click()
            logging.info('完成新增')

        # 添加断言
        with allure.step('断言'):
            ele = self.driver.find_element_by_id('member_list')
            try:
                assert name in ele.text
                logging.info(f'{name}添加成功')
            except Exception as e:
                logging.info(e)
