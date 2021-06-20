#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: conftest.py
# time: 2021/6/20 9:37 下午
from typing import List
import pytest
from function.calculator import Calculator
import logging


# 被测功能实例对象
@pytest.fixture(scope="class")
def calc():
    calc = Calculator()
    logging.info("计算器实例化完成")
    return calc

# 计算之前打印开始计算，计算之后打印结束计算
@pytest.fixture()
def tips():
    logging.info("====开始计算====")
    yield
    logging.info("====计算结束====")

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("items ===>", items)
    for item in items:
        # 修改测试用例的编码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


