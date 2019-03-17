#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .utils.default_model import *
import threading


class FctSet:
    path = "/test"
    ref_case = {}
    input_mapper = None
    output_mapper = None
    business_process = None
    log_switch = True
    error_msg = ""
    model = default_model
    threads = 1

    @staticmethod
    def set_init():
        FctSet.path = "/test"
        FctSet.ref_casec = {}
        FctSet.input_mapper = input_transparent
        FctSet.output_mapper = output_transparent
        FctSet.business_process = business_transparent
        FctSet.error_msg = ""

    @staticmethod
    def set_path(path):
        FctSet.path = path

    @staticmethod
    def set_case(case):
        FctSet.ref_case[case["name"]] = {"type": case["type"], "times": case["times"]}

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

    @staticmethod
    def set_log_switch(log_switch):
        FctSet.log_switch = False if log_switch is False else True


def input_transparent(input):
    return input


def output_transparent(input):
    return input


def business_transparent(input):
    return input