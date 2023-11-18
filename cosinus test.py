# Define two integer lists of the same length
list1 = [3, 7, 2, 5, 1]
list2 = [10, 4, 8, 2, 6]

# Create a list of tuples, where each tuple contains a pair of corresponding elements
pairs = list(zip(list1, list2))

# Find the minimal duo (pair with the smallest sum)
minimal_duo = min(pairs, key=lambda pair: pair[0] + pair[1])

# minimal_duo[0] contains the element from list1, and minimal_duo[1] contains the element from list2
print(f"The minimal duo is ({minimal_duo[0]}, {minimal_duo[1]}) with a sum of {minimal_duo[0] + minimal_duo[1]}.")
