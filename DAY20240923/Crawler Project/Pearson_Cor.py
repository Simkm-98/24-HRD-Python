import pandas as pd
import numpy as np
from scipy import stats

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

# 피어슨 상관계수 계산
correlation, p_value = stats.pearsonr(merged_data['Average Temperature'], merged_data['사용량_MWh'])

# 95% 신뢰구간 계산
n = len(merged_data)
r = correlation
stderr = 1.0 / np.sqrt(n-3)
delta = 1.96 * stderr
lower = np.tanh(np.arctanh(r) - delta)
upper = np.tanh(np.arctanh(r) + delta)

print(f"온도와 에너지 사용량의 피어슨 상관계수: {correlation:.4f}")
print(f"p-값: {p_value:.4f}")
print(f"95% 신뢰구간: ({lower:.4f}, {upper:.4f})")

# 스피어만 상관계수 계산 (비선형 관계를 더 잘 포착할 수 있음)
spearman_corr, spearman_p = stats.spearmanr(merged_data['Average Temperature'], merged_data['사용량_MWh'])

print(f"\n온도와 에너지 사용량의 스피어만 상관계수: {spearman_corr:.4f}")
print(f"p-값: {spearman_p:.4f}\n")

# 온도 구간별 상관계수 계산
low_temp = merged_data[merged_data['Average Temperature'] < 10]
mid_temp = merged_data[(merged_data['Average Temperature'] >= 10) & (merged_data['Average Temperature'] < 20)]
high_temp = merged_data[merged_data['Average Temperature'] >= 20]

print("온도 구간별 피어슨 상관계수:")
for temp_range, data in [("낮은 온도 (<10°C)", low_temp), ("중간 온도 (10-20°C)", mid_temp), ("높은 온도 (>20°C)", high_temp)]:
    corr, p_value = stats.pearsonr(data['Average Temperature'], data['사용량_MWh'])
    print(f"{temp_range}: 상관계수 = {corr:.4f}, p-값 = {p_value:.4f}")

print("\n온도 구간별 스피어만 상관계수:")
for temp_range, data in [("낮은 온도 (<10°C)", low_temp), ("중간 온도 (10-20°C)", mid_temp), ("높은 온도 (>20°C)", high_temp)]:
    corr, p_value = stats.spearmanr(data['Average Temperature'], data['사용량_MWh'])
    print(f"{temp_range}: 상관계수 = {corr:.4f}, p-값 = {p_value:.4f}")