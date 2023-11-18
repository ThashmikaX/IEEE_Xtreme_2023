def find_max_path_with_constraints(paths, B, K):
    max_sum = 0
    selected_path = None

    for path in paths:
        current_sum = 0
        consecutive_below_B = 0

        for value in path:
            if value >= B:
                current_sum += value
                consecutive_below_B = 0
            else:
                consecutive_below_B += 1

                if consecutive_below_B >= K:
                    break
                else:
                    current_sum += value

        if current_sum > max_sum:
            max_sum = current_sum
            selected_path = path

    if selected_path is None:
        return "No path satisfies the criteria."

    return selected_path, max_sum

paths = [
    [3, 5, 3, 7, 1, 8, 4],
    [3, 5, 3, 6, 1, 8, 4],
    [3, 5, 3, 6, 3, 8, 4],
    [3, 5, 3, 6, 3, 5, 4],
    [3, 5, 5, 6, 1, 8, 4],
    [3, 5, 5, 6, 3, 8, 4],
    [3, 5, 5, 6, 3, 5, 4],
    [3, 5, 5, 6, 3, 8, 4],
    [3, 5, 5, 6, 3, 5, 4],
    [3, 5, 5, 6, 5, 5, 4],
    [3, 4, 5, 6, 1, 8, 4],
    [3, 4, 5, 6, 3, 8, 4],
    [3, 4, 5, 6, 3, 5, 4],
    [3, 4, 5, 6, 3, 8, 4],
    [3, 4, 5, 6, 3, 5, 4],
    [3, 4, 5, 6, 5, 5, 4],
    [3, 4, 3, 6, 3, 8, 4],
    [3, 4, 3, 6, 3, 5, 4],
    [3, 4, 3, 6, 5, 5, 4],
    [3, 4, 3, 7, 5, 5, 4]
    # Add the rest of your paths here
]

B = 7
K = 3


result = find_max_path_with_constraints(paths, B, K)

if isinstance(result, tuple):
    selected_path, max_sum = result
    print("Selected Path:", selected_path)
    print("Maximum Sum:", max_sum)
else:
    print(result)
