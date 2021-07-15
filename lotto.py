import random

numbers = range(1,46) # 0,1,2,3,4 시작점은 생략이 가능하다.
#range(a,b) :a는 범위에 포함되고, b는 범위에 포함되지 않는다. 즉 a부터 b전까지
#1~45니까 range는 1,46
print(numbers)
#random.sample(seq,k): 시퀀스에서 랜덤한 중복되지 않는 길이 k의 리스트 반환
lotto = random.sample(numbers,6) 

print('로또 번호는',lotto)
# 3개 맞으면 5등
# 4개 맞으면 4등
# 5개 맞으면 3등
# 5+1맞으면 2등
# 6개 맞으면 1등