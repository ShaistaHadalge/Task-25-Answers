#!/usr/bin/env python
# coding: utf-8

# In[14]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\shais\OneDrive\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.imdb.com/search/name/")
import time
time.sleep(4)
driver.execute_script("window.scrollTo(0,500);")
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
nameelemeent= WebDriverWait(driver, 10).until( 
EC.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label")))
nameelemeent.click()


# In[15]:


import time
time.sleep(4)
driver.execute_script("window.scrollTo(0,500);")


# In[ ]:




