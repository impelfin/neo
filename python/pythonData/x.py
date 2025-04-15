from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# 드라이버 경로 및 옵션 설정
chrome_driver_path = '/root/chromedriver/chromedriver'
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f'--user-data-dir=/tmp/chrome-user-data-{int(time.time())}')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 페이지 접속
driver.get('https://www.pelicana.co.kr/store/store')
wait = WebDriverWait(driver, 10)

stores = []

while True:
    try:
        # 매장 리스트 대기
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.list > li')))
        store_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.list > li')

        for store in store_elements:
            try:
                name = store.find_element(By.CSS_SELECTOR, '.store_name').text.strip()
                address = store.find_element(By.CSS_SELECTOR, '.store_address').text.strip()
                phone = store.find_element(By.CSS_SELECTOR, '.store_tel').text.strip()
                stores.append([name, address, phone])
            except Exception as e:
                print("⚠️ 매장 정보 추출 오류:", e)

        # 다음 페이지 버튼 찾기
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="다음 페이지"]')
        if not next_button.is_enabled():
            print("🚫 다음 페이지 없음")
            break

        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(2)
    except Exception as e:
        print("❌ 다음 페이지로 이동 실패 또는 로딩 실패:", e)
        break

# CSV 저장
with open('pelicana_stores.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Store Name', 'Address', 'Phone'])
    writer.writerows(stores)

driver.quit()
print("✅ 모든 매장 정보 수집 완료! pelicana_stores.csv에 저장됨.")
