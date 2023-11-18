def max_sum_path(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Create a dynamic programming table to store the maximum sum at each cell.
    dp = [[0] * cols for _ in range(rows)]

    # Create a table to keep track of the values in the path.
    path_values = [[None] * cols for _ in range(rows)]

    # Initialize the first cell with the value from the matrix.
    dp[0][0] = matrix[0][0]
    path_values[0][0] = [matrix[0][0]]

    # Fill the first row and first column of the DP and path_values tables.
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
        path_values[i][0] = path_values[i - 1][0] + [matrix[i][0]]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
        path_values[0][j] = path_values[0][j - 1] + [matrix[0][j]]

    # Fill the rest of the DP and path_values tables.
    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
                path_values[i][j] = path_values[i - 1][j] + [matrix[i][j]]
            else:
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
                path_values[i][j] = path_values[i][j - 1] + [matrix[i][j]]

    # The bottom-right cell contains the maximum sum, and path_values[rows-1][cols-1] contains the path values.
    return dp[rows - 1][cols - 1], path_values[rows - 1][cols - 1]

# Define your 2x3 matrix with values between 0 and 9 (including 0 and 9).
matrix = [
    [5, 5, 6, 5],
    [3, 6, 3, 5],
    [7, 1, 8, 4]
]

maximum_sum, maximum_sum_path_values = max_sum_path(matrix)
print(f"The maximum sum is: {maximum_sum}")
print(f"The path that achieves the maximum sum is: {maximum_sum_path_values}")
