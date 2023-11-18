def function(matrix, i, B, K):
    def is_valid(x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

    def dfs(x, y, current_path):
        current_path.append(matrix[x][y])
        if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
            all_paths.append(list(current_path))
        else:
            for dx, dy in [(1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y):
                    dfs(new_x, new_y, current_path)
        current_path.pop()
    all_paths = []
    dfs(0, 0, [])
    mask = [1] * len(all_paths)
    max_sum = 0
    for index, path in enumerate(all_paths):
        current_sum = 0
        consecutive_below_B = 0

        for value in path:
            if value >= B:
                current_sum += value
                consecutive_below_B = 0
            else:
                consecutive_below_B += 1

                if consecutive_below_B >= K:
                    mask[index] = 0
                    break
                else:
                    current_sum += value
        if current_sum > max_sum:
            max_sum = current_sum
    if 1 in mask:
        print(f"Case {i + 1}: {max_sum}")
    else:
        print(f" Case {i + 1}: IMPOSSIBLE")

T = int(input())
for i in range(T):
    N, M, K, B = map(int, input().split())
    x = [list(map(int,input().rstrip().split())) for i in range(N)]
    function(x, i, B, K)