#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: conftest.py
# time: 2021/6/26 4:20 下午
from typing import List



# 修改测试用例的编码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("items ===>", items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')