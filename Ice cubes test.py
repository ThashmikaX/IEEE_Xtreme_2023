def max_path_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Create a dynamic programming table to store the maximum sum at each cell.
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first cell with the value from the matrix.
    dp[0][0] = matrix[0][0]

    # Fill the first row and first column of the DP table.
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Fill the rest of the DP table.
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell contains the maximum sum.
    return dp[rows - 1][cols - 1]

# Define your 2x3 matrix with values between 0 and 9 (including 0 and 9).
matrix = [
    [3, 4, 3, 7],
    [5, 5, 6, 5],
    [3, 6, 3, 5],
    [7, 1, 8, 4]
]

maximum_sum = max_path_sum(matrix)
print(f"The maximum sum path is: {maximum_sum}")
