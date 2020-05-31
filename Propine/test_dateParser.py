from time import sleep
import pytest
from utilities.BaseClass import BaseClass



class TestDate(BaseClass):


    def test_tittle(self):
        Tittle = self.driver.title
        assert Tittle


    def test_url(self):
        log = self.getLogger()
        url = self.driver.current_url
        log.info(url)

    @pytest.mark.usefixtures("get_input")
    def test_date_parser(self, get_input):
        log = self.getLogger()
        if get_input["Expected Result"] is not None and get_input["Test Inputs"] is not None:
            self.driver.find_element_by_name("date").send_keys(get_input["Test Inputs"])
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            result = self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]").text.strip()
            Expected_result = get_input["Expected Result"].strip()
            log.info(result)
            self.driver.refresh()
            assert result in Expected_result
            sleep(2)

