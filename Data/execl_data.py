import xlrd
class Execl_data:
    def __init__(self,sheet):
        self.workbook = xlrd.open_workbook("D:\\yundeng_ui\\Data\\test_case.xlsx")
        self.workSheet = self.workbook.sheet_by_name(sheet)
    def case_data(self,a,b):#a指行，b指列
        case_value = self.workSheet.cell(a,b).value
        return case_value

    def case_test_data(self,a,b):
        dict = {}
        lists = []
        case_value = self.workSheet.cell(a, b).value
        case_split = case_value.split("\n")
        for i in range(len(case_split)):
            case = case_split[i].split("：")
            lists.append(case)
        for list in lists:
            dict.update(
                {list[0]:list[1]}
            )
        return dict


if __name__ == '__main__':
    print(Execl_data("人员管理").case_test_data(15,3))
    # print(Execl_data("吊顶").case_data(8,1))



