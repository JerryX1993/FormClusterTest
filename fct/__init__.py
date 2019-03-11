#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Any

from .test_excutor import TestExcutor
from .test_form_loader import TestFormLoader
from .format_sample import *
from .attribute_model import *


class FctSet:
    path = "/test"
    case = []
    input_mapper = None
    output_mapper = None
    business_process = None
    error_msg = ""
    model = {"chi_name": make_chi_name, "chi_id": make_chi_id}

    @staticmethod
    def set_init():
        FctSet.path = "/test"
        FctSet.case = []
        FctSet.input_mapper = input_transparent
        FctSet.output_mapper = output_transparent
        FctSet.business_process = business_transparent
        FctSet.error_msg = ""

    @staticmethod
    def set_path(path):
        FctSet.path = path

    @staticmethod
    def set_case(case):
        FctSet.case.append(case)

    @staticmethod
    def set_input(f):
        FctSet.input_mapper = f

    @staticmethod
    def set_output(f):
        FctSet.output_mapper = f

    @staticmethod
    def set_business(f):
        FctSet.business_process = f

    @staticmethod
    def set_model(model_name, f):
        FctSet.model[model_name] = f


def path(path):
    def decorator(f):
        FctSet.set_init()
        FctSet.set_path(path)
        return f
    return decorator


def case(**args):
    def decorator(f):
        FctSet.set_case(path)
        return f
    return decorator


def input(f):
    FctSet.set_input(f)
    return f


def output(f):
    FctSet.set_input(f)
    return f


def business(f):
    FctSet.set_business(f)
    return f


def model(model_name):
    def decorator(f):
        FctSet.set_model(model_name, f)
        return f
    return decorator


def input_transparent(input):
    return input


def output_transparent(input):
    return input


def business_transparent(input):
    return input


class FormTestor:
    def __init__(self, path, case):
        self.path = path
        self.case = case
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
            test_loader = TestFormLoader(self.path, self.case)
            test_excutor = TestExcutor(test_loader, business=self.business, input_map=self.input_map, output_map=self.output_map)
            if not test_excutor.excute_test():
                result = False
            return result
        except Exception as e:
            return False

    @property
    def error_msg(self):
        return "Form Comparision Test Error"


def test():
    fct_testor = FormTestor(FctSet.path, FctSet.case)
    fct_testor.set_process(FctSet.business_process, FctSet.input_mapper, FctSet.output_mapper)
    result = fct_testor.test
    FctSet.error_msg = fct_testor.error_msg
    return result


def error_msg():
    return FctSet.error_msg
