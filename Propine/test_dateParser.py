from utilities.BaseClass import BaseClass


class TestDate(BaseClass):

    def test_date_parser(self,setup):
        print("Date parser")
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.find_element_by_name("date").sendkeys()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        print(self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]").text)




