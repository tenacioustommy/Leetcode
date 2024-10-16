def min_operations_to_exceed(x, y, a):
    operations = 0
    a.sort(reverse=True)  # Sort the array in descending order to maximize the multiplication effect

    while x < y:
        if not a:
            return -1  # If the array is empty and x is still less than y, return -1

        max_element = a[0]
        x *= max_element
        a = [elem for elem in a if elem != max_element]  # Remove all occurrences of max_element from the array
        operations += 1

    return operations

# Example usage:
x = 2
y = 10
a = [2, 3, 5]
print(min_operations_to_exceed(x, y, a))  # Output should be the minimum number of operations
