N= input()
ln= len(N)
n=int(N)
a=list[ln]
s=0
for i in range(1,ln+1):
    s += int(n%10)
    if(n<10):
        break
    else:
        n = n/10
    
    
print(s)