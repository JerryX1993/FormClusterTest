#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import uuid
from datetime import date, timedelta
from districode import DistriCode
import os
# os.chdir("../../")


class MakeUserData:
    """
    author: z675587
    """
    def __init__(self, user_type='new'):
        self.id_card_no = self._id_card_no(user_type)
        self.user_name = self._user_name(user_type)
        self.phone_number = self._phone_number(user_type)
        self.application_number = self.application_number()
        self.entity_number = self.entity_number()

    def _id_card_no(self, user_type):
        if user_type == 'new':
            id_card_no = self._id_gennerator()
        else:
            id_card_no = '210682' + '19801101' + '5105'
        return id_card_no

    def _user_name(self, user_type):
        if user_type == 'new':
            xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
            ming = '一二三四五六七八九十百千万东南西北中金木水火土甲乙丙丁上下左右前后忱普韦创芸彭泰心廷其业水焕干唯将战朔幸向凤兰仪沙胡璋珑朗举列纬歌献或见多谊迎州声男照辛有育甲起淮坦量楚劫勉典诺溪显稳甫羿端旦宣宙存迁万煦甜日翰淦劼庭徽豫锬铸蚵也好颉雍怀北西耘秀玄令蓬联斯朕箭港宗闽励谷异年习格桑讳丛领深宜律朴化陵庄财直欧棋孝子丞如燃畏弦容锁韩曼汽地芬上佶连郑兆纪盾相翌盈慰植任农'
            user_name = random.choice(xing) + "".join(random.choice(ming) for i in range(2))
            if random.randint(0, 10) < 5:
                user_name = user_name[:2]
            else:
                pass
        else:
            user_name = '常萍'
        return user_name

    def _phone_number(self, user_type):
        if user_type == 'new':
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                        "152", "153", "155", "156", "157", "158", "159", "176", "177", "186", "187", "188"]
            phone_number = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        else:
            phone_number = '18888888888'
        return phone_number

    def application_number(self):
        application_number = str(uuid.uuid1()).replace('-', '').upper()
        return application_number

    def entity_number(self):
        sums = random.randint(0, 999999999)
        left = sums % 7
        entity_number = "0" * (9 - len(str(sums))) + str(sums) + str(left)
        return entity_number

    # def _getdistrictcode(self):
    #     with open("districtcode.ini") as file:
    #         data = file.read()
    #         districtlist = data.split('\n')
    #     for node in districtlist:
    #         # print node
    #         if node[10:11] != ' ':
    #             state = node[10:].strip()
    #         if node[10:11] == ' ' and node[12:13] != ' ':
    #             city = node[12:].strip()
    #         if node[10:11] == ' ' and node[12:13] == ' ':
    #             district = node[14:].strip()
    #             code = node[0:6]
    #             codelist.append({"state": state, "city": city, "district": district, "code": code})
    #     with open("districode.py", 'w', encoding="utf-8") as give_file:
    #         give_file.write(str(codelist))

    def _id_gennerator(self):
        codelist = DistriCode.get_codelist()
        id = codelist[random.randint(0, len(codelist)-1)]['code']  # 地区项
        id = id + str(random.randint(1970, 2000))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # ，顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id



# user1 = MakeUserData(user_type='new')
# user2 = MakeUserData(user_type='old')
#
# print('user1:\n', user1.user_name, '\n', user1.id_card_no, '\n', user1.phone_number, '\n',
#       user1.application_number, '\n', user1.entity_number)
# print('user2:\n', user2.user_name, '\n', user2.id_card_no, '\n', user2.phone_number, '\n',
#       user2.application_number, '\n', user2.entity_number)


