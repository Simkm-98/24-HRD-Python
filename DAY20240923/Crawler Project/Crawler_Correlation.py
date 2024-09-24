import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일에서 데이터 읽기 (한글 인코딩 지정)
energy_data = pd.read_csv("seoul_average_energy_usage_2019_2023.csv", encoding='utf-8')
temp_data = pd.read_csv("seoul_temperature_data.csv", encoding='utf-8')

# '사용량' 열이 이미 숫자 형식인지 확인
if energy_data['사용량'].dtype == 'object':
    # 문자열인 경우에만 천 단위 구분자 제거 및 숫자로 변환
    energy_data['사용량'] = energy_data['사용량'].str.replace(',', '').astype(float)
else:
    # 이미 숫자 형식인 경우 그대로 사용
    energy_data['사용량'] = energy_data['사용량'].astype(float)

# KWh에서 MWh로 변환 (100,000 KWh = 100 MWh)
energy_data['사용량_MWh'] = energy_data['사용량'] / 1000

# 날짜 열 생성
energy_data['Date'] = pd.to_datetime(energy_data['년도'].astype(str) + '-' + energy_data['월'].astype(str).str.zfill(2) + '-01')
temp_data['Date'] = pd.to_datetime(temp_data['Date'])

# 데이터 병합
merged_data = pd.merge(energy_data, temp_data, on='Date', how='inner')

# 한글 폰트 설정 (matplotlib에서 한글 표시를 위해)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 산점도 그리기
plt.figure(figsize=(12, 8))
plt.scatter(merged_data['Average Temperature'], merged_data['사용량_MWh'], alpha=0.5)
plt.title('서울 평균 온도와 에너지 사용량의 관계')
plt.xlabel('평균 온도 (°C)')
plt.ylabel('에너지 사용량 (MWh)')

# 2차 다항식 추세선 추가
z = np.polyfit(merged_data['Average Temperature'], merged_data['사용량_MWh'], 2)
p = np.poly1d(z)
temp_range = np.linspace(merged_data['Average Temperature'].min(), merged_data['Average Temperature'].max(), 100)
plt.plot(temp_range, p(temp_range), "r--", alpha=0.8)

plt.show()

# 상관계수 계산
correlation = merged_data['Average Temperature'].corr(merged_data['사용량_MWh'])
print(f"온도와 에너지 사용량의 상관계수: {correlation:.2f}")

# 월별 평균 계산 및 출력
monthly_avg = merged_data.groupby('월')[['Average Temperature', '사용량_MWh']].mean()
print("\n월별 평균:")
print(monthly_avg)

# 극단값 확인
print("\n에너지 사용량 최대:")
print(merged_data.loc[merged_data['사용량_MWh'].idxmax()])
print("\n에너지 사용량 최소:")
print(merged_data.loc[merged_data['사용량_MWh'].idxmin()])

print("\n온도 최대:")
print(merged_data.loc[merged_data['Average Temperature'].idxmax()])
print("\n온도 최소:")
print(merged_data.loc[merged_data['Average Temperature'].idxmin()])

# 데이터 샘플 출력
print("\nMerged Data Sample:")
print(merged_data.head())
print("\nMerged Data Info:")
merged_data.info()