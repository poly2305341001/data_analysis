# pip install requests
# pip install BeautifulSoup4
# pip install selenium  # 웹 애플리케이션 테스팅을 위한 프레임워크
# pip install webdriver_manager # selenium이 chrome을 제어할 수 있도록 chromedriver를 버전에 맞게 자동 다운하고 path에 추가

# 크롤링할 사이트에 접속 준비
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# HTML 소스 파싱 준비
from bs4 import BeautifulSoup

# 동적 웹페이지 작동 준비
import time

# # 데이터 저장 준비
# import pandas as pd

# import requests


# 크롬 드라이버 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 사이트에 접속
driver.get('https://www.topuniversities.com/world-university-rankings/2022')

# 동적 페이지 갱신을 위한 여유시간
time.sleep(30)

# 웹 페이지 HTML 소스 파싱
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 중복되는 태그 제외, 학교 이름과 각 점수 파싱
rm_duplicate = soup.select('div.row.ind-row.firstloaded.hide-this-in-mobile-indi div.td-wrap-in')
f = open('univ_score.txt', 'w')
for line in rm_duplicate:
    text = line.get_text()
    f.write(text + '\n')
f.close()


# univ_name = list()
# univ_url = list()
#
# for a_tag in soup.select('a.uni-link'):
#     university_name = a_tag.text
#     university_url = a_tag['href']
#
#     univ_name.append(university_name)
#     univ_url.append(university_url)
#     # print(f'University Name: {university_name}')
#     # print(f'University URL: {university_url}')
#
# print(univ_name)
# print(univ_url)



# parameters = {
#     "tab": "indicators",
#     "region": "Asia",
#     "countries": "kr",
#     "sort_by": "rank",
#     "order_by": "asc"
# }

# response = requests.get('https://www.topuniversities.com/world-university-rankings/2022', params=parameters)
# response.raise_for_status()
# data = open('test.txt', 'w')
# data.write(response.text)
# data.close()
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     for a_tag in soup.select('a.uni-link'):
#         university_name = a_tag.text
#         university_url = a_tag['href']
#
#         print(f'University Name: {university_name}')
#         print(f'University URL: {university_url}')



# # 필요한 부분 추출
# rankings = soup.select('a.uni-link')
#
# # 데이터 저장
# data = pd.DataFrame(rankings)
# data.to_csv('rankings.csv')