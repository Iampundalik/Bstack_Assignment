from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Baseclass:

    def __init__(self,driver):
        self.driver = driver

    def HoverMen(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))

    def Click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).click()
    
    def SendKeys(self,by_locator,keys):
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).clear
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).send_keys(keys)
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located(checkboxlocator)).click()
    
