from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    prodName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    addToCart = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkOutOne = (By.CSS_SELECTOR, "a[class*='btn']")
    checkOutTwo = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def productName(self):
        return self.driver.find_elements(*CheckOutPage.prodName)

    def addtoCart(self):
        return self.driver.find_element(*CheckOutPage.addToCart)

    def checkOutone(self):
        return self.driver.find_element(*CheckOutPage.checkOutOne)

    def checkOuttwo(self):
        self.driver.find_element(*CheckOutPage.checkOutTwo).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage