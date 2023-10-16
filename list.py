"""def my_sum(input_list):
    if not input_list:
        return 0
    
    return input_list.pop()+my_sum(input_list)
    
list_test=[1,2,3,4,5]
print(my_sum(list_test)) """

"""def my_reserve(input_list):
    if not input_list:
        return 
    
    print(input_list.pop())
    my_reserve(input_list)
    
list_test=[1,2,3,4,5]
my_reserve(list_test) """

"""def my_order(input_list):
    if not input_list:
        return
    
    print(input_list.pop(0))
    my_order(input_list)

list_test = [1,2,3,4,5]
my_order(list_test) """

"""
def my_order(input_list):
    if not input_list:
        return
    
    print(input_list.pop(0))
    my_order(input_list)

list_test = [1, 2, 3, 4, 5]
my_order(list_test)

def my_reserve(input_list):
    if not input_list:
        return

    print(input_list.pop(), end=" ")
    my_reserve(input_list)

list_test=[1, 2, 3, 4, 5]
my_reserve(list_test)

def my_sum(input_list):
    if not input_list:
        return 0
    
    return input_list.pop(0)+my_sum(input_list)

list_test=[1, 2, 3, 4, 5]
print(my_sum(list_test))

"""

"""def my_print(input_list):
    if not input_list:
        return
    
    print(input_list.pop(0))
    my_print(input_list)

list_test = [1, 2, 3, 4, 5]
my_print(list_test)
"""
"""
def my_pop(input_list):
    if not input_list:
        return None
    last_item=input_list[-1]
    del input_list[-1]

    return last_item

list_test = [1,2,3,4,5]
print(my_pop(list_test))
"""

"""
def my_pop(input_list):
    if not input_list:
        return None
    
    last_item=input_list[-1]
    del input_list[-1]

    return last_item

list_test = [1,2,3,4,5]
print(my_pop(list_test))
"""

"""def my_pop(input_list):
    if not input_list:
        return None
    
    last_item = input_list[-1]
    del input_list[-1]

    return last_item

list_test = [1,2,3,4,5]
print(my_pop(list_test)) """

"""
def my_pop(input_list):
    if not input_list:
        return None
    
    last_item=input_list[-1]
    del input_list[-1]

    return last_item
    
list_test = [1,2,3,4,5]
print(my_pop(list_test)) """

