bl2 = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a=0
b=0
o=0
ab=0
for i in range(0,len(bl2)):
    s=bl2[i]
    if(s=='A'):
        a+=1
    elif(s=='B'):
        b+=1
    elif(s=='O'):
        o+=1
    else:
        ab+=1
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}"%(a,o,b,ab))

