def get_subsets(lst, index=0, current=[], result=None):
    if result is None:
        result = []
    if index == len(lst):
        result.append(current[:])  # Append a copy of current subset
        return
    get_subsets(lst, index + 1, current + [lst[index]], result)  # Include element
    get_subsets(lst, index + 1, current, result)  # Exclude element
    return result

nums = [1, 2, 3]
subsets = get_subsets(nums)
print(subsets)
