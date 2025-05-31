def min_time_to_paint(K, T, L):
    def can_paint_in_time(max_time):
        painters = 1
        current_sum = 0

        for length in L:
            if current_sum + length > max_time:
                painters += 1
                current_sum = length
                if painters > K:
                    return False
            else:
                current_sum += length

        return True

    left, right = max(L), sum(L)

    while left < right:
        mid = (left + right) // 2
        if can_paint_in_time(mid):
            right = mid
        else:
            left = mid + 1

    result_time = left
    painters_result = []
    current_painter = []
    current_sum = 0
    painters_used = 1

    for length in L:
        if current_sum + length > result_time:
            painters_result.append(current_painter)
            current_painter = [length]
            current_sum = length
            painters_used += 1
        else:
            current_painter.append(length)
            current_sum += length

    painters_result.append(current_painter)

    for i, painter in enumerate(painters_result):
        print(f"Painter {i+1}: {painter} ({sum(painter)})")

    return result_time * T


if __name__ == "__main__":
    K = 10
    T = 5
    L = [10, 5, 10, 15, 10, 5, 10, 15, 20, 20, 15, 20]

    print("Min_time_to_paint:", min_time_to_paint(K, T, L))
