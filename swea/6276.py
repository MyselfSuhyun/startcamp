data_list = list(range(1,10))
sum =''
for i in range(2,10):
    map_list = list(map(lambda x: i*x,data_list))
    filter_list = list(filter(lambda x: x%3!=0 and x%7!=0, map_list))
    sum += "{0}".format(filter_list)+', '
print('[%s]'%sum[:-2])