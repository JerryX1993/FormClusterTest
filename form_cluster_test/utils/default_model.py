#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .attribution_model import *

default_model = {"chi_name": make_chi_name,
                 "chi_id": make_chi_id,
                 "chi_phone": make_chi_phone,
                 "uuid1": make_uuid1,
                 "app_nmbr": make_application_number}
