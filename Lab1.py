def fix_monoton(arr):
    if not arr:
        return []

    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    if increasing or decreasing:
        return arr

    fixed_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= fixed_arr[-1]:
            fixed_arr.append(arr[i])

    return fixed_arr


arr = [1, 3, 2, 4, 5, 6, 8, 7, 9, 10]
print(fix_monoton(arr))
