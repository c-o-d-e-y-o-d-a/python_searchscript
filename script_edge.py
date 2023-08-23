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

c:\Users\hp\boostrap learn\bootstrap-learn\pythonScript
from msedge.selenium_tools import Edge, EdgeOptions

edge_options = EdgeOptions()
edge_options.use_chromium = True

# Open first account
edge_options.add_argument("user-data-dir=C:\\Users\\hp\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
edge_options.add_argument("profile-directory=Profile 6")

driver1 = Edge(options=edge_options)
driver1.get("https://rewards.bing.com/")

# Open second account
edge_options.add_argument("user-data-dir=C:\\Users\\hp\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
edge_options.add_argument("profile-directory=Profile 2")

driver2 = Edge(options=edge_options)
driver2.get("https://rewards.bing.com/")




options = EdgeOptions()
options.use_chromium = True
options.add_argument("user-data-dir=C:\\Users\\hp\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")

options.add_argument("profile-directory=Profile 5")
options.add_argument("--start-maximized")
driver = Edge(options=options)
driver.get("https://rewards.bing.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("search query")
search_box.submit()
    
    