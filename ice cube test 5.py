def function(matrix, i, B, K):
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, current_sum, consecutive_below_B):
        current_sum += matrix[x][y]
        if x == rows - 1 and y == cols - 1:
            if consecutive_below_B < K:
                max_sum[0] = max(max_sum[0], current_sum)
        else:
            for dx, dy in [(1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y):
                    if matrix[new_x][new_y] >= B:
                        dfs(new_x, new_y, current_sum, 0)
                    else:
                        dfs(new_x, new_y, current_sum, consecutive_below_B + 1)

    rows, cols = len(matrix), len(matrix[0])
    max_sum = [0]
    dfs(0, 0, 0, 0)

    if max_sum[0] > 0:
        print(f"Case {i + 1}: {max_sum[0]}")
    else:
        print(f"Case {i + 1}: IMPOSSIBLE")

T = int(input())
for i in range(T):
    N, M, K, B = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(N)]
    function(x, i, B, K)
