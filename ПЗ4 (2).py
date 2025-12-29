def sum_list(list):
    sm = 0
    for elem in list:
        try:
            sm += elem
        except:
            sm += sum_list(elem)
    return sm

my_list = [1, [2,3,7], [9], [4, [5,6]], [[-6, 1], [-5, 4]], [-1, -5], 0]
print (sum_list(my_list))



