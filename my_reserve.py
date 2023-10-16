def my_reserve(input_list):
    if not input_list:
        return
    
    print(input_list.pop())
    my_reserve(input_list)

list_test=[1,2,3,4,5]
my_reserve(list_test)