#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import random
from datetime import date, timedelta
from .districode import *


def make_chi_name():
    """
    Generate a random Chinese name.
    :return: name
    """
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '一二三四五六七八九十百千万东南西北中金木水火土甲乙丙丁上下左右前后忱普韦创芸彭泰心廷其业水焕干唯将战朔幸向凤' \
           '兰仪沙胡璋珑朗举列纬歌献或见多谊迎州声男照辛有育甲起淮坦量楚劫勉典诺溪显稳甫羿端旦宣宙存迁万煦甜日翰淦劼庭徽豫' \
           '锬铸蚵也好颉雍怀北西耘秀玄令蓬联斯朕箭港宗闽励谷异年习格桑讳丛领深宜律朴化陵庄财直欧棋孝子丞如燃畏弦容锁韩曼汽地' \
           '芬上佶连郑兆纪盾相翌盈慰植任农 '
    user_name = random.choice(xing) + "".join(random.choice(ming) for i in range(2))
    if random.randint(0, 10) < 5:
        user_name = user_name[:2]
    else:
        pass
    return user_name


def make_chi_id():
    """
    Generate a random Chinese ID card number.
    :return: ID card number
    """
    codelist = list(district_code().keys())
    chi_id = codelist[random.randint(0, len(codelist) - 1)]  # 地区项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    year_now = int(da.strftime('%Y'))
    chi_id = chi_id + str(random.randint(1970, year_now - 19))  # 年份项
    chi_id = chi_id + da.strftime('%m%d')
    chi_id = chi_id + str(random.randint(100, 300))  # ，顺序号简单处理
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                  '10': '2'}  # 校验码映射
    for i in range(0, len(chi_id)):
        count = count + int(chi_id[i]) * weight[i]
    chi_id = chi_id + check_code[str(count % 11)]  # 算出校验码
    return chi_id


def make_chi_phone():
    """
    Generate a random Chinese phone number (11).
    :return: Chinese phone number
    """
    pre = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
           "152", "153", "155", "156", "157", "158", "159", "176", "177", "186", "187", "188"]
    phone_number = random.choice(pre) + "".join(random.choice("0123456789") for i in range(8))

    return phone_number


def make_uuid1():
    return str(uuid.uuid1())


def make_application_number():
    application_number = str(uuid.uuid1()).replace('-', '').upper()
    return application_number

