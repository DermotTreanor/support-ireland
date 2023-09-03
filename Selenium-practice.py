from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

from selenium.webdriver.common.action_chains import ActionChains

import time

# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome()

driver.get("https://www.alcoholicsanonymous.ie/find-meeting/")
driver.maximize_window()

accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept.click()

#Load all meetings
load = driver.find_element(By.ID, "loadmore")
try:
    while True:
        load.click()
except ElementNotInteractableException:
    pass


#Get links to open meeting details
links = driver.find_elements(By.LINK_TEXT, "Meeting Info")
time.sleep(5)

for link in links:
    time.sleep(0.3)
    link.click()
    popup = driver.find_element(By.CLASS_NAME,"lity-opened")
    right = popup.find_element(By.CLASS_NAME, "item_popup_inner_right")
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    print(right.text, "\n")

