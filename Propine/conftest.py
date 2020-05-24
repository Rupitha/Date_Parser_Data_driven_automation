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
    return request.param
