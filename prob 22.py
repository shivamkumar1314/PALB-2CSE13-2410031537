def chocolate_distribution(arr, m):
    if m > len(arr):
        return -1

    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff