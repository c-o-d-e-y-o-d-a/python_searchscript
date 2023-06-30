from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from msedge.selenium_tools import Edge, EdgeOptions


import os
from datetime import datetime
from selenium.webdriver import ActionChains

driver = webdriver.Edge(executable_path = './msedgedriver.exe')

driver.get("https://www.google.com")




options = EdgeOptions()
options.use_chromium = True
options.add_argument("user-data-dir=C:/Users/hp/AppData/Local/Microsoft/Edge/User Data/Default")

options.add_argument("profile-directory=Profile 5")
options.add_argument("--start-maximized")
driver = Edge(options=options)
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("dfdkcjf")
elem.send_keys(Keys.RETURN)
    
    