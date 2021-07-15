data_list = list(range(1,11))

filter_list = list(filter(lambda x: x%2==0,data_list))
map_list = list(map(lambda x: x*x,filter_list))
print("{0}".format(map_list))