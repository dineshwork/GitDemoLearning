from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    chkbx = (By.ID, "exampleCheck1")
    drpdwn = (By.ID, "exampleFormControlSelect1")
    subform = (By.XPATH, "//input[@type='submit']")
    txt = (By.CLASS_NAME, "alert-success")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.chkbx)

    def dropDown(self):
        return self.driver.find_element(*HomePage.drpdwn)

    def submitForm(self):
        return self.driver.find_element(*HomePage.subform)

    def successText(self):
        return self.driver.find_element(*HomePage.txt)