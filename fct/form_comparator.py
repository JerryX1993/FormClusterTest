output_key_col = 0
output_value_col = 1
output_type_col = 2
output_mode_col = 3
output_upper_col = 4
output_note_col = 5


class FormComparator:
    def __init__(self):
        pass

    @staticmethod
    def compare_output_sheet(output_sheet, output):
        result = True
        rows = output_sheet.nrows
        for row in range(1, rows):
            try:
                key = output_sheet.cell(row, output_key_col).value
            except Exception as e:
                continue
            try:
                value = output_sheet.cell(row, output_value_col).value
            except Exception as e:
                value = ""

            if str(output[key]) != value:
                print("Fail: "+key+"; Expected: "+value+"; Received: "+str(output[key]))
                result = False
        return result
