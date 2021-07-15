import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text

# 우리가 받은 데이터는 html이라는 문서인데 문서내에서 유용한 정보를 뽑아야한다.
# >> html을 해석하는게 상당히 힘들다. >> 누군가 만들어 놓은걸 쓰자.
#>> BeautifulSoup4를 쓰자!
#response를 사용하기 십게 가공해서 data에 넣어줘
data = BeautifulSoup(response, 'html.parser')
# data에서 원하는 데이터를 뽑아내기 : select_one()
# 어떤 데이터를 뽑을건지 알려줘야함: 경로>> 선택자
k_value = data.select_one('#KOSPI_now').text
k2_value = data.select_one('#KOSDAQ_now').text
k3_value = data.select_one('#popularItemList').text
print(f'코스피지수 : {k_value}')
print(f'코스닥 지수 : {k2_value}')
print(f'인기 검색 종목 : {k3_value}')