#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd.xlsx
import os
import logging

ncols = 5
testcase_name_col = 0
testcase_times_col = 2
testcase_mode_col = 3


class TestFormLoader:
    def __init__(self, path, case):
        self.path = path
        self.case = case
        self.test_list = self._get_test_list()
        print(self.test_list)
        logging.info("Test List: " + str(self.test_list))

    def _get_test_list(self):
        test_list = []
        dir_list = os.listdir(self.path)
        for file_name in dir_list:
            try:
                if file_name[-4:] == ".xls":
                    test_list.append((file_name[:-4], 100))
                else:
                    continue
            except Exception as e:
                continue
        return test_list

    # def _get_test_list(self):
    #     test_list = []
    #     file_path = self.path + "/load_test.xls"
    #     load_test = xlrd.open_workbook(file_path)
    #     list_sheet = load_test.sheet_by_name("LIST")
    #
    #     nrows = list_sheet.nrows
    #     for i in range(1, nrows):
    #         try:
    #             testcase_name = list_sheet.cell(i, testcase_name_col).value
    #         except Exception as e:
    #             continue
    #
    #         try:
    #             testcase_times = int(list_sheet.cell(i, testcase_times_col).value)
    #         except Exception as e:
    #             testcase_times = 1
    #
    #         try:
    #             testcase_mode = list_sheet.cell(i, testcase_mode_col).value
    #             if testcase_mode == "OFF":
    #                 continue
    #             if testcase_mode == "SOLO":
    #                 test_list = []
    #                 test_list.append((testcase_name, testcase_times))
    #                 break
    #         except Exception as e:
    #             pass
    #
    #         test_list.append((testcase_name, testcase_times))
    #     return test_list
