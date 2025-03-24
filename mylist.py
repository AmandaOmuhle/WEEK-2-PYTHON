my_list = [10, 20, 30, 40]

my_list.insert(1, 15)
my_list.extend([50, 60,70])
my_list.remove(70)
my_list.sort()
index_of_30 = my_list.index(30)
print(index_of_30)  # Output: 3
print(my_list)  # Output: [10, 15, 20, 30, 40]

