def remove_duplicates(arr):
    unique = []
    for i in range(len(arr)):
        found = False
        for j in range(len(unique)):
            if arr[i] == unique[j]:
                found = True
                break
        if not found:
            unique.append(arr[i])
    return unique

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print(result)  # Output: [1, 2, 3, 4, 5]
