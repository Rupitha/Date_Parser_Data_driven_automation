import openpyxl



class DateParserData:
    @staticmethod
    def getTestData(self):
        book = openpyxl.load_workbook("//home//rupz//Documents//inputs.xlsx")
        sheet = book.active
        cell = sheet.cell(row=1,column=2)
        print(cell.value)
        for i in range(2,sheet.max_row+1):
            for j in range(2,sheet.max_column+1):
                print(sheet.cell(row=i,column=j).value)
   



