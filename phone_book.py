#각 식당마다 전화번호를 매칭 시키기
#전화번호부에서 찾으려고 하는 목적 데이터는 전화번호
#식당의 이름을 이용해서 전화번호를 찾는다 >>>
#김밥천국 >> 김밥나라?? 식당일므을 정확하게 알아야 전화번호를 찾는다
#식당이름이 key 값이다.
#key-value 형태로 이루어진 데이터는 dictionary라는 형태로 저장한다.
#'식당이름 - 전화번호' 가 한 쌍의 데이터
#{key : value, key1:value1, key2:value2, ...}
menu = {'한식':'123-456','일식':'222-333','양식':'444-555','중식':'666-777'}

print(menu['한식'])

#랜덤으로 전화번호는 어떻게 가져올까요?