#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .fct_set import *
from .test_excutor import TestExcutor
from .test_form_loader import TestFormLoader


class FormTestor:
    def __init__(self, path, ref_case):
        self.path = path
        self.ref_case = ref_case
        self.input_map = input_transparent
        self.output_map = output_transparent
        self.business = business_transparent

    def set_process(self, business=business_transparent, input_map=input_transparent, output_map=output_transparent):
        self.input_map = input_map
        self.output_map = output_map
        self.business = business

    @staticmethod
    def business_process(input):
        return business_transparent(input)

    @property
    def test(self):
        result = True
        try:
            test_loader = TestFormLoader(self.path, self.ref_case)
            test_excutor = TestExcutor(test_loader, business=self.business, input_map=self.input_map, output_map=self.output_map)
            if not test_excutor.excute_test():
                result = False
            return result
        except Exception as e:
            return False

    @property
    def error_msg(self):
        return "Form Comparision Test Error"