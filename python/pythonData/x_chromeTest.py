from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = '/root/chromedriver/chromedriver'

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f'--user-data-dir=/tmp/chrome-user-data-{int(time.time())}')

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.pelicana.co.kr/store/store")
print("✅ 크롬 실행 및 페이지 접속 성공")

driver.quit()
