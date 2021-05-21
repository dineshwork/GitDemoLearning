import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItem()

        cards = checkOutPage.productName()

        for prod in cards:
            name = prod.text
            print(name)
            log.info(name)
            if name == "Blackberry":
                checkOutPage.addtoCart().click()

        checkOutPage.checkOutone().click()
        confirmPage = checkOutPage.checkOuttwo()
        log.info("Entering Country name as India")
        confirmPage.purchaConf().send_keys("Ind")
        #wait = WebDriverWait(self.driver, 7)

        self.verifyLinkPresence("India")
        confirmPage.linkText().click()

        confirmPage.termsCondition().click()
        confirmPage.purchasConfirm().click()

        stext = confirmPage.confirmText().text
        log.info("Text received from application is "+stext)
        assert "Success!Very Thank you!" in stext
        print(stext)
        print("Dinesh Kannan")
        print("din@abc.com")
        assert "Success! Thank you!" in stext
        self.driver.get_screenshot_as_file("screen.png")