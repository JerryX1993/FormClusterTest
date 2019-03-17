#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .test_excutor import TestExcutor
from .test_form_loader import TestFormLoader
from .utils.format_sample import *
from .utils.attribution_model import *
from .fct_set import *
from .form_testor import *


def path(path: str):
    """
    Manually set form_cluster_test path by a decorator.
    @form_cluster_test.path(path = "testcase/test_demo")
    All test form files should be put under form_cluster_test path, the past case and business will be clear.
    """
    def decorator(f):
        FctSet.set_init()
        FctSet.set_path(path)
        return f

    return decorator


def log(log_switch: bool):
    """
    Manually set form_cluster_test log switch.
    @form_cluster_test.log(log_switch = False)
    By default, form_cluster_test log is switched to True, which means that will generate logs while processing.
    """
    def decorator(f):
        FctSet.set_init()
        FctSet.set_log_switch(log_switch)
        return f

    return decorator


def case(cases: list):
    """
    Manually set case type and times by a decorator.
    @form_cluster_test.case(cases = [("test_name_1", 2), ("test_name_2", 0), ("test_name_3", -4)])
    By default, form_cluster_test will scan and load all tests under form_cluster_test.path with type: "normal", times: "1".
    If one test_name is manually set, type and times will be covered.
    Example:
    # change test times
    @form_cluster_test.case(cases = [ ("test_name_1", 2) ])

    # change test to skip
    @form_cluster_test.case(cases = [ ("test_name_2", 0) ])

    # change test to be solo, block other normal tests
    # minus symbol before times represents "solo"
    @form_cluster_test.case(cases = [ ("test_name_2", -4) ])
    """
    def decorator(f):
        try:
            for single_case in cases:
                insert_case = {}
                (name, times) = single_case
                insert_case["name"] = name
                insert_case["times"] = abs(times)
                if times == 0:
                    insert_case["type"] = "skip"
                elif times < 0:
                    insert_case["type"] = "solo"
                else:
                    insert_case["type"] = "normal"
                FctSet.set_case(insert_case)
        except Exception as e:
            pass
        return f

    return decorator


def input(f):
    """
    Manually set form_cluster_test input map method.
    @form_cluster_test.input
    By default, input map method is transparent.
    """
    FctSet.set_input(f)
    return f


def output(f):
    """
    Manually set form_cluster_test output map method.
    @form_cluster_test.output
    By default, output map method is transparent.
    """
    FctSet.set_input(f)
    return f


def business(f):
    """
    Manually set form_cluster_test business process.
    @form_cluster_test.business
    By default, business process is transparent.
    """
    FctSet.set_business(f)
    return f


def model(model_name: str):
    """
    Manually set attribution model. Model function must provide a return value
    @form_cluster_test.model(model_name = "model_1")
    In test form, just make attribution type "model", and make attribution value like "${model_name}"

    BuildIn model:
    ${chi_name}: Chinese name randomly
    ${chi_id}: Chinese id card number randomly
    ${uuid}: uuid
    """
    def decorator(f):
        FctSet.set_model(model_name, f)
        return f

    return decorator


def test():
    fct_testor = FormTestor(FctSet.path, FctSet.ref_case)
    fct_testor.set_process(FctSet.business_process, FctSet.input_mapper, FctSet.output_mapper)
    result = fct_testor.test
    FctSet.error_msg = fct_testor.error_msg
    return result


def error_msg():
    return FctSet.error_msg


