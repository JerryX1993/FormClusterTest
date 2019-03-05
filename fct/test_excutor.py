from src.mspccp.fct.single_testor import SingleTestor


class TestExcutor:
    def __init__(self, test_loader, business, input_map, output_map):
        self.test_loader = test_loader
        self.test_list = test_loader.test_list
        self.business = business
        self.input_map = input_map
        self.output_map = output_map

    def excute_test(self):
        result = True
        for test_set in self.test_list:
            (testcase_name, testcase_times) = test_set
            for time in range(1, testcase_times+1):
                print("Run Test " + testcase_name + " Try " + str(time) + "")
                file = self.test_loader.path + "/" + testcase_name + ".xls"
                try:
                    single_test = SingleTestor(file)
                    if not single_test.do_test(business=self.business, input_map=self.input_map, output_map=self.output_map):
                        result = False
                    print("Excute Test Done: "+file)
                except Exception as e:
                    result = False
                    print("Excute Test Error: "+file)

        return result
