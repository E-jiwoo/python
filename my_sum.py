def my_sum(input_list):
    if not input_list:
        return 0
    
    return input_list.pop(0)+my_sum(input_list)

list_test=[1,2,3,4,5]
print(my_sum(list_test))