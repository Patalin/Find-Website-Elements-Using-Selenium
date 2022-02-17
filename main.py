# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service('/Users/macbookpro/Desktop/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get('https://www.amazon.com/2021-Apple-iPad-Mini-Wi-Fi/dp/B09J6K6Y21/ref=sr_1_12?crid=UY9G1VSLK7Y3&keywords='
           'ipad&qid=1645012132&sprefix=aipad%2Caps%2C148&sr=8-12&th=1')

# Find element by ID
price = driver.find_element(By.ID, 'corePrice_desktop')
print(price.text)

driver.quit()
