# def snail(n):
#     arr = [[0 for j in range(n)] for i in range(n)] #1
#     row = 0 #2
#     col = -1 #2
#     cnt = 1 #3
#     trans = 1 #4
#     while n > 0: #5
#         for i in range(n): #6
#             col += trans
#             arr[row][col] = cnt
#             cnt += 1
#         n -= 1 #7
#         for j in range(n): #8
#             row += trans
#             arr[row][col] = cnt
#             cnt += 1
#         trans *= -1 #9
#     return arr


# arr = snail(4)
# for i in arr:
#     for j in i:
#         print('%5d' %j , end=' ')
#     print()
n = int(input())
snail = [[0]*n for i in range(n)]
cnt = n*n
inital = 0
y = n
h = n

# while y > 0 and h > 0:
#     for i in range(inital, inital+h):
#         snail[inital][i] = cnt
#         cnt -= 1
#     for i in range(inital+1, inital+y):
#         snail[i][inital+h-1] = cnt
#         cnt -= 1
#     for i in range(inital+h-2, inital-1, -1):
#         snail[inital+y-1][i] = cnt
#         cnt -= 1
#     for i in range(inital+y-2, inital, -1):
#         snail[i][inital] = cnt
#         cnt -= 1

#     inital += 1
#     y -= 2
#     h -= 2

#90도 회전
while y > 0 and h > 0:
    for i in range(inital, inital+y):
        snail[i][inital+h-1] = cnt
        cnt -= 1
    for i in range(inital+h-2, inital-1, -1):
        snail[inital+y-1][i] = cnt
        cnt -= 1
    for i in range(inital+y-2, inital, -1):
        snail[i][inital] = cnt
        cnt -= 1
    for i in range(inital, inital+h-1):
        snail[inital][i] = cnt
        cnt -= 1

    inital += 1
    y -= 2
    h -= 2

for i in range(0, n):
    for j in range(0, n):
        print("%3d" % snail[i][j], end=' ')
    print()