from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from .Basepage import Baseclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Dashboard(Baseclass):

    men_locator = (By.XPATH,"//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div")
    Tshirt_locator = (By.XPATH,"//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div/div/div/div/li[1]/ul/li[2]/a")

    def __init__(self,driver):
        self.driver = driver

    def HoverOverMen(self):
        action = ActionChains(self.driver)
        men = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.men_locator))
        action.move_to_element(men).perform()

    def Hover_and_click_Tshirt(self):
        action = ActionChains(self.driver)
        Tshirt = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.Tshirt_locator))
        action.move_to_element(Tshirt).click().perform()
        # action.perform()
