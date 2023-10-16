def my_pop(input_list):
    if not input_list:
        return None
    
    last_item = input_list[-1]
    del input_list[-1]

    return last_item

list_test = [1,2,3,4,5]
print(my_pop(list_test))