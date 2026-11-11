def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


print("Sum:", sum_array([1, 2, 3, 4, 5]))
print("Sum:", sum_array([]))
print("Sum:", sum_array([15]))
print("Sum:", sum_array([-5, 8, -2]))