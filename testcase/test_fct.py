#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
# import form_cluster_test as fct
import form_cluster_test as fct


class TestFCT(unittest.TestCase):

    @fct.path(path="testcase/test_demo")
    @fct.case(cases=[("test_2", -2)])
    @fct.log(log_switch=True)
    def test_demo(self):
        @fct.model(model_name="get_list")
        def get_list():
            return True

        @fct.business
        def business(input):
            return {"ReturnCode": "0000"}

        assert fct.test(), fct.error_msg()
