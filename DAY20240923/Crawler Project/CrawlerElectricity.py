from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import locale


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def crawl_seoul_energy_data(year, driver):
    url = "https://energyinfo.seoul.go.kr/energy/energyUsagePattern?menu-id=Z020400"
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "searchYear"))
    )

    # 연도 선택
    year_select = Select(driver.find_element(By.ID, "searchYear"))
    year_select.select_by_value(str(year))

    # 조회 버튼 클릭
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), '조회')]")
    search_button.click()

    # 데이터 로딩을 위한 대기
    time.sleep(10)

    # 데이터 추출
    monthly_data = {}
    for month in range(1, 13):
        try:
            # XPath를 사용하여 '서울시 평균' 행의 각 월 데이터 추출
            xpath = f"//tr[@id='2']/td[@aria-describedby='gridSeoul_M{month:02d}']"
            usage_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            usage = float(usage_element.text.replace(',', ''))
            monthly_data[f'{month:02d}'] = usage
        except Exception as e:
            print(f"Error extracting data for {year}-{month:02d}: {e}")

    return monthly_data


# 로케일 설정 (천 단위 구분자 사용을 위해)
locale.setlocale(locale.LC_ALL, '')

# 여러 해의 데이터 크롤링
years = range(2020, 2024)  # 2020부터 2023까지
all_data = []

driver = setup_driver()
try:
    for year in years:
        yearly_data = crawl_seoul_energy_data(year, driver)
        for month, usage in yearly_data.items():
            all_data.append({
                '년도': year,
                '월': month,
                '사용량': usage
            })
        time.sleep(5)  # 각 연도 크롤링 사이에 잠시 대기
finally:
    driver.quit()

if all_data:
    # DataFrame 생성
    df = pd.DataFrame(all_data)

    # '사용량' 열을 float 타입으로 유지
    df['사용량'] = df['사용량'].astype(float)

    # CSV 파일로 저장
    csv_filename = 'seoul_average_energy_usage_2020_2023.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"Data saved to '{csv_filename}'")

else:
    print("Failed to crawl data.")
