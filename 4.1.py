def move_zeros(arr):
    non_zero_elements = [num for num in arr if num != 0]
    zero_count = arr.count(0)
    return non_zero_elements + [0] * zero_count


print(move_zeros([0, 1, 0, 12, 3]))
print(move_zeros([0]))
print(move_zeros([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))