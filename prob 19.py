def is_subset(a, b):
    from collections import Counter

    count_a = Counter(a)
    count_b = Counter(b)

    for key in count_b:
        if count_b[key] > count_a[key]:
            return False
    return True


# Example
print(is_subset([11, 7, 1, 13, 21, 3, 7, 3],
                [11, 3, 7, 1, 7]))  # Output: True