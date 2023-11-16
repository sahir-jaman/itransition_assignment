def sort_by_binary_count(arr):
    def count_ones(n):
        return bin(n).count('1')

    def sorting_key(x):
        return count_ones(x), x

    return sorted(arr, key=sorting_key)

# Test case
result = sort_by_binary_count([3, 7, 8, 9])
print(result)  # Output: [8, 3, 9, 7]
