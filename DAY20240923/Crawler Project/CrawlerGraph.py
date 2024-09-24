import pandas as pd
import matplotlib.pyplot as plt
import platform

# UTF-8 설정
plt.rcParams['axes.unicode_minus'] = False

# 운영 체제별 폰트 설정
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic' 
else:
    plt.rcParams['font.family'] = 'NanumGothic'

# 엑셀 파일 경로 설정
energy_file_path = r"C:\Code\Python\pythonProject\seoul_average_energy_usage_2019_2023.csv"
temperature_file_path = r"C:\Code\Python\pythonProject\seoul_temperature_data.csv"

# 데이터 처리
energy_df = pd.read_csv(energy_file_path)
energy_df['날짜'] = pd.to_datetime(energy_df['년도'].astype(str) + '-' + energy_df['월'].astype(str).str.zfill(2) + '-01')
energy_df['사용량'] = pd.to_numeric(energy_df['사용량'].astype(str).str.replace(',', ''), errors='coerce')
energy_df['사용량(KWh)'] = energy_df['사용량'] * 1000

temp_df = pd.read_csv(temperature_file_path)
temp_df['Date'] = pd.to_datetime(temp_df['Date'])

merged_df = pd.merge(energy_df, temp_df, left_on='날짜', right_on='Date', how='inner')

# 그래프 생성
years = sorted(merged_df['년도'].unique())
fig, axs = plt.subplots(2, 2, figsize=(20, 16))
fig.suptitle('서울 에너지 사용량과 평균 온도 (2020-2023)', fontsize=20, y=0.95)
axs = axs.ravel()

# 서브플롯 간격 조정
plt.subplots_adjust(hspace=0.3, wspace=0.3)

for idx, year in enumerate(years):
    year_data = merged_df[merged_df['년도'] == year]

    ax = axs[idx]
    ax2 = ax.twinx()

    # 에너지 사용량 (선 그래프)
    line1 = ax.plot(year_data['월'], year_data['사용량(KWh)'], color='blue', marker='o')

    # 평균 온도 (막대 그래프)
    bar1 = ax2.bar(year_data['월'], year_data['Average Temperature'],
                   width=0.5, color='red', alpha=0.5)

    # 0도 기준선 추가
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.7)

    # 그래프 설정
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(range(1, 13), rotation=0, fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.7)

    # y축 범위 설정
    ax.set_ylim(year_data['사용량(KWh)'].min() * 0.95, year_data['사용량(KWh)'].max() * 1.05)
    temp_min = min(year_data['Average Temperature'].min(), 0)
    temp_max = year_data['Average Temperature'].max()
    ax2.set_ylim(temp_min - 5, temp_max + 5)

    # 제목과 설명을 그래프 상단에 추가
    ax.text(0.5, 1.03, f'{year}년', color='black', ha='center', va='top', transform=ax.transAxes, fontsize=8)
    ax.text(0.5, 0.98, '에너지 사용량 (KWh)', color='blue', ha='center', va='top', transform=ax.transAxes, fontsize=8)
    ax.text(0.5, 0.93, '평균 온도 (°C)', color='red', ha='center', va='top', transform=ax.transAxes, fontsize=8)

    # 축 숨기기
    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 전체 제목을 위한 여백 조정
plt.show()