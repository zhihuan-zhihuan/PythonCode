#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: test_calculator.py
# time: 2021/6/19 2:04 下午
import logging
import pytest
import allure
import yaml

# 获取yaml文件中的数据
def get_datas():
    with open("./datas/datas.yaml") as f:
        datasdict = yaml.safe_load(f)
        add_suc_data = (datasdict["add_suc"]["datas"], datasdict["add_suc"]["ids"])
        add_err_data = (datasdict["add_err"]["datas"], datasdict["add_err"]["ids"])
        div_suc_data = (datasdict["div_suc"]["datas"], datasdict["div_suc"]["ids"])
        div_err_data = (datasdict["div_err"]["datas"], datasdict["div_err"]["ids"])
        return add_suc_data, add_err_data, div_suc_data, div_err_data


# 添加大的功能点
@allure.feature("计算器测试")
class TestCalculator:
    @allure.story("加法用例")
    @allure.title("加法正常用例：{a}+{b}")
    # 参数化
    @pytest.mark.parametrize('a,b,values', get_datas()[0][0], ids=get_datas()[0][1])
    # 报告添加测试步骤
    @allure.step("步骤")
    # 创建加法测试正常测试用例
    def test_add_suc(self, tips, calc, a, b, values):
        with open("./image/baidu.png", "rb") as f:
            context = f.read()
            allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)
        allure.attach("文本附件", "文本标题", allure.attachment_type.TEXT)
        logging.info(f"assert [{a}+{b}]")
        assert values == calc.add(a, b)

    @allure.story("加法用例")
    @allure.title("加法异常用例：{a}+{b}")
    @pytest.mark.parametrize('a,b,values', get_datas()[1][0], ids=get_datas()[1][1])
    # 创建加法异常测试用例
    @pytest.mark.xfail(True, reason="浮点数相加精度损失")
    def test_add_float(self, tips, calc, a, b, values):
        logging.info(f"assert [{a}+{b}]")
        assert isinstance(a, float) and isinstance(b, float)

    @allure.story("除法用例")
    @allure.title("除法正常用例：{a}/{b}")
    @pytest.mark.parametrize('a,b,values', get_datas()[2][0], ids=get_datas()[2][1])
    # 创建除法正常用例
    def test_div_suc(self, tips, calc, a, b, values):
        logging.info(f"assert [{a}/{b}]")
        assert values == calc.div(a, b)

    @allure.story("除法用例")
    @allure.title("除法异常用例：{a}/{b}")
    @pytest.mark.parametrize('a,b,values', get_datas()[3][0], ids=get_datas()[3][1])
    # 创建除法异常测试用例
    def test_div_zero(self, tips, calc, a, b, values):
        with pytest.raises(ZeroDivisionError):
            logging.info(f"assert [{a}/{b}]")
            assert values == calc.div(a, b)
