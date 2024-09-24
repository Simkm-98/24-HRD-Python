from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Selenium 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# WebDriver 초기화
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 접속
url = "https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do?pgmNo=179"
driver.get(url)

try:
    # 페이지 로딩 대기
    wait = WebDriverWait(driver, 30)
    table = wait.until(EC.presence_of_element_located((By.ID, "rankStatTA")))

    # 로딩 마스크가 사라질 때까지 대기
    wait.until(EC.invisibility_of_element_located((By.ID, "loading-mask")))

    # 검색 버튼 클릭 (데이터 로딩 트리거)
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn[onclick*='goSearch']")))
    search_button.click()

    # 데이터 로딩 대기
    time.sleep(5)

    # 데이터 추출
    data = []
    rows = driver.find_elements(By.CSS_SELECTOR, "#rankStatTA tr")
    print(f"Number of rows found: {len(rows)}")  # 디버깅용
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 0:
            date = cols[2].text
            avg_temp = cols[3].text
            if "2020-01" <= date <= "2023-12":
                data.append([date, avg_temp])

    # 데이터프레임 생성
    df = pd.DataFrame(data, columns=['Date', 'Average Temperature'])

    # CSV 파일로 저장
    df.to_csv("seoul_temperature_data.csv", index=False, encoding='utf-8-sig')
    print("Data has been saved to seoul_temperature_data.csv")

except Exception as e:
    print(f"An error occurred: {e}")
    # 페이지 소스 출력 (디버깅용)
    print("Page source:")
    print(driver.page_source)

finally:
    # 브라우저 종료
    driver.quit()