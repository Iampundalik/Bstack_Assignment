from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from .Basepage import Baseclass
from selenium.webdriver.common.action_chains import ActionChains

class TshirtPage(Baseclass):

    search_button = (By.XPATH,"//*[@id='mountRoot']/div/main/div[3]/div[1]/section/div/div[3]/div[1]")
    van_hus = (By.XPATH,"//*[@id='mountRoot']/div/main/div[3]/div[1]/section/div/div[3]/ul/li[1]/label")
    keys = "Van"
    input_field = (By.XPATH,"//*[@id='mountRoot']/div/main/div[3]/div[1]/section/div/div[3]/div[1]/input")

    def __init__(self,driver):
        self.driver = driver
    
    def ClickOnSearch(self):
        self.Click(self.search_button)
        self.SendKeys(self.input_field,self.keys)
    
    def EnterVan(self):
        self.Click(self.van_hus)