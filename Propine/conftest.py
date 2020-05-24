import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/home/rupz/Chrome/chromedriver")
    driver.get("https://vast-dawn-73245.herokuapp.com/")
    driver.maximize_window()
    request.cls.driver = driver

    #yield
    #driver.close()
@pytest.fixture(params=[(18-12-1994,18/12/1994)])
def getdata(request):
    Dict = {}

    book = openpyxl.load_workbook("//home//rupz//Documents//inputs.xlsx")
    sheet = book.active
    cell = sheet.cell(row=1, column=2)
    print(cell.value)
    for i in range(2, sheet.max_row + 1):
        print(sheet.cell(row=i, column=2).value)
        # print(sheet.cell(row=i,column=sheet.max_column).value)
        Dict[sheet.cell(row=1, column=2).value] = sheet.cell(row=i, column=2).value
    return request.param
