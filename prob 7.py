arr = [2, 3, -8, 7, -1, 2, 3]

max_sum = current = arr[0]
for num in arr[1:]:
    current = max(num, current + num)
    max_sum = max(max_sum, current)

print(max_sum)