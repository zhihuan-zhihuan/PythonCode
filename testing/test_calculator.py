#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhihuan
# file: test_calculator.py
# time: 2021/6/19 2:04 下午

"""
课后作业
2、使用参数化完成测试用例的自动生成
注意：
使用等价类，边界值，因果图等设计测试用例
"""
import pytest
import allure
import yaml
from function.calculator import Calculator


def get_datas():
    with open("./datas/datas.yaml") as f:
        datasdict = yaml.safe_load(f)
        add_suc_data = (datasdict["add_suc"]["datas"], datasdict["add_suc"]["ids"])
        add_err_data = (datasdict["add_err"]["datas"], datasdict["add_err"]["ids"])
        div_suc_data = (datasdict["div_suc"]["datas"], datasdict["div_suc"]["ids"])
        div_err_data = (datasdict["div_err"]["datas"], datasdict["div_err"]["ids"])
        return add_suc_data, add_err_data, div_suc_data, div_err_data

@allure.title("计算机加、除功能测试")
class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.fixture()
    def tips(self):
        print("====开始计算====")
        yield
        print("====计算结束====")

    @allure.story("加法用例")
    @pytest.mark.parametrize('a,b,values', get_datas()[0][0], ids=get_datas()[0][1])
    def test_add_suc(self, tips, a, b, values):
        assert values == self.calc.add(a, b)

    @allure.story("加法异常用例")
    @pytest.mark.parametrize('a,b,values', get_datas()[1][0], ids=get_datas()[1][1])
    @pytest.mark.xfail(True, reason="浮点数相加精度损失")
    def test_add_xfail(self, tips, a, b, values):
        assert isinstance(a, float) and isinstance(b, float)

    @allure.story("除法用例")
    @pytest.mark.parametrize('a,b,values', get_datas()[2][0], ids=get_datas()[2][1])
    def test_div_suc(self, tips, a, b, values):
        assert values == self.calc.div(a, b)

    @allure.story("除法异常用例")
    @pytest.mark.parametrize('a,b,values', get_datas()[3][0], ids=get_datas()[3][1])
    @pytest.mark.xfail(True, reason="0不能做除数")
    def test_div_xfail(self, tips, a, b, values):
        assert b == 0
