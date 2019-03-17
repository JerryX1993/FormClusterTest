#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd.xlsx

from .form_analyzer import FormAnalyzer
from .form_comparator import FormComparator

input_sheet_name = "INPUT"
output_sheet_name = "OUTPUT"


class SingleTestor:
    def __init__(self, file):
        self.file = file
        self.load_test = xlrd.open_workbook(self.file)
        self.input = None
        self.output = None

    def analyze_data(self):
        input_sheet = self.load_test.sheet_by_name(input_sheet_name)
        self.input = self.input_analyze(input_sheet)
        print(self.input)
        pass

    def compare_result(self):
        output_sheet = self.load_test.sheet_by_name(output_sheet_name)
        return FormComparator.compare_output_sheet(output_sheet, self.output)

    def do_test(self, business, input_map, output_map):
        self.analyze_data()
        business_input = input_map(self.input)
        business_output = business(business_input)
        self.output = output_map(business_output)
        try:
            return self.compare_result()
        except Exception as e:
            return False

    def input_analyze(self, input_sheet):
        return FormAnalyzer.input_sheet_analyzer(input_sheet)

