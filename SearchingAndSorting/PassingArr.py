def call_by_value(x):
    x = x + 10
    print("Inside function (by value):", x)

def pass_arr(arr):
    arr[0], arr[1] = arr[1]+1, arr[0]+2

my_list = [10, 20, 30]
print("Before passing:", my_list)
pass_arr(my_list)
print("After passing:", my_list) 

# a = 5
# call_by_value(5)  # Output: None
# print(a)