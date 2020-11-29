from itertools import permutations

my_list = [1, 2, 3, 4, 5]
list_len = len(my_list)

while(list_len):
    perm = permutations(my_list, list_len)

    for el in perm:
        print(el)

    list_len = list_len-1