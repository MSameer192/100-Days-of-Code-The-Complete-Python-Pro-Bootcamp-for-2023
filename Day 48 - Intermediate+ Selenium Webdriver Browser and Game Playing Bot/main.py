from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '../../../WebAutomation/chromedriver-linuxNew/chromedriver-linux64/chromedriver'   
service = Service(chrome_driver_path)

# #Keep Chrome browser open after progra finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_cents.text}.{price_cents.text}")


# Python.org

driver.get('https://python.org')
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_line = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_line.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# Create an empty dictionary to store the data
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)




#  ----------------   Get upcoming event list by Sameer Method
# upcoming_events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

# # Find all li elements within the ul
# list_items = upcoming_events.find_elements(By.TAG_NAME, 'li')

# # Create an empty dictionary to store the data
# events_dict = {}

# # Loop through each li element
# for index, li in enumerate(list_items, start=1):
#     # Extract time and text
#     time_with_text = li.text
    
#     print('time_with_text', time_with_text)
#     # Extract the text from the <a> tag, if it exists
#     a_tag_text = ""
#     a_tag = li.find_element(By.TAG_NAME, 'a')
#     if a_tag:
#         a_tag_text = a_tag.text
    
#     # Store time with text and a tag text in the dictionary
#     events_dict[f"Event{index}"] = {
#         'Time with Text': time_with_text,
#         'A Tag Text': a_tag_text
#     }

# # Print the resulting dictionary
# print(events_dict)




#Particular tab
# driver.close()

#Complete Browser
driver.quit()

