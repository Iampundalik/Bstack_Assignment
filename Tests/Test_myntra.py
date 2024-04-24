import time
from selenium import webdriver
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from PageObjects.Basepage import Baseclass
from PageObjects.Dashboard_page import Dashboard
from PageObjects.SearchedItemPage import Finalpage
from PageObjects.Tshirt_page import TshirtPage
from selenium.webdriver.common.by import By

baseURL = "https://www.myntra.com/"

def test_myntra():

    #Opens up the Chrome and Maximize it
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()

    #Hover Over Men field and click Tshirt
    Dash = Dashboard(driver)
    Dash.HoverOverMen()
    Dash.Hover_and_click_Tshirt()

    #Search Van and Click Van Hussaen
    Tshirt = TshirtPage(driver)
    Tshirt.ClickOnSearch()
    Tshirt.EnterVan()

    #Get All product Details
    page = Finalpage(driver)
    time.sleep(5)

    product_results = driver.find_elements(page.allProducts)
    for product in product_results:
            i=1
            print(product.find_element(By.TAG_NAME,"a").text)
    



