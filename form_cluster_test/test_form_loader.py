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
    def __init__(self, path, ref_case):
        self.path = path
        self.ref_case = ref_case
        self.test_list = self._get_test_list()
        print(self.test_list)
        logging.info("Test List: " + str(self.test_list))

    def _get_test_list(self):
        test_list = []
        dir_list = os.listdir(self.path)
        include_solo = False
        for file_name in dir_list:
            try:
                test_name = file_name[:-4]
                if file_name[-4:] == ".xls":
                    # cover test case with reference case
                    try:
                        test_type = self.ref_case[test_name]["type"]
                    except Exception as e:
                        test_type = "normal"
                    try:
                        test_times = self.ref_case[test_name]["times"]
                    except Exception as e:
                        test_times = 1

                    # insert test list for each type
                    if test_type == "skip":
                        continue
                    elif test_type == "solo":
                        if not include_solo:
                            # if there's no solo included, clear test list & tag included
                            test_list = []
                            include_solo = True
                        else:
                            # if there's already solo included, keep it
                            pass
                        test_list.append((test_name, test_times))
                    else:
                        if not include_solo:
                            # if there's no solo included, insert to test list
                            test_list.append((test_name, test_times))
                        else:
                            # if there's already solo included, skip it
                            continue
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
