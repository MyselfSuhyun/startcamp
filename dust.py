# 조건에 따른 실행문장 선택하기 : 조건문
# 미세먼지 농도(dust)의 값이 50이상이면 '50초과' 50이하이면 '50이하'를 출력하기
dust = 90

# #if 조건문:         조건문 안에는 참/거짓을 따질 수 있는 표현식(Expression이 들어가야 한다.
# #   실행할 문장
# #else:
# #   실행할 문장

# if dust>50: #dust가 50초과이면, 아래문장 실행
#     print('50초과')
# else: #dust가 50초과가 아니면, 아래문장 실행
#     print('50이하')

# #if는 필수인데 else(elif)는 선택
# if dust< 50:
#     print('50미만')
# else:
#     print('50이상')

#0~30, 31~80, 81~150, 151~
if 150<dust: #150 초과
    print('매우 나쁨')
elif 80<dust: #150이하, 80초과
    print('나쁨')
elif 30<dust: #80이하, 30초과
    print('SoSo')
else:#30이하
    print('Good')
