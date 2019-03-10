#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
# import form_cluster_test as fct
import fct


class TestFCT(unittest.TestCase):

    @fct.path("testcase/test_demo")
    def test_demo(self):
        @fct.business
        def business(input):
            return {"ReturnCode": "0000"}

        assert fct.test(), fct.error_msg()
