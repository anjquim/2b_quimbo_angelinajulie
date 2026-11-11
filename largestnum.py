def largest_number(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")

    if len(arr) == 1:
        return arr[0]

    largest = largest_number(arr[1:])

    if arr[0] > largest:
        return arr[0]
    else:
        return largest


print("Largest:", largest_number([5, 10, 3, 8]))
print("Largest:", largest_number([20]))
print("Largest:", largest_number([2, 5, 10, 18]))
print("Largest:", largest_number([-9, -5, -10]))