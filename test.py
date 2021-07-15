N= input()
data_str=N
data_list= list(data_str)
li = len(data_list)
s=''
for i in range(li):
    s+=data_list[i]+' '
print(s)