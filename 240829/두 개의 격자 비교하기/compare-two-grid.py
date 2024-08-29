n, m = map(int, input().split())  # Read n and m as integers

arr_1 = []
arr_2 = []
final = []

# Read the first array
for _ in range(n):
    arr_1.append(list(map(int, input().split())))  # Split input and convert each to int

# Read the second array
for _ in range(n):
    arr_2.append(list(map(int, input().split())))  # Split input and convert each to int

# Compare the two arrays and create the final array
for i in range(n):
    temp = []
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            temp.append(0)  # Append 0 as an integer
        else:
            temp.append(1)  # Append 1 as an integer
    final.append(temp)

# Print the final array
for item in final:
    print(' '.join(str(x) for x in item))  # Convert each integer to a string and join