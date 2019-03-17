# Form Cluster Test

It's a framework for form data cluster test with data-driven test.

## Installation

```bash
pip install form_cluster_test
```
Or download .whl file, and cd to download path
```bash
pip install form_cluster_test-[version]-py3-none-any.whl
```

## Import and Usage
Step 1:
Prepare Test xls files, and put them into a test directory that could be accessed in project.
How to make a template test xls file:
```python
import form_cluster_test as fct

# For json object
fct.format_json(input_json={}, encoding="utf-8")

# For json file
fct.format_json_file(json_file="demo.json", encoding="utf-8")

# For xml file
fct.format_xml_file(xml_file="demo.xml", encoding="utf-8")
```

Step 2:
```python
import form_cluster_test as fct
import unittest

class TestFCT(unittest.TestCase):
    # [Required] Initiate fct test for one suite
    @fct.path(path="testcase/test_demo")
    # [Optional] Manually Set case type and times.
    @fct.case(cases=[("test_2", 2)])
    # [Optional] Manually Set log switch, switch is ON by default.
    @fct.log(log_switch=True)
    def test_demo(self):
        # [Optional] Choose a generator function for your parameter model.
        @fct.model(model_name="get_list")
        def get_list():
            return True
        # [Required] Assign the business process that you will test.
        @fct.business
        def business(input):
            return {"ReturnCode": "0000"}
    
        # [Required] Assert the test result.
        assert fct.test(), fct.error_msg()
```

## Version Log
#### Version 0.1.0
1. Support model attribution
2. Support solo case, skip case, repeat case