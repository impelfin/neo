import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print(type(driver))
print('-' * 50) 

print('Go Goole~!!')
url = 'http://www.google.com'
driver.get(url)

search_textbook = driver.find_element(By.NAME, 'q')

word = 'selenium'
search_textbook.send_keys(word)
search_textbook.submit()

wait = 3
print(str(wait) + ' seconds later...')
time.sleep(wait)

imagefile = 'p368_selenium.png'
driver.save_screenshot(imagefile)
print(imagefile + ' saved')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('Brwowser closed')