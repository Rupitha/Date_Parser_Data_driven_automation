import pytest
from selenium import webdriver
from TestData import Exceldata


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/home/rupz/Chrome/chromedriver")
    input_url =driver.get("https://vast-dawn-73245.herokuapp.com/")
    # driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=Exceldata.Dateparser.getdata())
def get_input(request):
    return request.param
