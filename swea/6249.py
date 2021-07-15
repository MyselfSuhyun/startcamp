a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N=input()
n=int(N)
ln= len(N)
s=''
for i in range(1,ln+1):
    k = int(n%10)
    a[k]+=1
    if(n<10):
        break
    else:
        n = n/10

print('0 1 2 3 4 5 6 7 8 9')
for i in range(10):
    s+=str(a[i])+' '
print(s)