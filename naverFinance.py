#네이버 금융 증시 주요 뉴스 top6
!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
 

import time
from selenium import webdriver
 

 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

url = "https://finance.naver.com/news/" 
driver.get(url)
 
update = driver.find_element_by_css_selector(".main_news")

top6 = update.text
top = list(map(str, top6.split('\n')))

#top6 뉴스 전체 출력 CSV 파일 만들기
for i in range(6):
  line=f'{top[i]}'
  print(line)

with open('top6.csv', 'w') as fp:
  for i in range(6):
    line=f'{top[i]}'
    fp.write(line)

#top6 뉴스 중 뉴스 골라보기
select = list(map(int, input('몇 번째 뉴스를 골라올까요?(띄워쓰기로 숫자를 구분하세요)').split()))

for i in (select):
  line=f'{top[i-1]}'
  print(line)

with open('top6_select.csv', 'w') as fp:
  for i in range(len(select)):
    line=f'{top[select[i]-1]}\n'
    fp.write(line)
