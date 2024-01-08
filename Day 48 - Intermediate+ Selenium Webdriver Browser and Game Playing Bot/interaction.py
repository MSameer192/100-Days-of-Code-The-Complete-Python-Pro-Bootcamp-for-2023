from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_driver_path = '../../../WebAutomation/chromedriver-linuxNew/chromedriver-linux64/chromedriver'   
service = Service(chrome_driver_path)

# #Keep Chrome browser open after progra finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

wiki_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(wiki_articles.text)
# wiki_articles.click()

# Find element by Link text
content_link = driver.find_element(By.LINK_TEXT, value='Community portal')
print(content_link.text)
# content_link.click()


# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value='search')

# Sending keyboard input to Selenium
search.send_keys('Python', Keys.ENTER)


#Complete Browser
# driver.quit()

