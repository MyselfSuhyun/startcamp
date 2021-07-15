data = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
data_list = list(data)
li = len(data_list)
sum=0
for i in range(li):
    if(data_list[i]=='A'):
        sum+=4
    elif(data_list[i]=='B'):
        sum+=3
    elif(data_list[i]=='C'):
        sum+=2
    else:
        sum+=1
print(sum)