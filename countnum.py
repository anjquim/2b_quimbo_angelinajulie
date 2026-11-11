def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("Count:", count_number([1, 2, 2, 3, 2], 2))
print("Count:", count_number([], 5))
print("Count:", count_number([9, 5, 6], 7))