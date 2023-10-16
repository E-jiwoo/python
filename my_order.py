def my_order(input_list):
    if not input_list:
        return
    
    print(input_list.pop(0))
    my_order(input_list)

list_test=[1,2,3,4,5]
my_order(list_test)