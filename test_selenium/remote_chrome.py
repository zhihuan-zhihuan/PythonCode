#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: remote_chrome.py
# time: 2021/6/26 4:26 下午

import yaml
from selenium import webdriver

"""
1、配置Chrome环境变量
2、命令行：Chrome --remote-debugging-port=9999,代码端口与命令一致
3、手动扫码登陆
4、代码设置debugging，通过复用浏览器获取cookies
"""

# 设置debugger地址
def set_debug_address():
    opst = webdriver.ChromeOptions()
    opst.debugger_address = "127.0.0.1:9999"
    driver = webdriver.Chrome(options=opst)
    return driver

# 通过复用浏览器获取cookies，写入yaml文件
def remote_cookies():
    driver = set_debug_address()
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookies = driver.get_cookies()
    print(cookies)
    with open("./datas/cookies.yaml", "w") as f:
        yaml.safe_dump(cookies, f)

if __name__ == "__main__":
    remote_cookies()