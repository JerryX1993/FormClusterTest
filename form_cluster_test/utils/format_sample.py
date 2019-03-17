#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmltodict, xlrd, xlwt
import xml
from datetime import datetime
import json


def format_json_file(json_file, encoding="utf-8"):
    with open(json_file, encoding=encoding) as fd:
        input_json = json.loads(fd.read())
    return format_json(input_json, encoding)


def format_xml_file(xml_file, encoding="utf-8"):
    with open(xml_file, encoding=encoding) as fd:
        input_json = xmltodict.parse(fd.read())
    return format_json(input_json, encoding)


def format_json(input_json, encoding="utf-8"):
    target_list = {}
    convert_flat(input_json=input_json, target_list=target_list)
    print(target_list)
    xls_name = datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S") + '.xls'

    xls_file = xlwt.Workbook()

    input_table = xls_file.add_sheet("INPUT")
    xls_file.add_sheet("OUTPUT")

    input_table.write(0, 0, 'KEY')
    input_table.write(0, 1, 'VALUE')
    input_table.write(0, 2, 'TYPE  DEFAULT: str')
    input_table.write(0, 3, 'MODE  DEFAULT: =')
    input_table.write(0, 4, 'UPPER  DEFAULT: /')
    input_table.write(0, 5, 'NOTE')

    cusor_row = 1

    for (key, value) in target_list.items():
        input_table.write(cusor_row, 0, key)
        input_table.write(cusor_row, 1, value[0])
        input_table.write(cusor_row, 2, value[1])
        input_table.write(cusor_row, 4, "/" + value[2])
        cusor_row += 1

    xls_file.save(xls_name)


def convert_flat(input_json, target_list, upper_name="", ):
    for (key, value) in input_json.items():
        if isinstance(value, dict):
            target_list[key] = ("", "obj", upper_name)
            node = key if upper_name == "" else upper_name + "/" + key
            convert_flat(value, target_list, node)
        else:
            target_list[key] = (value, str(type(value))[8:-2], upper_name)


