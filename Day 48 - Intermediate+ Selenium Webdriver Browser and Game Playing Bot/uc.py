import undetected_chromedriver as uc 
 
driver = uc.Chrome() 
driver.get("https://qxbroker.com/en") 
 
print(driver.current_url) # https://www.nowsecure.nl/ 
print(driver.title) # nowSecure
