from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from .Basepage import Baseclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Finalpage(Baseclass):

    allProducts = (By.CLASS_NAME,'product-base')
    price = (By.CLASS_NAME,"product-price")
    # discount = (By.CLASS_NAME,"product-discountPercentage")
    # product_links = (By.XPATH,'//*[@id="desktopSearchResults"]/div[2]/section/ul/li')
 
    def __init__(self,driver):
        self.driver = driver


    # def print_product_Details(self):
    #     Names = self.driver.find_elements(self.allProducts)
    #     return Names
        # Prices = self.driver.find_elements(self.price)
        # discounted = self.driver.find_elements(self.discount)
        # links = self.driver.find_elements(self.product_links)
        
        
        # for Price in Prices:
        #     print(Price.text)
        
        # for discount in discounted:
        #     print(discount.text)

        # for link in links:
        #     print(links.text)
        
        

