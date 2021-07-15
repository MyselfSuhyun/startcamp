#내가 제출한 거
# N=int(input())
# sum = 0

# for i in range(1,N+1):
#     sum+=i

# print(sum)

#교수님이 알려주신 것
#input() >> 한 줄 입력 받기 :
#input()의 결과는 문자열 '26' >> 26
#정수형 문자열을  정수로 바꾸는 함수 int('문자열')
N =int(input())

i=1
#계속 누적합을 알고 있어야 합니다.
# 누적합을 저장할 변수를 하나 선언합니다.
result = 0 # 아무것도 더하지 않으면 0이니까 0으로 초기화
while i <=N:
    result = result + i
    i= i+1
print(result)

# 천재 능력자님이 알려주신 것.
# a=int(input())
# b=0
# if a<=10000:
#     for i in range(1,a+1):
#         b+=i
# print(b)    