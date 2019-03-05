from src.mspccp.fct.test_excutor import TestExcutor
from src.mspccp.fct.test_form_loader import TestFormLoader


def new(path="/test"):
    return FormTestor(path)


def input_transparent(input):
    return input


def output_transparent(input):
    return input


def business_transparent(input):
    return input


class FormTestor:
    def __init__(self, path):
        self.path = path
        self.input_map = input_transparent
        self.output_map = output_transparent
        self.business = business_transparent

    def set_process(self, business=business_transparent, input_map=input_transparent, output_map=output_transparent):
        self.input_map = input_map
        self.output_map = output_map
        self.business = business

    @property
    def test(self):
        result = True
        try:
            test_loader = TestFormLoader(self.path)
            test_excutor = TestExcutor(test_loader, business=self.business, input_map=self.input_map, output_map=self.output_map)
            if not test_excutor.excute_test():
                result = False
            return result
        except Exception as e:
            return False

    @property
    def error_msg(self):
        return "Form Comparision Test Error"
