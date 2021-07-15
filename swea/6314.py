data_list = list(range(1,11))
filter_list = list(filter(lambda x: x%2==0, data_list))
print("{0}".format(filter_list))