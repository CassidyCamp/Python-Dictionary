def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for i, num in enumerate(numbers):
        result.setdefault(num, []).append(i)
    return result


nums = [7, 6, 9, 0, 2, 4, 7, 7, 5, 12, 12, 1, 6, 9, 2, 5]
print(group_indices(nums))
