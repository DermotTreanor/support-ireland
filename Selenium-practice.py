from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

#driver = webdriver.Chrome()

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

meeting_data = {}
for link in links:
    time.sleep(0.3)
    link.click()
    
    #Open the popup with information for a particular meeting
    popup = driver.find_element(By.CLASS_NAME,"lity-opened")
    
    #Get the name of the meeting and the address from the popup
    title = popup.find_element(By.CLASS_NAME, "popup_title").text
    address = popup.find_element(By.CLASS_NAME, "item_address").text
    #times = popup.find_element(By.CLASS_NAME, "item_popup_inner_right").text
    
    times = {}
    dates = popup.find_elements(By.CLASS_NAME, "times_list_item")
    for date in dates:
        day = date.find_element(By.CLASS_NAME, "day_label").text
        times[day] = []
        hours = date.find_elements(By.CLASS_NAME, "time_list_item")
        
        for hour in hours:
            try:
                meet_type = hour.find_element(By.CLASS_NAME, "meeting_description").text
            except NoSuchElementException:
                meet_type = None
            if meet_type == "Physical":
                times[day].append(hour.find_element(By.CLASS_NAME, "time").text)
                
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    meeting_data[title] = (address, times)
    #print(times.text, "\n")
print(meeting_data)

for i in meeting_data:
    print(i, "\n\n", meeting_data[i][0], "\n\n\n", meeting_data[i][1], "\n\n\n\n\n\n")
    
    
    
    

