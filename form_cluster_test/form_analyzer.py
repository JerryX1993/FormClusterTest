#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from form_cluster_test.utils.json_utils import *

input_key_col = 0
input_value_col = 1
input_type_col = 2
input_mode_col = 3
input_upper_col = 4
input_bound_col = 5
input_note_col = 6


class FormAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def input_sheet_analyzer(input_sheet):
        input_json = json.loads("{}", encoding="utf-8")
        rows = input_sheet.nrows
        for row in range(1, rows):
            try:
                key = input_sheet.cell(row, input_key_col).value
                value = input_sheet.cell(row, input_value_col).value
                key_type = input_sheet.cell(row, input_type_col).value
                key_mode = input_sheet.cell(row, input_mode_col).value
                key_upper = input_sheet.cell(row, input_upper_col).value
                key_bound = input_sheet.cell(row, input_bound_col).value
                # key_note = input_sheet.cell(row, input_note_col).value
                key_type, key_mode, key_upper = set_default_value(key_type, key_mode, key_upper)
                input_json = insert_to_json(input_json, key, value, key_type, key_mode, key_upper)
            except Exception as e:
                continue
        return input_json


def set_default_value(key_type, key_mode, key_upper):
    if key_type == "":
        key_type = "str"
    if key_mode == "":
        key_mode = "="
    if key_upper == "":
        key_upper = "/"
    return key_type, key_mode, key_upper
