import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First Name is "+ getData["fname"])
        homePage.getName().send_keys(getData["fname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.clickCheckbox().click()
        self.selectOptionByText(homePage.dropDown(), getData["gender"])
        homePage.submitForm().click()
        message = homePage.successText().text

        assert "success" in message
        self.driver.refresh()
        print(message)
        print("Yay all is good maga")

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param