def my_order(input_list):
    if not input_list:
        return 
    
    print(input_list.pop(0))
    my_order(input_list)

def my_reserve(input_list):
    if not input_list:
        return
    
    print(input_list.pop())
    my_reserve(input_list)



list_test = [1,2,3,4,5]
my_reserve(list_test)

list_test = [1,2,3,4,5]
my_order(list_test)