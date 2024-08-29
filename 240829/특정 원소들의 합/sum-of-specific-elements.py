# Reading the input
matrix = []
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initializing the sum
total_sum = 0

# Adding the specific elements
total_sum += matrix[0][0]             # First row, first element
total_sum += matrix[1][0] + matrix[1][1]  # Second row, first two elements
total_sum += matrix[2][0] + matrix[2][1] + matrix[2][2]  # Third row, first three elements
total_sum += matrix[3][0] + matrix[3][1] + matrix[3][2] + matrix[3][3]  # Fourth row, all elements

# Printing the result
print(total_sum)