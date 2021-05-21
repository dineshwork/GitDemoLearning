from selenium.webdriver.common.by import By


class ConfirmPage:


    def __init__(self, driver):
        self.driver = driver

    purchaseConfirm = (By.ID, "country")
    linkTxt = (By.LINK_TEXT, "India")
    termsCon = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    purchConf = (By.XPATH, "//input[@value='Purchase']")
    confText = (By.CLASS_NAME, "alert-success")

    def purchaConf(self):
        return self.driver.find_element(*ConfirmPage.purchaseConfirm)

    def linkText(self):
        return self.driver.find_element(*ConfirmPage.linkTxt)

    def termsCondition(self):
        return self.driver.find_element(*ConfirmPage.termsCon)

    def purchasConfirm(self):
        return self.driver.find_element(*ConfirmPage.purchConf)

    def confirmText(self):
        return self.driver.find_element(*ConfirmPage.confText)