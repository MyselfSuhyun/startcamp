n = {} 
def pibonacci(x):
    s=''
    for i in range(1,x+1):    
        if(i<3):
            n[i]=1
        else:
            n[i]=n[i-1]+n[i-2]
        s+= str(n[i])+', '
    print('[%s]' % s[:-2])
    




T = int(input())
pibonacci(T)
