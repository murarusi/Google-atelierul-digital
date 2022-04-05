#1
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#2
asc_order_list = my_list.copy()
asc_order_list.sort()
print(asc_order_list)

#3
desc_order_list = my_list.copy()
desc_order_list.sort(reverse=True)
print(desc_order_list)

#4
print(asc_order_list[0:-1:2])

#5
print(asc_order_list[1:10: 2])

#6
print(asc_order_list[5:10: 3])

print(my_list)

